import streamlit as st
import pandas as pd
import schemetypedata as stdata
import dataextraction as dataex

st.title("RAGathon Challenge: Mutual Fund Performance Insights Application")
df = pd.read_csv('mutualfunds.csv')

tab1, tab2, tab3 = st.tabs(['Generate report', 'Visualize data', 'Upload reports'])
with tab1:
    monthselected = st.multiselect('Select the month', df['month and year'].unique())
    typeselected = st.multiselect('Select the scheme type', stdata.types)
    subtypeselected = st.multiselect('Select the scheme subtype', stdata.subtypes)
    namesselected = st.multiselect('Select the scheme name', stdata.names)
    result = st.button('Generate Report')
    if result:
        res = df[
            (df['month and year'].isin(monthselected)) &
            ((df['Scheme Type'].isin(typeselected)) |
            (df['Scheme Subtype'].isin(subtypeselected)) |
            (df['Scheme Name'].isin(namesselected)))
        ]
        res.columns = dataex.column_headers
        st.dataframe(res)

with tab2:
    namesselected = st.multiselect('Select the scheme name', stdata.names)

with tab3:
    st.write("Report PDF Upload")
    pdfs = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True, help="Select one or more reports in the standard pdf format to update the existing data...")
    submit = st.button("Update data")
    if submit:
        if len(pdfs) != 0:
            with st.spinner(text='Extracting data...'):
                bar = st.progress(0)
                p = 0
                for pdf in pdfs:
                    pdf_bytes = pdf.read()
                    pdf_path = "reports/{}.pdf".format(pdf.name)
                    with open(pdf_path, "wb") as f:
                        f.write(pdf_bytes)
                    newdf = pd.DataFrame(columns=dataex.column_headers)
                    tables = dataex.get_tables(pdf_path)
                    for tbname in tables:
                        table = tables[tbname]
                        newdf = dataex.add_data_to_dataframe(table, tbname, newdf)
                    df = df._append(newdf, ignore_index=True)
                    df.drop_duplicates(inplace=True)
                    bar.progress(p+int(100/len(pdfs)))
                bar.progress(100)
                df.to_csv('mutualfunds.csv', index=False)
                st.success('Done')
                st.rerun()


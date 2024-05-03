import pandas
import streamlit as st
import pandas as pd
import schemetypedata as stdata
import dataextraction as dataex

st.title("RAGathon Challenge: Mutual Fund Performance Insights Application")
df = pd.read_csv('mutualfunds.csv')
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
    st.write(res)


st.write("Report PDF Upload")
pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
submit = st.button("Update data")
if submit:
    if pdf is not None:
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
        df.to_csv('mutualfunds.csv', index=False)
        st.write('Data updated successfully')


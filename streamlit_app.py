import streamlit as st
import pandas as pd
import schemetypedata as stdata
import dataextraction as dataex
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

subtypes = ['Income/Debt Oriented Schemes (Open ended)', 'Growth/Equity Oriented Schemes (Open ended)', 'Hybrid Schemes (Open ended)','Solution Oriented Schemes (Open ended)','Other Schemes (Open ended)', 'Income/Debt Oriented Schemes (Close ended)', 'Growth/Equity Oriented Schemes (Close ended)','Other Schemes (Close ended)', 'Growth/Equity Oriented Schemes (Open ended)', 'Hybrid Schemes (Open ended)','Solution Oriented Schemes (Open ended)','Other Schemes (Open ended)', 'Income/Debt Oriented Schemes (Interval)', 'Growth/Equity Oriented Schemes (Interval)','Other Schemes (Interval)']
st.set_option('deprecation.showPyplotGlobalUse', False)

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
    option = st.radio('Get data based on ', ['Scheme name', 'Scheme type', 'Scheme subtype'])
    if option == 'Scheme name':
        title = nameselected = st.selectbox('Select the scheme name', stdata.names, key='sn')
        filtered_df = df[df['Scheme Name'] == nameselected]
    elif option == 'Scheme type':
        title = typeselected = st.selectbox('Select the scheme type', stdata.types, key='st')
        filtered_df = df[df['Scheme Type'] == typeselected]
    elif option == 'Scheme subtype':
        title = subtypeselected = st.selectbox('Select the scheme subtype', subtypes, key='sst')
        if(subtypeselected=='Income/Debt Oriented Schemes (Open ended)'):
            filtered_df = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Growth/Equity Oriented Schemes (Open ended)':
            filtered_df = df[
                (df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Hybrid Schemes (Open ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Hybrid Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Solution Oriented Schemes (Open ended)':
            filtered_df = df[
                (df['Scheme Subtype'] == 'Solution Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Other Schemes (Open ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Income/Debt Oriented Schemes (Close ended)':
            filtered_df = df[
                (df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
        elif subtypeselected == 'Growth/Equity Oriented Schemes (Close ended)':
            filtered_df = df[
                (df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
        elif subtypeselected == 'Other Schemes (Close ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
        elif subtypeselected == 'Income/Debt Oriented Schemes (Interval)':
            filtered_df = df[
                (df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
        elif subtypeselected == 'Growth/Equity Oriented Schemes (Interval)':
            filtered_df = df[
                (df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
        elif subtypeselected == 'Other Schemes (Interval)':
            filtered_df = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Interval Schemes')]

    foption = st.selectbox('Select data field ', stdata.fields)
    result = filtered_df[['{}'.format(foption), 'month and year']]
    result['month and year'] = pd.to_datetime(df['month and year'])
    result = result.sort_values('month and year')
    result = result.groupby('month and year')['{}'.format(foption)].sum().reset_index()
    st.dataframe(result)
    # Plot the line graph
    plt.figure(figsize=(15,5))
    plt.ticklabel_format(style='plain')
    plt.plot(result['month and year'], result['{}'.format(foption)], marker='o', linestyle='-')
    date_format = mdates.DateFormatter('%m-%Y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.title('{}'.format(title))
    plt.xlabel('Month and Year')
    plt.ylabel('{}'.format(foption))
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()

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


import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import os
import dataextraction as dataex
import schemetypedata as stdata

subtypes = ['Income/Debt Oriented Schemes (Open ended)', 'Growth/Equity Oriented Schemes (Open ended)', 'Hybrid Schemes (Open ended)','Solution Oriented Schemes (Open ended)','Other Schemes (Open ended)', 'Income/Debt Oriented Schemes (Close ended)', 'Growth/Equity Oriented Schemes (Close ended)','Other Schemes (Close ended)', 'Growth/Equity Oriented Schemes (Open ended)', 'Hybrid Schemes (Open ended)','Solution Oriented Schemes (Open ended)','Other Schemes (Open ended)', 'Income/Debt Oriented Schemes (Interval)', 'Growth/Equity Oriented Schemes (Interval)','Other Schemes (Interval)']
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("RAGathon Challenge: Mutual Fund Performance Insights Application")
df = pd.read_csv('mutualfunds.csv')

tab1, tab2, tab3, tab4 = st.tabs(['Generate report', 'Visualize data', 'Upload reports', 'Report PDFs'])
with tab1:
    st.markdown('#### Generate report in csv format')
    option = st.radio('Get data based on ', ['Scheme name', 'Scheme type', 'Scheme subtype'], key='tb1')
    if option == 'Scheme name':
        title = namesselected = st.multiselect('Select the scheme names', stdata.names, key='sn1')
        filtered_df = df[df['Scheme Name'].isin(namesselected)]
    elif option == 'Scheme type':
        title = typesselected = st.multiselect('Select the scheme types', stdata.types, key='st1')
        filtered_df = df[df['Scheme Type'].isin(typesselected)]
        if not filtered_df.empty:
            numerical_columns = filtered_df.select_dtypes(include=[np.number]).columns.tolist()
            filtered_df = filtered_df.groupby('month and year')[numerical_columns].sum().reset_index()
    elif option == 'Scheme subtype':
        title = subtypesselected = st.multiselect('Select the scheme subtypes', subtypes, key='sst1')
        filtered_df = pd.DataFrame()
        for subtypeselected in subtypesselected:
            if (subtypeselected == 'Income/Debt Oriented Schemes (Open ended)'):
                fdf = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Growth/Equity Oriented Schemes (Open ended)':
                fdf = df[(df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Hybrid Schemes (Open ended)':
                fdf = df[(df['Scheme Subtype'] == 'Hybrid Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Solution Oriented Schemes (Open ended)':
                fdf = df[(df['Scheme Subtype'] == 'Solution Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Other Schemes (Open ended)':
                fdf = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Income/Debt Oriented Schemes (Close ended)':
                fdf = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Growth/Equity Oriented Schemes (Close ended)':
                fdf = df[(df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Other Schemes (Close ended)':
                fdf = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Income/Debt Oriented Schemes (Interval)':
                fdf = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Growth/Equity Oriented Schemes (Interval)':
                fdf = df[(df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
            elif subtypeselected == 'Other Schemes (Interval)':
                fdf = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
                filtered_df = filtered_df._append(fdf, ignore_index=True)
        if not filtered_df.empty:
            numerical_columns = filtered_df.select_dtypes(include=[np.number]).columns.tolist()
            filtered_df = filtered_df.groupby('month and year')[numerical_columns].sum().reset_index()

    all = st.checkbox('Display all the fields', value=True)
    if not filtered_df.empty:
        filtered_df['month and year'] = pd.to_datetime(filtered_df['month and year'], errors='coerce')
        filtered_df = filtered_df.sort_values('month and year')
        filtered_df['month and year'] = filtered_df['month and year'].dt.strftime('%m-%Y')

        # Add a new column named "slno" and number it in order
        filtered_df.insert(0, 'slno', range(1, len(filtered_df) + 1))
        # Calculate sum for numeric columns
        numeric_columns = filtered_df.select_dtypes(include=[np.number]).columns
        column_sums = filtered_df[numeric_columns].sum()

        # Create a dictionary for the new row
        new_row_data = {'slno': 'Total'}

        # Iterate over columns
        for col in filtered_df.columns:
            if col == 'slno':
                continue
            elif col in numeric_columns:
                new_row_data[col] = column_sums[col]
            else:
                new_row_data[col] = ''

        # Append the new row to the DataFrame
        filtered_df = filtered_df._append(new_row_data, ignore_index=True)

    if all:
        if not filtered_df.empty and title:
            st.dataframe(filtered_df)
    else:
        fieldsselected = st.multiselect('Select the data fields to display other than month and year', stdata.allfields, key="af1")
        if fieldsselected and title:
            fieldsselected.append('month and year')
            fieldsselected.insert(0, 'slno')
            st.dataframe(filtered_df[fieldsselected])

with tab2:
    st.markdown('#### Plot the the graph of data fields vs month and year')
    option = st.radio('Get data based on ', ['Scheme name', 'Scheme type', 'Scheme subtype'], key='tb2')
    if option == 'Scheme name':
        title = nameselected = st.selectbox('Select the scheme name', stdata.names, key='sn2', index=None)
        filtered_df = df[df['Scheme Name'] == nameselected]
    elif option == 'Scheme type':
        title = typeselected = st.selectbox('Select the scheme type', stdata.types, key='st2', index=None)
        filtered_df = df[df['Scheme Type'] == typeselected]
    elif option == 'Scheme subtype':
        title = subtypeselected = st.selectbox('Select the scheme subtype', subtypes, key='sst2', index=None)
        if(subtypeselected=='Income/Debt Oriented Schemes (Open ended)'):
            filtered_df = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Growth/Equity Oriented Schemes (Open ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Hybrid Schemes (Open ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Hybrid Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Solution Oriented Schemes (Open ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Solution Oriented Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Other Schemes (Open ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Open ended Schemes')]
        elif subtypeselected == 'Income/Debt Oriented Schemes (Close ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
        elif subtypeselected == 'Growth/Equity Oriented Schemes (Close ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
        elif subtypeselected == 'Other Schemes (Close ended)':
            filtered_df = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Close Ended Schemes')]
        elif subtypeselected == 'Income/Debt Oriented Schemes (Interval)':
            filtered_df = df[(df['Scheme Subtype'] == 'Income/Debt Oriented Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
        elif subtypeselected == 'Growth/Equity Oriented Schemes (Interval)':
            filtered_df = df[(df['Scheme Subtype'] == 'Growth/Equity Oriented Schemes') & (df['Scheme Type'] == 'Interval Schemes')]
        elif subtypeselected == 'Other Schemes (Interval)':
            filtered_df = df[(df['Scheme Subtype'] == 'Other Schemes') & (df['Scheme Type'] == 'Interval Schemes')]

    foption = st.selectbox('Select data field ', stdata.fields, index=None)
    if title is not None and foption is not None:
        result = filtered_df[['{}'.format(foption), 'month and year']]
        result['month and year'] = pd.to_datetime(result['month and year'], errors='coerce')
        result = result.sort_values('month and year')
        result = result.groupby('month and year')['{}'.format(foption)].sum().reset_index()
        #st.dataframe(result)

        # Plot the line graph
        plt.style.use('dark_background')
        plt.figure(figsize=(15,5))
        plt.ticklabel_format(style='plain')
        plt.plot(result['month and year'], result['{}'.format(foption)], color='#00CEFF', marker='o', linestyle='-')
        date_format = mdates.DateFormatter('%m-%Y')
        plt.gca().xaxis.set_major_formatter(date_format)
        plt.title('{}'.format(title), color='#FFFFFF', fontweight='bold', fontsize=16)
        plt.xlabel('Month and Year', color='#00CEFF')
        plt.ylabel('{}'.format(foption), color='#00CEFF')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        st.pyplot()

with tab3:
    st.markdown('#### Report PDF Upload')
    pdfs = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True, help="Select one or more reports in the standard pdf format to update the existing data...")
    submit = st.button("Update data")
    oldreports = [file for file in os.listdir('reports') if file.endswith('.pdf')]
    if submit:
        if len(pdfs) != 0:
            with st.spinner(text='Extracting data...'):
                for pdf in pdfs:
                    if pdf.name in oldreports:
                        st.write('You have already uploaded the report - {}'.format(pdf.name))
                        continue
                    else:
                        bar = st.progress(0)
                        p = 0
                        pdf_bytes = pdf.read()
                        pdf_path = "reports/{}".format(pdf.name)
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
with tab4:
    pdf_files = [file for file in os.listdir('reports') if file.endswith('.pdf')]
    if pdf_files:
        st.markdown("#### Download available Report PDFs")
        for pdf_file in pdf_files:
            download_path = os.path.join('reports', pdf_file)
            st.download_button(
                label="{}".format(pdf_file),
                data=open(download_path, "rb").read(),
                file_name=pdf_file,
                mime="application/pdf"
            )

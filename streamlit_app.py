import streamlit as st
import pandas as pd
import schemetypedata as stdata
import dataextraction as dataex
st.write("RAGathon Challenge: Mutual Fund Performance Insights Application")
df = pd.read_csv('mutualfunds.csv')
monthselected = st.multiselect('Select the month', df['month and year'].unique())
typeselected = st.multiselect('Select the scheme type', stdata.types)
subtypeselected = st.multiselect('Select the scheme subtype', stdata.subtypes)
namesselected = st.multiselect('Select the scheme name', stdata.names)
result = st.button('get result')
if result:
    res = df[
        (df['month and year'].isin(monthselected)) &
        ((df['Scheme Type'].isin(typeselected)) |
         (df['Scheme Subtype'].isin(subtypeselected)) |
         (df['Scheme Name'].isin(namesselected)))
    ]
    res.columns = dataex.column_headers
    st.write(res)


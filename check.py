import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Индекс Джини")
@st.cache
def get_data():
    data_url = 'https://github.com/Maxim1le/erdata/raw/main/data.csv'
    return pd.read_csv(data_url)
df = get_data()
df.columns = df.columns.str.replace('Value', 'Gini Index')
country = st.selectbox('Country',
                       df['Country Name'].value_counts().index)
df_selection=df[lambda x: x['Country Name'] == country]
df_selection
fig, ax = plt.subplots()
sns.lineplot(x= 'Year', y = 'Gini Index', data = df_selection)
st.pyplot(fig)
st.title("Бюджет РФ")
@st.cache
def get_data1():
    data_url1 = 'https://github.com/Maxim1le/erdata/raw/main/data-20220211-structure-20220211.csv'
    return pd.read_csv(data_url1)
df1 = get_data1()
df1
Year = st.selectbox('Период',
                       df1['Период'].value_counts().index)
df_selection1=df1[lambda x: x['Период'] == Year]
df_selection1

a = alt.Chart(df1).mark_line().encode(
    x='Период', y='Нефтегазовые доходы')

b = alt.Chart(df1).mark_line().encode(
    x='Период', y='Ненефтегазовые доходы')
c = alt.layer(a, b)
st.altair_chart(c, use_container_width=True)

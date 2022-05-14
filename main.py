import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import folium
from streamlit_folium import st_folium
import json

df_1 = pd.read_csv("Height.csv")
df_1
df_2 = pd.read_csv("500.csv")
df_2
df_3 = pd.read_csv("mass.csv")
df_3

fig, ax = plt.subplots(figsize=(30,40), dpi= 80)
sns.stripplot(df_2.Height, df_2.Weight, jitter=0.25, size=8, ax=ax, linewidth=.7, orient='h')
plt.title('Height and weight of people from a sample size of 500 people', fontsize=30)
st.pyplot(fig)

fig = plt.figure(figsize=(13,10), dpi= 80)
sns.boxplot(x='Gender', y='Height', data=df_2, notch=False)
plt.title('Height', fontsize=30)
st.pyplot(fig)

fig = plt.figure(figsize=(13,10), dpi= 80)
sns.boxplot(x='Gender', y='Weight', data=df_2, notch=False)
plt.title('Weight', fontsize=30)
st.pyplot(fig)

fig = plt.figure(figsize=(13,10), dpi= 80)
sns.boxplot(x='Gender', y='Index', data=df_2, notch=False)
plt.title('Mass index', fontsize=30)
st.pyplot(fig)

df_counts = df_2.groupby(['Index']).size().reset_index(name='counts')

categories = df_counts.shape[0]
colors = [plt.cm.inferno_r(i/float(categories)) for i in range(categories)]
fig = plt.figure(
    FigureClass = Waffle,
    plots = {
        111: {
            'values': df_counts['counts'],
            'labels': ["{0}".format(n[0], n[1]) for n in df_counts[['Index', 'counts']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1.2), 'fontsize': 22},
            'title': {'label': 'Distribution of body mass index', 'loc': 'center', 'fontsize':30}
        },
    },
    rows = 10,
    colors = colors,
    figsize = (20, 15)
)
st.pyplot(fig)

country = st.selectbox(
        "Country Name", df_1["Country Name"].value_counts().index)
df_selection = df_1[lambda x: x["Country Name"] == country]
df_selection
df_sel = df_3[lambda y: y["Country"] == country]
df_sel

the_most = st.selectbox(
    'Choose what you want',
    ('the highest','the lowest'))
gen = st.selectbox(
    '',
    ('men','women'))

if(the_most == 'the highest' and gen == 'men'):
    df_11 = df_1.sort_values(by =['Male Height in Cm'])[:10]
    fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
    ax.vlines(x=df_11['Country Name'], ymin = 150, ymax=170, color='blue', alpha=0.7, linewidth=2)
    ax.scatter(x=df_11['Country Name'], y=df_11['Male Height in Cm'], s=75, color='blue', alpha=0.7)
    st.pyplot(fig)
 
    



world_map = folium.Map()
w = st_folium(world_map, width=725)
point = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8, tiles = "Mapbox bright")


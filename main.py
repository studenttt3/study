import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
from pywaffle import Waffle

df_1 = pd.read_csv("Height.csv")
df_1
df_2 = pd.read_csv("500.csv")
df_2
df_3 = pd.read_csv("mass.csv")
df_3

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

fig, ax = plt.subplots(figsize=(30,10), dpi= 80)
sns.stripplot(df_2.Height, df_2.Weight, jitter=0.25, size=8, ax=ax, linewidth=.5)
st.pyplot(fig)

df_counts = df_2.groupby(['Index']).size().reset_index(name='counts')

fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
ax.vlines(x=df_counts.Index, ymin=0, ymax=df_counts.counts, color='blue', alpha=0.7, linewidth=2)
ax.scatter(x=df_counts.Index, y=df_counts.counts, s=75, color='blue', alpha=0.7)
st.pyplot(fig)

categories = df_counts.shape[0]
colors = [plt.cm.inferno_r(i/float(categories)) for i in range(categories)]

fig = plt.figure(
    FigureClass = Waffle,
    plots = {
        111: {
            'values': df_counts['counts'],
            'labels': ["{0}".format(n[0], n[1]) for n in df_counts[['Index', 'counts']].itertuples()],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.1, 1.2), 'fontsize': 22},
            'title': {'label': 'Body mass index', 'loc': 'center', 'fontsize':30}
        },
    },
    rows = 10,
    colors = colors,
    figsize = (20, 15)
)
st.pyplot(fig)

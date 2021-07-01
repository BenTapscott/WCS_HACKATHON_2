import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import plotly.graph_objects as go

st.title('Welcome to the Fiverr Seller Advisor Prototype Number 1 - hello Wilders!!!!')

st.sidebar.header('User Input Parameters')

link = "https://raw.githubusercontent.com/BenTapscott/WCS_HACKATHON_2/main/df_nlp.csv"

df_nlp = pd.read_csv(link)

seller_level = st.sidebar.selectbox('Choose seller level',
    ('Top Rated Seller', 'Level 1 Seller','Level 2 Seller'))

search_term = st.sidebar.text_input('Search for key words', 'website design')

st.write('Current search term is :', search_term)

st.subheader('Data with filters applied : ')

df_nlp.loc[(df_nlp['seller_level']==seller_level) & (df_nlp['tf_idf'].str.contains(search_term))]

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(18,14))
ax.hist(df_nlp['len_description_content'].loc[(df_nlp['seller_level']==seller_level) & (df_nlp['tf_idf'].str.contains(search_term))]);
ax.plot( linewidth=1);
ax.set_title('length of gig description');
ax.set_xlabel('Number of characters')
ax.set_ylabel('Number of gigs');
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(18,14))
sns.set_theme(style="darkgrid")
plt.title ("COUNTRIES")
plt.xticks(rotation=45)
ax = sns.countplot(x="user_country", data=df_nlp.loc[(df_nlp['seller_level']==seller_level) & (df_nlp['tf_idf'].str.contains(search_term))])
st.pyplot(fig)

#df_nlp


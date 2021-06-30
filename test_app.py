import streamlit as st

import pandas as pd


st.title('Welcome to the Fiverr Seller Advisor')

st.sidebar.header('User Input Parameters')

link = "https://raw.githubusercontent.com/BenTapscott/WCS_HACKATHON_2/main/df_nlp.csv"

df_nlp = pd.read_csv(link)

seller_level = st.sidebar.selectbox('Choose seller level',
    ('Top Rated Seller', 'Level 1 Seller','Level 2 Seller'))

st.write('Current search term is :', search_term)

st.subheader('Data with filters applied : ')

search_term = st.sidebar.text_input('Search for key words', 'website design')

df_nlp.loc[(df_nlp['seller_level']==seller_level) & (df_nlp['tf_idf'].str.contains(search_term))]

#df_nlp


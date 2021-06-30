import streamlit as st

import pandas as pd


st.title('Welcome to our app')


st.write("Select the gig")

st.sidebar.header('User Input Parameters')

link = "https://raw.githubusercontent.com/BenTapscott/WCS_HACKATHON_2/main/df_nlp.csv"

df_nlp = pd.read_csv(link)

seller_level = st.sidebar.selectbox('Choose seller level',
    'Top Rated Seller', 'Level 1 Seller','Level 2 Seller')

st.subheader('Show DF filtered')

df_nlp.loc[(df_nlp['seller_level']=seller_level)]


#df_nlp
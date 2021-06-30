import streamlit as st

import pandas as pd


st.title('Welcome to our app')


st.write("Select the gig")

st.sidebar.header('User Input Parameters')

link = "https://raw.githubusercontent.com/BenTapscott/WCS_HACKATHON_2/main/df_nlp.csv"

df_nlp = pd.read_csv(link)

def user_input_features():
    seller_level = st.selectbox('Choose seller level',
        ('Top Rated Seller', 'Level 1 Seller','Level 2 Seller'))
    
    features = pd.DataFrame(df_nlp['seller_level'] == seller_level)
    return features

df = user_input_features()

st.subheader('Show DF filtered')
st.write(df)

#df_nlp
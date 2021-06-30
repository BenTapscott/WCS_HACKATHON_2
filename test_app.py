import streamlit as st

import pandas as pd


st.title('Welcome to our app')


st.write("Select the gig")

st.sidebar.header('User Input Parameters')

link = "https://raw.githubusercontent.com/BenTapscott/WCS_HACKATHON_2/main/df_nlp.csv"

df_nlp = pd.read_csv(link)

seller_level = st.selectbox('Choose seller level',
        ('Top Rated Seller', 'Level 1 Seller','Level 2 Seller'))

st.write('You selected:', seller_level)

"""
def user_input_features():
    seller_level = st.selectbox('Choose seller level',
        ('Top Rated Seller', 'Level 1 Seller','Level 2 Seller'))

    data = {'Top Rated Seller': 'Top Rated Seller',
            'Level 1 Seller': 'Level 1 Seller',
             'Level 2 Seller' : 'Level 2 Seller'   
              features = pd.DataFrame(data, index=[0])
    return features
"""

# Here we use "magic commands":

#df_nlp
import streamlit as st

import pandas as pd


st.title('Welcome to our app')


st.write("Select the gig")


link = "https://raw.githubusercontent.com/BenTapscott/WCS_HACKATHON_2/main/df_nlp.csv"

df_nlp = pd.read_csv(link)


# Here we use "magic commands":

df_nlp
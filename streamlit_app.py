from numpy.core.fromnumeric import argsort
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from gsheetsdb import connect

st.set_page_config(
     page_title="MP Eco Score",
     page_icon="🌱",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'About': "This app gives a visualisation of MP eco scores accross the UK!"
     }
 )

st.title('MP Eco Score')

conn = connect()

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = "https://docs.google.com/spreadsheets/d/1l_FJSRDGlvzm3edj8TSKuGcxjvj4-CA3KODg-vkNIrc/edit#gid=0"

rows = run_query(f'SELECT * FROM "{sheet_url}"')

df = pd.DataFrame(rows)

def onSelect(*options):
    for x in options:
        st.write("You have selected:" + x)


options = st.multiselect("Select consituencies",df,on_change=onSelect())


"""
for row in rows:
    st.write(f"{row.Constituency} has an eco score of {row.Total_Score}")
"""
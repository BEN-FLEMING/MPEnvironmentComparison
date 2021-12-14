from numpy.core.fromnumeric import argsort
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
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

#columns=['Constituency','MP_Name','Supports_the_CEE_Bill?','Attended_Climate_Change_Debate?','Signed_Net_Zero_Letter?','Transport Emissions Target','Voted_for_2015_Fracking_Moratorium','2008_Climate_Change_Act','Prevent_Onshore Wind_Subsidy_Abolition','Supports_Divest_Parliament','GIB Climate_Target','Energy Decarbonisation_Target_2013','Energy_Decarbonisation_Target_2016','Total','Total_Possible_Votes','Total_Score']

df.set_index("Constituency")

plot = alt.Chart(df).mark_bar().encode(
        x='Constituency',
        y='Total_Score',
    )

st.write(plot)

options = []

def onSelect():
    for x in options:
        st.write("You have selected:" + x)

    result = df.loc[options]
    
    
    plot1 = alt.Chart(result).mark_bar().encode(
        x='Constituency',
        y='Total_Score',
    )
    
    st.write(plot1)


options = st.multiselect("Select consituencies",df,on_change=onSelect)


"""
for row in rows:
    st.write(f"{row.Constituency} has an eco score of {row.Total_Score}")
"""
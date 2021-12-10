import pandas as pd
import streamlit as st
from gsheetsdb import connect

st.title('MP Eco Score')

conn = connection()

@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["public_gsheets_url"]

rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.Constituency} has a :{row.Total}:")

import streamlit as st
import pandas as pd

st.title("Hospital Dashboard - Incoming Incidents")

try:
    df = pd.read_csv('incoming_incidents.csv', names=['reporter','lat','lon','severity'])
    st.table(df.tail(10))
except FileNotFoundError:
    st.info("No incidents yet. Submit one via the /report API.")

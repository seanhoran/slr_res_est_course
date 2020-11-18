import streamlit as st

radio_options = ["01 About the Course"]
st.sidebar.radio("Pick Exercise", options=radio_options, index=0, key=None)

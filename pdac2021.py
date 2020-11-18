import streamlit as st

radio_options = ["01 About the Course", 
                 "02 Database", 
                 "03 Capping", 
                 "04 Compositing", 
                 "05 Variograms", 
                 "06 Interpolation", 
                 "07 Classification"]

exercise=st.sidebar.radio("Pick Exercise", 
                          options=radio_options, 
                          index=0, 
                          key=None)

if exercise == radio_options[0]:
  st.title("Fundamentals of Resource Estimation")


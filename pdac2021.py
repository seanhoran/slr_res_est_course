import streamlit as st
import exercises.about_course as about_course
import exercises.db_ex as db_ex
import exercises.capping_ex as capping_ex
from folium.plugins import Fullscreen
Fullscreen().add_to(map)

radio_options = ["01 About the Course", 
                 "02 Database", 
                 "03 Capping", 
                 "04 Compositing", 
                 "05 Variograms", 
                 "06 Interpolation", 
                 "07 Classification"]

exercise=st.sidebar.radio("", 
                          options=radio_options, 
                          index=0, 
                          key=None)

if exercise == radio_options[0]:
  about_course.about_course()
if exercise == radio_options[1]:
  db_ex.db_ex()
if exercise == radio_options[2]:
  capping_ex.capping_ex()


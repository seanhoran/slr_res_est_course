import streamlit as st
import exercises.about_course as about_course
import exercises.db_ex as db_ex
import exercises.capping_ex as capping_ex

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
  st.image("055CF2A4-98DC-488C-B5A6-15CC02C9974E.png", width=100)
  st.title("Fundamentals of Resource Estimation")
  about_course.about_course()
  st.write("")
  st.markdown("## Presenters")
  st.markdown("**Sean Horan**  <shoran@slrconsulting.com>")
  st.image("49640CBC-E71B-4565-9307-0558A8B916B4.jpeg", width=200)
  st.write("Can put bios here")
if exercise == radio_options[1]:
  db_ex.db_ex()
if exercise == radio_options[2]:
  capping_ex.capping_ex()


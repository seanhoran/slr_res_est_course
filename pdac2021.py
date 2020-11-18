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
  about_course_text = "This course introduces the fundamentals of estimating mineral resources and is intended for exploration and mine geologists. These workers are primarily responsible for the discovery, definition, and production of mineral discoveries— yet they are often sidelined when it comes to estimating resources. This course is intended to fill that knowledge gap to produce more informed geologists, which will lead to better resource estimates and drill hole targeting."
  about_course_text += "The course will start where many geologists stop, at the resource database and will proceed to domaining, block modeling, etc. Although most geologists do an excellent job interpreting the genesis and geometry of a mineral deposit, some aspects of their interpretation lack consideration necessary for a mineral resource model, including practical aspects such as proposed mining method and equipment, or geostatistical aspects such as the selection of appropriate domain criterion. RPA will explain the fundamentals and importance of each step, including common risks and mistakes."
  st.write(about_course_text)
  st.write("")
  st.markdown("## Presenters")
  st.markdown("**Sean Horan**")
  st.image("49640CBC-E71B-4565-9307-0558A8B916B4.jpeg", width=200)
  st.write("Can put bios here")


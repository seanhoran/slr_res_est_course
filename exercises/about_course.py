import streamlit as st
import itertools
import os



def about_course():
  
  st.image("..//pdac2021_res_est_course//055CF2A4-98DC-488C-B5A6-15CC02C9974E.png", width=100)
  
  st.title("Fundametals of Resource Estimation")
  path = "..//pdac2021_res_est_course//text_blocks"
  f = open(path + "//about_course.txt", "r")
  st.write(f.read())
  
  st.write("")
  st.markdown("# Presenters")
  st.write("")
  st.image("..//pdac2021_res_est_course//49640CBC-E71B-4565-9307-0558A8B916B4.jpeg", width=200)
  st.markdown("**Sean Horan P.Geo - Technical Manager Geology**")
  st.markdown("<shoran@slrconsulting.com>")
  st.write("Can put bios here")

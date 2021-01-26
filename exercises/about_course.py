import streamlit as st
import itertools
import os

def about_course():
  
  st.image("..//pdac2021_res_est_course//055CF2A4-98DC-488C-B5A6-15CC02C9974E.png", width=100)
  st.title("Fundametals of Resource Estimation")
  
  # this is how to read a block of text:
  path = "..//pdac2021_res_est_course//text_blocks"
  f = open(path + "//about_course.txt", "r")
  # and then write it to the app
  st.write(f.read())
  
  st.write("")
  st.markdown("# Presenters")
  st.write("")
  st.image("..//pdac2021_res_est_course//headshots//Sean_Horan.jpeg", width=200)
  st.markdown("**Sean Horan P.Geo - Technical Manager Geology**")
  st.markdown("<shoran@slrconsulting.com>")
  st.write("Can put bios here")

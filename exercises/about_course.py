import streamlit as st
import itertools
import os

def about_course():
  
  st.image("..//pdac2021_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  st.title("Fundamentals of Resource Estimation")
  
  # this is how to read a block of text:
  path = "..//pdac2021_res_est_course//text_blocks"
  f = open(path + "//about_course.txt", "r")
  # and then write it to the app
  st.write(f.read())
  
  st.write("")
  st.image("..//pdac2021_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  st.markdown("# Presenters")
  presenter = st.selectbox("", options=['Sean Horan', 'Valerie Wilson', 'Pierre Landry', 'Ian Weir'])
  split_name = presenter.split(" ")
  lcase_name = (split_name[0] + "_" + split_name[1]).lower()
  ucase_name = (split_name[0] + "_" + split_name[1])
  
  col1, col2 = st.beta_columns([1,2.5])
  with col1:
    st.image("..//pdac2021_res_est_course//headshots//" + ucase_name + ".jpeg", use_column_width=True)
    st.markdown("**Sean Horan P.Geo - Technical Manager Geology**")
    st.markdown("<shoran@slrconsulting.com>")
  with col2:
    path = "..//pdac2021_res_est_course//text_blocks"
    f = open(path + "//resume_" + lcase_name + ".txt", "r")
    st.write(f.read())
 

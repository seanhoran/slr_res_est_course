import streamlit as t

def about_course():
  f = open("..//text_blocks//about_course.txt", "r")
  st.write(f.read())

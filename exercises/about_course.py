import streamlit as st
import os

path = os.getcwd().split("//")[:-1].flatten() + "//text_blocks"

def about_course():
  f = open(path + "//about_course.txt", "r")
  st.write(f.read())

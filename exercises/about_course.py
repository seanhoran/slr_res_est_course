import streamlit as st
import itertools
import os

path = "..//pdac2021_res_est_course//text_blocks"

def about_course():
  f = open(path + "//about_course.txt", "r")
  st.write(f.read())

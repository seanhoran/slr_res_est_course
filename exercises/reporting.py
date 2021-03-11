import streamlit as st
import funcs
import pandas as pd

def reporting():
  st.title("Reporting/Classification Exercise")
  text = funcs.get_text_block("reporting.txt")
  st.markdown(text)
  st.image("..//pdac2021_res_est_course//images//res_table.jpg", use_column_width=True)
  
  st.markdown("## Answers")
  st.write(pd.DataFrame({
    'Error Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'second column': ["MII tallied in final row.", "No information as to whether Mineral Resources and Inclusive or Exclusive.", 30, 40,50,60,70,80,90,100,110,120],}))

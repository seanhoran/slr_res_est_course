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
    'Error': ["MII tallied in final row.", "No information as to whether Mineral Resources and Inclusive or Exclusive.", "Missing information as to which cut-off grade is relevant for each ore type.", "Missing zinc metal prices.", "Missing key assumption as to whether the deposit is envisaged to be mined using underground or open pit mining.", "Missing the statement reiterating that Mineral Resources that are not Mineral Reserves do not have demonstrated economic viability.", "Too many significant figures for contained zinc.", "Too many significant figures for silver grade.", "No unit for the material quantity (Million Tonnes).", "No details on metallurgical assumptions used to generate the cut-off value.", "No information as to how the reasonable prospects for eventual economic extraction were determined.", "Missing Statement discussing issues relating to all relevant technical and economic factors likely to influence the prospect of economic extraction, and whether they can be resolved with further work."],}))

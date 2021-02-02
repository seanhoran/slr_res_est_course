import streamlit as st
import funcs
import pandas as pd

def cut_off():
  
  df = pd.read_csv("..//pdac2021_res_est_course//data//Worksheet COGs.csv")
  df = df.fillna("")
  df = df.drop(df.columns[-1],axis=1).copy()
  df = df.drop(df.columns[-1],axis=1).copy()
  df = df[:32].copy()

  st.title("Cut-off Grade Exercise")
  st.write("")
  st.markdown("## Question 1: Do we send this block to the processing plant?")
  st.write("")
  
  col1, col2 = st.beta_columns([1, 2])
  
  with col1:
    st.image("..//pdac2021_res_est_course//images//cog1_block.jpg", width=300)
  with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown('### Operating costs:')
    st.markdown('* Mining: $50/t')
    st.markdown('* Process: $20/t')
    st.markdown('* G&A: $15/t')
  
  q1_options = ['yes', 'no']
  cog_q1_answer = st.radio("Do we send this block to the processing plant?", options=q1_options, key='cog_q1')
  
  st.write("")
  st.markdown("## Question 2: Complex Cut-off Calculation")
  st.write("")
  col3, col4 = st.beta_columns([1, 2])
  with col3:
    text = funcs.get_text_block("cog_q2_intro.txt")
    st.markdown(text)
  with col4:
    st.table(df)
  q2_options = ['I have no idea', 
                'The block is below all cut-off grades', 
                'The block is greater than the marginal but less than the break-even cut-off', 
                'The block exceeds all cut-off grades']
  cog_q2_answer = st.radio("Select the appropriate statement?", options=q2_options, key='cog_q2')

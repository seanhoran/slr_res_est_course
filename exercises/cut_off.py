import streamlit as st
import funcs

def cut_off():
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
  text = funcs.get_text_block("cog_q2_intro.txt")
  st.markdown(text)
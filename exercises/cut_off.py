import streamlit as st


def cut_off():
  st.title("Cut-off Grade Exercise")
  st.write("")
  st.markdown("## Question 1: Do we send this block to the processing plant?")
  st.write("")
  
  col1, col2 = st.beta_columns([1, 2])
  
  with col1:
    st.write("")
    st.write("")
    st.image("..//pdac2021_res_est_course//images//cog1_block.jpg", width=500)
  with col2:
    st.markdown('### Operating costs:')
    st.markdown('* Mining: $50/t')
    st.markdown('* Process: $20/t')
    st.markdown('* G&A: $15/t')
  
  q1_options = ['yes', 'no']
  cog_q1_answer = st.radio("Select the correct answer:", options=options, key='cog_q1')           

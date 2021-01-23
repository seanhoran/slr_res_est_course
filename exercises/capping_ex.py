import streamlit as st

def capping_ex():
  st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            }
        </style>
        """,
    unsafe_allow_html=True)
  
  st.title("Capping Exercise")
  options = ['None', 'Answer 1', 'right answer']
  answer=st.radio('what is the answer', options=options, index=0, key='quest')
  
  if answer=='right answer':
    st.write('correct')
  else:
    st.write('wrong')
    
  answer=st.radio('what is the answer', options=options, index=0, key='quest')
  
  if answer=='right answer':
    st.write('correct')
  else:
    st.write('wrong')
    
    

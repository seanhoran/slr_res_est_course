import streamlit as st

def capping_ex():
 
  st.title("Capping Exercise")
  
  count_correct = 0
  
  q1_options = ['Please Select an Answer', 
             'Answer 1', 
             'right answer']
  
  q1_answer=st.radio('what is the answer', options=options, index=0, key='quest')
  
  if q1_answer=='right answer':
   count_correct +=1
    
  q2_options = ['Please Select an Answer', 
             'Answer 1', 
             'right answer']
    
  q2_answer=st.radio('what is the answer', options=options, index=0, key='quest2')
  
  if q2_answer=='right answer':
   count_correct +=1
    
  st.write("Number correct = " + str(count_correct) + " out of 2")
    
    

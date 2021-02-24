import streamlit as st

def capping_ex():
 
  st.title("Capping Exercise")
  
  count_correct = 0
  
  st.write("Write some stuff2")
  
  st.image("..//pdac2021_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  
  q1_options = ['Please Select an Answer', 
             'Answer 1', 
             'right answer', 
                'Answer 3']
  
  q1_answer=st.radio('This is the question', options=q1_options, index=0, key='quest1')
  
  if q1_answer=='right answer':
   count_correct +=1
    
  q2_options = ['Please Select an Answer', 
             'Answer 1', 
             'right answer']
    
  q2_answer=st.radio('what is the answer', options=q2_options, index=0, key='quest2')
  
  if q2_answer=='right answer':
   count_correct +=1
    
  st.write("Number correct = " + str(count_correct) + " out of 2")
    
    

import streamlit as st

def capping_ex():
 
  st.title("Capping Exercise")
  
  count_correct = 0
  
  st.write("The grade restriction module introduced some of the tools that can help you identify whether high grade restraining is required. This exercise uses real data and shows how the high grade restraining workflow is iterative, and that your decision to domain, cap, or otherwise restrict outlier samples should be informed by a group of tools. Lastly, it is important to note that you may elect to revisit your high grade restraining workflow after validating your estimate visually and statistically since the impact of high grade samples on the final resource estimate can be significant.")
  st.write("another change")
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
    
  st.write("Number correct = " + str(count_correct) + " out of 21")
    
    

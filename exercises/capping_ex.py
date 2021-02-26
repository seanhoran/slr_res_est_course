import streamlit as st

def capping_ex():
 
  st.title("Capping Exercise")
  
  count_correct = 0
  
  st.write("The grade restriction module introduced some of the tools that can help you identify whether high grade restraining is required. This exercise uses real data and shows how the high grade restraining workflow is iterative, and that your decision to domain, cap, or otherwise restrict outlier samples should be informed by a group of tools. Lastly, it is important to note that you may elect to revisit your high grade restraining workflow after validating your estimate visually and statistically since the impact of high grade samples on the final resource estimate can be significant.")

  st.image("..//pdac2021_res_est_course//images//wireframe_header.jpg", use_column_width=True)

  st.header("Exercise 1 - Gold Deposit - Question 1")
   
  q1_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  q1_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate.', options=q1_options, index=0, key='quest1')
  st.image("..//pdac2021_res_est_course//images//HG_LG_Decile.jpg", use_column_width=True)
  st.image("..//pdac2021_res_est_course//images//HG_LG_HISTO.jpg", use_column_width=True)
  st.image("..//pdac2021_res_est_course//images//HG_LG_PP.jpg", use_column_width=True)
  st.image("..//pdac2021_res_est_course//images//HG_LG_PlanCaps.jpg", use_column_width=True)
  st.image("..//pdac2021_res_est_course//images//HG_LG_ObliqueCaps.jpg", use_column_width=True)
  
  if q1_answer=='10 g/t Au':
   count_correct +=0.5
  if q1_answer=='20 g/t Au':
   count_correct +=2
  if q1_answer=='25 g/t Au':
   count_correct +=1
  if q1_answer=='Something is wrong':
   count_correct +=3


  st.header("Exercise 1 - Gold Deposit - Question 2")
   
  q2_options = ['Please Select an Answer', 
             '5 g/t Au', 
             '10 g/t Au', 
             '15 g/t Au',
               'Other',
               'Something is wrong']
  
  q2_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate.', options=q2_options, index=0, key='quest1')
  st.image("..//pdac2021_res_est_course//images//LG_Decile.jpg", use_column_width=True)
  st.image("..//pdac2021_res_est_course//images//LG_HISTO.jpg", use_column_width=True)
  st.image("..//pdac2021_res_est_course//images//LG_PP.jpg", use_column_width=True)
  
  if q2_answer=='5 g/t Au':
   count_correct +=1

   
    
  st.write("Number correct = " + str(count_correct) + " out of 21")
    
    

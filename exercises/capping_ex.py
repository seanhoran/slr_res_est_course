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
  st.subheader("Decile Analysis")
  st.image("..//pdac2021_res_est_course//images//HG_LG_Decile.jpg", use_column_width=True)
  st.subheader("Histogram")
  st.image("..//pdac2021_res_est_course//images//HG_LG_HISTO.jpg", use_column_width=True)
  st.subheader("Probability Plot")
  st.image("..//pdac2021_res_est_course//images//HG_LG_PP.jpg", use_column_width=True)
  st.subheader("Plan View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG_LG_PlanCaps.jpg", use_column_width=True)
  st.subheader("Oblique View - Looking Along Strike")
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
  
  q2_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate.', options=q2_options, index=0, key='quest2')
  st.subheader("Decile Analysis")
  st.image("..//pdac2021_res_est_course//images//LG_Decile.jpg", use_column_width=True)
  st.subheader("Histogram")
  st.image("..//pdac2021_res_est_course//images//LG_HISTO.jpg", use_column_width=True)
  st.subheader("Probability Plot")
  st.image("..//pdac2021_res_est_course//images//LG_PP.jpg", use_column_width=True)
  st.subheader("Plan View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//LG_PlanCaps.jpg", use_column_width=True)
  st.subheader("Oblique View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//LG_ObliqueCaps.jpg", use_column_width=True)
  
  if q2_answer=='5 g/t Au':
   count_correct +=3
  if q2_answer=='10 g/t Au':
   count_correct +=2
  if q2_answer=='15 g/t Au':
   count_correct +=0.5


  st.header("Exercise 1 - Gold Deposit - Question 3")
   
  q3_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  q3_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate.', options=q3_options, index=0, key='quest3')
  st.subheader("Decile Analysis")
  st.image("..//pdac2021_res_est_course//images//HG_Decile.jpg", use_column_width=True)
  st.subheader("Histogram")
  st.image("..//pdac2021_res_est_course//images//HG_HISTO.jpg", use_column_width=True)
  st.subheader("Probability Plot")
  st.image("..//pdac2021_res_est_course//images//HG_PP.jpg", use_column_width=True)
  st.subheader("Plan View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG_PlanCaps.jpg", use_column_width=True)
  st.subheader("Oblique View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG_ObliqueCaps.jpg", use_column_width=True)
  
  
  if q3_answer=='10 g/t Au':
   count_correct +=0.5
  if q3_answer=='20 g/t Au':
   count_correct +=2
  if q3_answer=='25 g/t Au':
   count_correct +=1
  if q3_answer=='Something is wrong':
   count_correct +=3



  st.header("Exercise 1 - Gold Deposit - Question 4")
   
  q4_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '15 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  q4_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate.', options=q4_options, index=0, key='quest4')
  st.subheader("Decile Analysis")
  st.image("..//pdac2021_res_est_course//images//HG_2_7_Decile.jpg", use_column_width=True)
  st.subheader("Histogram")
  st.image("..//pdac2021_res_est_course//images//HG_2_7_HISTO.jpg", use_column_width=True)
  st.subheader("Probability Plot")
  st.image("..//pdac2021_res_est_course//images//HG_2_7_PP.jpg", use_column_width=True)
  st.subheader("Plan View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG_2_7_PlanCaps.jpg", use_column_width=True)
  st.subheader("Oblique View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG_2_7_ObliqueCaps.jpg", use_column_width=True)
  
  
  if q4_answer=='10 g/t Au':
   count_correct +=3
  if q4_answer=='15 g/t Au':
   count_correct +=1


  st.header("Exercise 1 - Gold Deposit - Question 5")
   
  q5_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  q5_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate.', options=q5_options, index=0, key='quest5')
  st.subheader("Decile Analysis")
  st.image("..//pdac2021_res_est_course//images//HG1_Decile.jpg", use_column_width=True)
  st.subheader("Histogram")
  st.image("..//pdac2021_res_est_course//images//HG1_HISTO.jpg", use_column_width=True)
  st.subheader("Probability Plot")
  st.image("..//pdac2021_res_est_course//images//HG1_PP.jpg", use_column_width=True)
  st.subheader("Plan View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG1_PlanCaps.jpg", use_column_width=True)
  st.subheader("Oblique View - Looking Along Strike")
  st.image("..//pdac2021_res_est_course//images//HG1_ObliqueCaps.jpg", use_column_width=True)
  
  
  if q5_answer=='10 g/t Au':
   count_correct +=1
  if q5_answer=='20 g/t Au':
   count_correct +=3
  if q5_answer=='25 g/t Au':
   count_correct +=1

  
  
    
  st.write("Number correct = " + str(count_correct) + " out of 15")
    

  st.image("..//pdac2021_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  
  st.write("As you might have gathered from the plan and oblique views, the gold deposit dataset from Question 1 contains a high grade and low grade population, where the high grade veins are contained within a lower grade alteration halo. The second exercise is a continuation from the first and requires you to match the domains shown in the images below with the statistics presented in each of the questions from the first exercise.")
  
  st.write("Note: The images below are an inclined views and are looking down over the along strike oblique views presented in Exercise 1.")

  st.subheader("Domains 1, 2 and 3")
  st.image("..//pdac2021_res_est_course//images//Domains123.jpg", use_column_width=True)
  st.subheader("Domains 1, 2 and 3 with Capped Assays")
  st.image("..//pdac2021_res_est_course//images//Domains123_Caps2.jpg", use_column_width=True)
  st.subheader("Capped Assays")
  st.image("..//pdac2021_res_est_course//images//Domains123_Caps.jpg", use_column_width=True)

  st.header("Exercise 2 - Gold Deposit - Question 1")
   
  q6_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q6_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 1 from Exercise 1?', options=q6_options, index=0, key='quest6')

  
  if q6_answer=='Domains 1, 2, and 3':
   count_correct +=3

   
  st.header("Exercise 2 - Gold Deposit - Question 2")
   
  q7_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q7_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 2 from Exercise 1?', options=q7_options, index=0, key='quest7')

  
  if q7_answer=='Domain 3':
   count_correct +=3
   
   
  st.header("Exercise 2 - Gold Deposit - Question 4")
   
  q9_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q9_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 3 from Exercise 1?', options=q9_options, index=0, key='quest8')

  
  if q9_answer=='Domains 1 and 2':
   count_correct +=3
      
    
  st.header("Exercise 2 - Gold Deposit - Question 4")
   
  q9_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q9_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 4 from Exercise 1?', options=q9_options, index=0, key='quest9')

  
  if q9_answer=='Domain 2':
   count_correct +=3
      
      
    
  st.header("Exercise 2 - Gold Deposit - Question 5")
   
  q10_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q10_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 5 from Exercise 1?', options=q10_options, index=0, key='quest10')

  
  if q10_answer=='Domain 1':
   count_correct +=3
   
  st.write("Number correct = " + str(count_correct) + " out of 30")

import streamlit as st

def capping_ex():
 
  st.title("Capping Exercise")
  
  count_correct = 0
  
  st.write("The grade restriction module introduced some of the tools that can help you identify whether high grade restraining is required. This exercise uses real data and shows how the high grade restraining workflow is iterative, and that your decision to domain, cap, or otherwise restrict outlier samples should be informed by a group of tools. Lastly, it is important to note that you may elect to revisit your high grade restraining workflow after validating your estimate visually and statistically since the impact of high grade samples on the final resource estimate can be significant.")

#   st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)

  st.header("Exercise 1 - Gold Deposit - Question 1")
   
  q1_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  
  q1_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate. Careful review of the Plan and Oblique views should help provide a better sense of the spatial distribution of the pre-selected decile thresholds.', options=q1_options, index=0, key='quest1')
  col1, col2, col3 = st.columns((1,1.5,1))
  with col1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG_LG_Decile.jpg", use_column_width=True)
  with col2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_LG_HISTO.jpg", use_column_width=True)
  with col3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_LG_PP.jpg", use_column_width=True)
  
  cola1, cola2 = st.columns((1,1.6))
  with cola1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG_LG_PlanCaps.jpg", use_column_width=True)
  with cola2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG_LG_ObliqueCaps.jpg", use_column_width=True)
   st.subheader("Oblique View - Looking Along Strike")
  st.write("")
#   st.subheader("Answer: Something is wrong - dataset has a distinct high grade population that should be evaluated independently.")
  st.write("")
  st.write("")
  st.write("")
  
  st.header("Exercise 1 - Gold Deposit - Question 2")
  q2_options = ['Please Select an Answer', 
             '5 g/t Au', 
             '10 g/t Au', 
             '15 g/t Au',
               'Other',
               'Something is wrong']
  
  q2_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate. Careful review of the Plan and Oblique views should help provide a better sense of the spatial distribution of the pre-selected decile thresholds.', options=q2_options, index=0, key='quest2')
  colb1, colb2, colb3 = st.columns((1,1.5,1))
  with colb1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//LG_Decile.jpg", use_column_width=True)
  with colb2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//LG_HISTO.jpg", use_column_width=True)
  with colb3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//LG_PP.jpg", use_column_width=True)
  
  colc1, colc2 = st.columns((1,1.6))
  with colc1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//LG_PlanCaps.jpg", use_column_width=True)
  with colc2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//LG_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
#   st.subheader("Answer: 5 g/t Au or 10 g/t Au practitioner dependant.")
  st.write("")
  st.write("")
  st.write("")
  

  
  st.header("Exercise 1 - Gold Deposit - Question 3")
   
  q3_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  q3_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate. Careful review of the Plan and Oblique views should help provide a better sense of the spatial distribution of the pre-selected decile thresholds.', options=q3_options, index=0, key='quest3')
  cold1, cold2, cold3 = st.beta_columns((1,1.5,1))
  with cold1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG_Decile.jpg", use_column_width=True)
  with cold2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_HISTO.jpg", use_column_width=True)
  with cold3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_PP.jpg", use_column_width=True)
  
  cole1, cole2 = st.beta_columns((1,1.6))
  with cole1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG_PlanCaps.jpg", use_column_width=True)
  with cole2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
  st.subheader("Answer: Something is wrong - The dataset has a distinct higher grade population that should be evaluated independently.")
  st.write("")
  st.write("")
  st.write("")
  

  st.header("Exercise 1 - Gold Deposit - Question 4")
   
  q4_options = ['Please Select an Answer', 
             '5 g/t Au', 
             '10 g/t Au', 
             '15 g/t Au',
               'Other',
               'Something is wrong']
  
  q4_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate. Careful review of the Plan and Oblique views should help provide a better sense of the spatial distribution of the pre-selected decile thresholds.', options=q4_options, index=0, key='quest4')
  colf1, colf2, colf3 = st.beta_columns((1,1.5,1))
  with colf1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG_2_7_Decile.jpg", use_column_width=True)
  with colf2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_2_7_HISTO.jpg", use_column_width=True)
  with colf3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_2_7_PP.jpg", use_column_width=True)
  
  colg1, colg2 = st.columns((1,1.6))
  with colg1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG_2_7_PlanCaps.jpg", use_column_width=True)
  with colg2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG_2_7_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
#   st.subheader("Answer: 10 g/t Au or 15 g/t Au practitioner dependant.")
  st.write("")
  st.write("")
  st.write("")
  


  st.header("Exercise 1 - Gold Deposit - Question 5")
   
  q5_options = ['Please Select an Answer', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Other',
               'Something is wrong']
  
  q5_answer=st.radio('Review the following histogram, probability plot and decile analysis and determine which capping level is most appropriate. Careful review of the Plan and Oblique views should help provide a better sense of the spatial distribution of the pre-selected decile thresholds.', options=q5_options, index=0, key='quest5')
  colh1, colh2, colh3 = st.columns((1,1.5,1))
  with colh1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG1_Decile.jpg", use_column_width=True)
  with colh2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG1_HISTO.jpg", use_column_width=True)
  with colh3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG1_PP.jpg", use_column_width=True)
  
  coli1, coli2 = st.columns((1,1.6))
  with coli1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG1_PlanCaps.jpg", use_column_width=True)
  with coli2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG1_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
  st.subheader("Answer: 25 g/t Au or potentially higher based on a more detailed spatial review.")
  st.write("")
  st.write("")
  st.write("")
  
  

  st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  
  st.write("As you might have gathered from the plan and oblique views, the gold deposit dataset from Question 1 contains a high grade and low grade population, where the high grade veins are contained within a lower grade alteration halo. The second exercise is a continuation from the first and requires you to match the domains shown in the images below with the statistics presented in each of the questions from the first exercise. If you had some incorrect responses in the first exercise, consult the information and images below prior to beginning Exercise 2.")
  
  st.write("Note: The images below are inclined views and are looking down over the along strike oblique views presented in Exercise 1. Wireframes were constructed for Domains 1 and 2 at a nominal cut-off grade of 1 g/t Au while the Domain 3 wireframes were constructed at a nominal 0.20 g/t Au cut-off grade.")

  st.subheader("Domains 1, 2 and 3")
  st.image("..//slr_res_est_course//images//Domains123.jpg", use_column_width=True)
  st.subheader("Domains 1, 2 and 3 with Capped Assays")
  st.image("..//slr_res_est_course//images//Domains123_Caps2.jpg", use_column_width=True)
  st.subheader("Capped Assays")
  st.image("..//slr_res_est_course//images//Domains123_Caps.jpg", use_column_width=True)

  st.header("Exercise 2 - Gold Deposit - Question 1")
   
  q6_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q6_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 1 from Exercise 1?', options=q6_options, index=0, key='quest6')
  st.write("")
#   st.subheader("Answer: Domains 1, 2, and 3")
  st.write("")
  st.write("")
  st.write("")
  

   
  st.header("Exercise 2 - Gold Deposit - Question 2")
   
  q7_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q7_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 2 from Exercise 1?', options=q7_options, index=0, key='quest7')
  st.write("")
  st.subheader("Answer: Domain 3")
  st.write("")
  st.write("")
  st.write("")
  

   
  st.header("Exercise 2 - Gold Deposit - Question 4")
   
  q9_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q9_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 3 from Exercise 1?', options=q9_options, index=0, key='quest8')

  st.write("")
#   st.subheader("Answer: Domains 1 and 2")
  st.write("")
  st.write("")
  st.write("")

  
  st.header("Exercise 2 - Gold Deposit - Question 4")
   
  q9_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q9_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 4 from Exercise 1?', options=q9_options, index=0, key='quest9')

  st.write("")
#   st.subheader("Answer: Domain 2")
  st.write("")
  st.write("")
  st.write("")
 
    
  st.header("Exercise 2 - Gold Deposit - Question 5")
   
  q10_options = ['Please Select an Answer', 
             'Domain 1', 
             'Domain 2', 
             'Domain 3',
             'Domains 1 and 2',
             'Domains 1 and 3',
             'Domains 1, 2, and 3']
  
  q10_answer=st.radio('Which domain(s) best reflect the histogram, probability plot and decile analysis presented in Question 5 from Exercise 1?', options=q10_options, index=0, key='quest10')
  st.write("")
#   st.subheader("Answer: Domain 1")
  st.write("")
  st.write("")
  st.write("")
  


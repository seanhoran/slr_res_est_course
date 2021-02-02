import streamlit as st
import funcs
import pandas as pd
import numpy as np

def adjust_calculation(df2):
  
  colx1, colx2, colx3, colx4 = st.beta_columns((1,1,1,1))
  
  with colx1:
    st.markdown("Production")
    df2.loc[0, 'Resource COG'] = st.slider("Tonnes", 1000000, 10000000, 5000000, 1000000, key="cgsl1")
    df2.loc[1, 'Resource COG'] = st.slider("Cu %", 0., 2.0, 1.0, 0.1, key="cgsl2")
    df2.loc[2, 'Resource COG'] = st.slider("Au g/t", 0., 2.0, 1.0, 0.1, key="cgsl3")
  with colx2:
    st.markdown("Production")
    df2.loc[4, 'Resource COG'] = st.slider("Cu Recovery", 60., 95., 87., 1.0, key="cgsl4")
    df2.loc[5, 'Resource COG'] = st.slider("Au Recover", 60., 95., 87., 1.0, key="cgsl5")
  with colx3:
    st.markdown("Metal Prices")
    df2.loc[16, 'Resource COG'] = st.slider("Cu Price ($/lbs)", 2.5, 4.0, 3.25, 0.1, key="cgsl6")
    df2.loc[17, 'Resource COG'] = float(st.slider("Au Price ($/oz)", 1000.0, 2000.0, 1500.0, 500.0, key="cgsl7"))
  with colx4:
    st.markdown("Other")
    df2.loc[10, 'Resource COG'] = st.slider("Cu Con Grade", 20.0, 35.0, 25.0, 1.0, key="cgsl8")
    df2.loc[13, 'Comments'] = st.slider("Payabe Cu", 85., 100., 90., 1.0, key="cgsl9")
    df2.loc[14, 'Comments'] = st.slider("Payable Au", 85., 100., 99., 1.0, key="cgsl10")
  
  df2.loc[7, 'Resource COG'] = np.round(df2.loc[0, 'Resource COG']*(df2.loc[1, 'Resource COG']/100.)*(df2.loc[4, 'Resource COG']/100.)*2.20462,0)
  df2.loc[8, 'Resource COG'] = np.round(df2.loc[0, 'Resource COG']*(df2.loc[2, 'Resource COG'])*(df2.loc[5, 'Resource COG']/100.)/31.103, 0)
  df2.loc[9, 'Resource COG'] = np.round(df2.loc[7, 'Resource COG']*1000./2204.62/df2.loc[10, 'Resource COG']/100., 0)
  df2.loc[11, 'Resource COG'] = np.round(df2.loc[8, 'Resource COG']*31.1035/df2.loc[9, 'Resource COG'],2)
  
  df2.loc[13, 'Resource COG'] = np.round(df2.loc[7, 'Resource COG']*(df2.loc[13, 'Comments']),0)
  df2.loc[14, 'Resource COG'] = np.round(df2.loc[8, 'Resource COG']*(df2.loc[14, 'Comments']),0)
  
  df2.loc[18, 'Resource COG'] = np.round(df2.loc[13, 'Resource COG']*df2.loc[16, 'Resource COG'], 0)
  st.write(df2.loc[14, 'Resource COG'], df2.loc[17, 'Resource COG'])
  df2.loc[19, 'Resource COG'] = np.round(df2.loc[14, 'Resource COG']*float(df2.loc[17, 'Resource COG']), 0)
    
  df2.loc[20, 'Resource COG'] = df2.loc[18, 'Resource COG']+df2.loc[19, 'Resource COG']
                                         
  df2.loc[22, 'Resource COG'] = np.round(df2.loc[9, 'Resource COG']*9.0, 0)
  df2.loc[23, 'Resource COG'] = np.round(df2.loc[13, 'Resource COG']*0.09,0)
  df2.loc[24, 'Resource COG'] = np.round(df2.loc[14, 'Resource COG']*5.0, 0)
                                         
  df2.loc[25, 'Resource COG'] = np.round(df2.loc[20, 'Resource COG']-df2.loc[22, 'Resource COG']-df2.loc[23, 'Resource COG']-df2.loc[24, 'Resource COG'], 0)
                                         
  df2.loc[27, 'Resource COG'] = np.round((df2.loc[18, 'Resource COG']-df2.loc[22, 'Resource COG']-0.09*df2.loc[13, 'Resource COG']/1000.)/df2.loc[25, 'Resource COG'], 2)
  df2.loc[28, 'Resource COG'] = np.round((df2.loc[19, 'Resource COG']-df2.loc[23, 'Resource COG']-5.0*df2.loc[14, 'Resource COG']/1000.)/df2.loc[25, 'Resource COG'], 2)
                                         
  df2.loc[30, 'Resource COG'] = np.round((df2.loc[27, 'Resource COG']*df2.loc[25, 'Resource COG']*1000./(df2.loc[0, 'Resource COG']*df2.loc[1, 'Resource COG'])),0)
  df2.loc[31, 'Resource COG'] = np.round((df2.loc[28, 'Resource COG']*df2.loc[25, 'Resource COG']*1000./(df2.loc[0, 'Resource COG']*df2.loc[2, 'Resource COG'])),0)
  
  st.table(df2)
  
def cut_off():
  
  df = pd.read_csv("..//pdac2021_res_est_course//data//Worksheet COGs.csv")
  df = df.fillna("")
#   df = df.drop(df.columns[-1],axis=1).copy()
#   df = df.drop(df.columns[-1],axis=1).copy()
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
  q2_options = ['A. I have no idea', 
                'B. The block value is below all cut-off grades', 
                'C. The block value is greater than the marginal but less than the break-even cut-off', 
                'D. The block value exceeds all cut-off grades']
  cog_q2_answer = st.radio("Select the appropriate statement:", options=q2_options, key='cog_q2')
  st.write("")
  st.markdown("## Sensitivities")
  adjust_calculation(df.copy())
  

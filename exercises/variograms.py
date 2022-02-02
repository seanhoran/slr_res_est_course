import numpy as np
import streamlit as st
import funcs
import pandas as pd
import getpass
# import pymysql
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def variogram(nugget=0.0, srange=100., struct_type='Spherical'):
  var = 1.-nugget
  h = np.arange(0,150.,5.)
  gamma = h
  if struct_type == 'Spherical':
    gamma = nugget + var*((3*h)/(2*srange)-(h**3)/(2*srange**3))
    gamma[h>srange]=1.0
    gamma[0] = nugget
  elif struct_type == 'Power':
    gamma = nugget + var*(h/srange)**1.5
  else:
    gamma = var*(1.0-np.cos((h**2/srange**2)*np.pi)*np.exp((-3*h)/(srange*1.2))) + nugget
  return gamma, h; 

def ex_var(example=1, 
           hint='Hint: Contrary to popular flat earther beliefs.', 
           key_nugget='nug1', key_range='range1', key_stype='stype1', 
           im='sim1.jpg'):  
  st.markdown("### Example " + str(example) + ":")
  st.markdown(hint)
  col1, col2 = st.columns([1, 1])
  with col1:
    struct_type = st.selectbox("Structure Type", options=["Spherical", "Power", "Hole Effect"], index=0, key=key_stype)
    nugget = st.slider('Nugget', 0.0, 1.0, 0.1, 0.05, key=key_nugget) 
    srange = st.slider('Range', 0.0, 120., 100., 10., key=key_range)
    gamma, h = variogram(nugget, srange, struct_type)
    fig, ax = plt.subplots()
    plt.plot([0, 120.], [1.0, 1.0], '--k')
    plt.plot(h, gamma, '-r')
    plt.xlabel('Range (m)')
    plt.ylabel('Gamma')
    plt.xlim((0.,120.))
    plt.ylim((0.,1.5))
    st.pyplot(fig)  
  with col2:
    st.write("")
    st.write("")
    st.write("")
    st.image("..//slr_res_est_course//images//" + im)
    
  return struct_type, nugget, srange
  
def variograms():
  st.title("Variogram Exercise")
  st.write("")
  st.markdown("## Model the appropriate variogram for each grade pattern observed")
  text = funcs.get_text_block("variography_intro.txt")
  st.markdown(text)
  
  results = []
  
  s,n,r = ex_var(example=1, 
           hint='Hint: Contrary to popular flat earther beliefs.', 
           key_nugget='nug1', key_range='range1', key_stype='stype1', 
           im='sim1.jpg')
#   st.markdown("## Answer: Spherical model, moderate to low nugget e.g. 0.2-0.3 and moderate to long range e.g. 60-80m")
  results.append([1, s,n,r])
  s,n,r = ex_var(example=2, 
           hint='Hint: Think about the seasons.', 
           key_nugget='nug2', key_range='range2', key_stype='stype2', 
           im='sim2.jpg')
#   st.markdown("## Answer: Hole effect model, moderate to low nugget e.g. 0.2-0.3 and short range e.g. 10-20m")
  results.append([2, s,n,r])
  s,n,r = ex_var(example=3, 
           hint='Hint: Think about sand...', 
           key_nugget='nug3', key_range='range3', key_stype='stype3', 
           im='sim3.jpg')
#   st.markdown("## Answer: Power model, low nugget e.g. 0.0-0.1 and moderate to long range e.g. 50-70m")
  results.append([3, s,n,r])
  s,n,r = ex_var(example=4, 
           hint='Hint: This is when you wonder why you bother to get out of bed in the morning.', 
           key_nugget='nug4', key_range='range4', key_stype='stype4', 
           im='sim4.jpg')
#   st.markdown("## Answer: Spherical model, high nugget e.g. 0.4-0.6 and moderate to short range e.g. 20-30m")
  results.append([4, s,n,r])
  df = pd.DataFrame(data=results, 
                    columns=['Example', 'Structure Type', 'Nugget', 'Range'])
  uname = getpass.getuser()
  st.table(df)
  

  

  

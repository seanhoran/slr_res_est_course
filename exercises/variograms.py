import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def variogram(nugget=0.0, srange=100.):
  var = 1.-nugget
  h = np.arange(120.)
  gamma = nugget + var*((3*h)/(2*srange)-(h**3)/(2*srange**3))
  gamma[h==0]=0.
  gamma[h>srange]=1.0
  return gamma, h; 

def variograms():
  st.title("Variogram Exercise")
  st.write("")
  st.write("Model the appropriate variogram")
  col1, col2 = st.beta_columns([1, 2])
  with col1:
    nugget = st.slider('Nugget', 0.0, 1.0, 0.1, 0.05, key='nugget') 
    srange = st.slider('Range', 0.0, 120., 100., 10., key='range')
    gamma, h = variogram(nugget, srange)
    fig, ax = plt.subplots()
    plt.plot(h, gamma, '-r')
    plt.xlabel('Range (m)')
    plt.ylabel('Gamma')
    st.pyplot(fig)  
  with col2:
    st.write("")
    st.write("")
    st.image("..//pdac2021_res_est_course//images//sim1.jpg", width=450)
   

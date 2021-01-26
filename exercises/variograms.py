import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def variogram(nugget=0.0, srange=100., struct_type='Spherical'):
  var = 1.-nugget
  h = np.arange(120.)
  gamma = h
  if struct_type == 'Spherical':
    gamma = nugget + var*((3*h)/(2*srange)-(h**3)/(2*srange**3))
    gamma[h>srange]=1.0
    gamma[0] = nugget
  elif struct_type == 'Gaussian':
    pass
  elif struct_type == 'Power':
    pass
  else:
    gamma = nugget*(1.0-np.exp((-3*h/srange)*np.pi)*(np.cos(h/1)*np.pi))
    
    
      
  return gamma, h; 

def variograms():
  st.title("Variogram Exercise")
  st.write("")
  st.markdown("## Model the appropriate variogram for each grade pattern observed")
  st.markdown("### Example 1:")
  col1, col2 = st.beta_columns([1, 2])
  with col1:
    struct_type = st.selectbox("Structure Type", options=["Spherical", "Gaussian", "Power", "Hole Effect"], index=0)
    nugget = st.slider('Nugget', 0.0, 1.0, 0.1, 0.05, key='nugget') 
    srange = st.slider('Range', 0.0, 120., 100., 10., key='range')
    gamma, h = variogram(nugget, srange, struct_type)
    fig, ax = plt.subplots()
    plt.plot(h, gamma, '-r')
    plt.xlabel('Range (m)')
    plt.ylabel('Gamma')
    plt.xlim((0.,120.))
    plt.ylim((0.,1.2))
    st.pyplot(fig)  
  with col2:
    st.write("")
    st.write("")
    st.write("")
    st.image("..//pdac2021_res_est_course//images//sim1.jpg", width=460)
   

import numpy as np
import matplotlib.pyplot as plt

def variogram(nugget=0.0, srange=100.):
  var = 1.-nugget
  h = np.arange(150.)
  gamma = nugget + var*((3*h)/(2*srange)-(h**3)/(2*srange**3))
  gamma[h==0]=0.
  gamma[h>srange]=1.0
  return gamma, h; 

def variograms():
  gamma, h = variogram(0.3, 60.)
  fig, ax = plt.subplots()
  plt.plot(h, gamma, '-r')
  st.pyplot(fig)

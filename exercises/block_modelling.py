import streamlit as st
import streamlit.components.v1 as components

def block_modelling():
  st.markdown("# Leapfrog View Example")

  html = '<iframe src="https://view.seequent.com/embed/hbev1b2f395mzjahn1v9/default/kazbudqcim9aj33cpuiw" width=800 height=650 allowfullscreen></iframe>'

  st.markdown("Embedding using markdown:")

  st.markdown(html, unsafe_allow_html=True)

  st.markdown("Embedding using components.iframe:")
  components.iframe(html)

  st.markdown("Embedding using components.html:")
  components.html(html)

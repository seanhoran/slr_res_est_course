import streamlit as st
import itertools
import os
import funcs

def about_course():
  
  st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  st.title("Fundamentos de la Estimación de Recursos Minerales")
  
  # get text from text_blocks:
  text = funcs.get_text_block("about_course_esp.txt")
  st.write(text)
  
  st.write("")
  st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  st.markdown("# Presentadores")
  for presenter in ['Sean Horan', 'Rosmery Cardenas', 'Benjamin Sanfurgo', 'Ian Weir']:
    split_name = presenter.split(" ")
    lcase_name = (split_name[0] + "_" + split_name[1]).lower()
    ucase_name = (split_name[0] + "_" + split_name[1])

    col1, col2 = st.columns([1,2.5])
    with col1:
      st.image("..//slr_res_est_course//headshots//" + ucase_name + ".jpg", use_column_width=True)
      text = funcs.get_text_block("title_" + lcase_name + ".txt")
      st.markdown(text)
    with col2:
      text = funcs.get_text_block("resume_" + lcase_name + "_esp.txt")
      st.write(text)
 

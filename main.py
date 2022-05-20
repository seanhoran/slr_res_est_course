import streamlit as st
import exercises.about_course as about_course
import exercises.capping_ex as capping_ex
import exercises.variograms as variograms
import exercises.cut_off as cut_off
import exercises.block_modelling as block_modelling
import exercises.geo_interp as geo_interp
import exercises.reporting as reporting
import exercises.interp as interp
import exercises.about_streamlit as about_streamlit


import exercises.about_course_esp as about_course_esp
import exercises.capping_ex_esp as capping_ex_esp
import exercises.variograms_esp as variograms_esp
import exercises.cut_off_esp as cut_off_esp
import exercises.block_modelling_esp as block_modelling_esp
import exercises.geo_interp_esp as geo_interp_esp
import exercises.reporting_esp as reporting_esp
import exercises.interp as interp
# import exercises.about_streamlit as about_streamlit

max_width = 1200

padding_top = 0
padding_right = 0
padding_left = 0
padding_bottom = 0
COLOR = '#180c52'
BACKGROUND_COLOR = 'white'

# st.markdown(
#         f"""
# <style>
#     .reportview-container .main .block-container{{
#         max-width: {max_width}px;
#         padding-top: {padding_top}rem;
#         padding-right: {padding_right}rem;
#         padding-left: {padding_left}rem;
#         padding-bottom: {padding_bottom}rem;
#     }}
#     .reportview-container .main {{
#         color: {COLOR};
#         background-color: {BACKGROUND_COLOR};
#     }}
# </style>
# """,
#         unsafe_allow_html=True,
#     )

st.set_page_config(
     page_title="Fundamentals of Resource Estimation",
     page_icon="random",
     layout="wide",
     initial_sidebar_state="expanded")

lang = st.sidebar.selectbox("Select Language/Escoje Idioma", options=['English', 'Espanol'])

st.sidebar.image("..//slr_res_est_course//images//SLR Logo 2020 _RGB-dark blue_for web.png")

# Capping Exercise - interactive
# Compositing - Q&A
# Variograms - interactive
# Interpolation - interactive
# Compositing - Q&A

if lang == 'English':

    radio_options = ["01 About the Course",
                     "02 Geological Interp",
                     "03 Capping",
                     "04 Variograms",
                     "05 Interpolation",
                     "06 Cut-Off Grade",
                     "07 Reporting/Classification",
                     "08 About Streamlit"]
else:
    radio_options = ["01 Sobre El Curso",
                     "02 Interpretacion Geologica",
                     "03 Capping",
                     "04 Variogramas",
                     "05 Interpolacion",
                     "06 Ley de Corte",
                     "07 Reportes/Classificacion",
                     "08 Sobre Streamlit"]


exercise=st.sidebar.radio("", 
                          options=radio_options, 
                          index=0, 
                          key=None)

if lang == 'English':
    if exercise == radio_options[0]:
      about_course.about_course()
    if exercise == radio_options[1]:
    #   st.write("Page available during nominated exercise session")
      geo_interp.geo_interp()
    if exercise == radio_options[2]:
    #   st.write("Page available during nominated exercise session")
      capping_ex.capping_ex()
    if exercise == radio_options[3]:
    #   st.write("Page available during nominated exercise session")
      variograms.variograms()
    if exercise == radio_options[4]:
    #   st.write("Page available during nominated exercise session")
    #   interp.block_modelling()
      block_modelling.block_modelling()
    if exercise == radio_options[5]:
    #   st.write("Page available during nominated exercise session")
      cut_off.cut_off()
    if exercise == radio_options[6]:
    #   st.write("Page available during nominated exercise session")
      reporting.reporting()
    if exercise == radio_options[7]:
    #   st.write("Page available during nominated exercise session")
      about_streamlit.about_streamlit()
else:
    if exercise == radio_options[0]:
      about_course_esp.about_course()
    if exercise == radio_options[1]:
    #   st.write("Page available during nominated exercise session")
      geo_interp_esp.geo_interp()
    if exercise == radio_options[2]:
    #   st.write("Page available during nominated exercise session")
      capping_ex.capping_ex()
    if exercise == radio_options[3]:
    #   st.write("Page available during nominated exercise session")
      variograms_esp.variograms()
    if exercise == radio_options[4]:
    #   st.write("Page available during nominated exercise session")
    #   interp.block_modelling()
      block_modelling_esp.block_modelling()
    if exercise == radio_options[5]:
    #   st.write("Page available during nominated exercise session")
      cut_off_esp.cut_off()
    if exercise == radio_options[6]:
    #   st.write("Page available during nominated exercise session")
      reporting_esp.reporting()
    if exercise == radio_options[7]:
    #   st.write("Page available during nominated exercise session")
      about_streamlit_esp.about_streamlit()


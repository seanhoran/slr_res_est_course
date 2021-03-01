import streamlit as st

def geo_interp():

    st.title("Geological Interpretation")

    '''
    ## Question 1: Pick a modelling cut-off
    
    You are tasked with building a Mineral Resource domain for a typical orogenic gold deposit of Ontario.​

    The mineralization is erratic and, for the most part, hosted within a fractured basalt.​

    Review the following cross sections showing mineralization at a variety of cut-off grades, as well as lithology and answer the following questions:
    '''

    q1_options = ["Select an Answer",
                  "25% of the economic cut-off",
                  "50% of the economic cut-off",
                  "75% of the economic cut-off",
                  "100% of the economic cut-off",
                  "Limit to host lithology irrespective of grade"]

    st.radio("What cut-off grade will you use to guide your Mineralization Domain?", options=q1_options, key="q1")

    q2_options = ["Select an Answer",
                  "I will need to manage high grades.",
                  "I will need to carefully design the interpolation to not over-smooth grades.",
                  "I will need to be cautious about how I connect mineralization in less tightly drilled areas.",
                  "I will need to confirm this choice using exploratory data analysis (EDA)."]

    st.radio("How will this choice impact how I design the downstream workflow for Mineral Resource estimation?", options=q2_options, key="q2")

    col1, col2, col3 = st.beta_columns((1,1,1))

    with col1:
        st.write("")
        st.write("Litho")
        st.write("")
        st.write("")
        st.image("..//pdac2021_res_est_course//images//litho.jpg", width=400)

    with col2:

        cog = st.slider("Select a cut-off (% of economic cut-off)", min_value=0,value=0, step=1, max_value=3, key="sl1")
        st.image("..//pdac2021_res_est_course//images//gt" + str(int(cog)) + ".jpg", width=400)

    with col3:

        cog2 = st.slider("Select a cut-off (% of economic cut-off)", min_value=0, value=0, step=1, max_value=4, key="sl2")
        st.image("..//pdac2021_res_est_course//images//gt2" + str(int(cog2))+ ".jpg", width=400)



import streamlit as st
import funcs

def geo_interp():
    
    st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)

    st.title("Geological Interpretation")

    st.markdown("## Question 1a: Pick a modelling cut-off")
    st.markdown("")
    st.markdown("You are tasked with building a Mineral Resource domain for a typical orogenic gold deposit of Ontario.")
    st.markdown("The mineralization is erratic and, for the most part, is hosted within a fractured basalt.")
    st.markdown("Review the following cross sections showing mineralization at a variety of cut-off grades, as well as lithology and answer the following questions:")

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.write("")
        st.write("Litho")
        st.write("")
        st.write("")
        st.write("")
        st.image("..//slr_res_est_course//images//litho.jpg", output_format="PNG")

    with col2:

        cog = st.slider("Select a cut-off (% of economic cut-off)", min_value=0,value=0, step=1, max_value=3, key="sl1")
        st.image("..//slr_res_est_course//images//gt" + str(int(cog)) + ".jpg")

    with col3:

        cog2 = st.slider("Select a cut-off (% of economic cut-off)", min_value=0, value=0, step=1, max_value=4, key="sl2")
        st.image("..//slr_res_est_course//images//gt2" + str(int(cog2))+ ".jpg")
        
    q1_options = ["Select an Answer",
                  "25% of the economic cut-off",
                  "50% of the economic cut-off",
                  "75% of the economic cut-off",
                  "100% of the economic cut-off",
                  "Limit to host lithology irrespective of grade"]

    st.radio("What cut-off grade will you use to guide your Mineralization Domain?", options=q1_options, key="q1")
#     st.markdown("## Answer: 25% of the cut-off grade.")
    

    st.markdown("## Question 1b: What is the impact?")
    q2_options = ["Select an Answer",
                  "I will need to manage high grades.",
                  "I will need to carefully design the interpolation to not over-smooth grades.",
                  "I will need to be cautious about how I connect mineralization in less tightly drilled areas.",
                  "I will need to confirm this choice using exploratory data analysis (EDA)."]

    st.radio("How will this choice impact how I design the downstream workflow for Mineral Resource estimation?", options=q2_options, key="q2")
#     st.markdown("## Answer: All of the above.")
    st.write("")       
    st.write("")
    
    st.markdown("")
    st.markdown("## Question 2: Choose a domaining strategy")
    st.markdown("")
    text = funcs.get_text_block("geo_interp_q2.txt")
    st.markdown(text)
    q3_options = ["Select an Answer",
                  "All together.",
                  "All separate.",
                  "There is no need to model phosphorus.",
                  "Silica and iron together, phosphorus separate."]

    st.radio("How will I domain and estimate these elements?", options=q3_options, key="q3")
    colz1, colz2, colz3 = st.columns((0.8,0.7,1))
    
    with colz1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("..//slr_res_est_course//images//flow_chart.jpg")
    with colz2:
        sel_graph = st.selectbox("Select Graph", options=['Fe vs Si', 'P vs Si'], index=0, key='g1')
        if sel_graph == 'Fe vs Si':
            inp = 'fesi.jpg'
        else:
            inp = 'psi.jpg'
        st.image("..//slr_res_est_course//images//" + inp)
            
    with colz3:
        sel_sect = st.selectbox("Display Section", options=['Si', 'Fe', 'P'], index=0, key='g1')
        st.image("..//slr_res_est_course//images//" + sel_sect + "_sect.jpg")
#     st.markdown("## Answer: Silica and iron together, phosphorus separate.")


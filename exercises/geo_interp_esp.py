import streamlit as st
import funcs

def geo_interp():
    
    st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)

    st.title("Interprtación Geológica")

    st.markdown("## Pregunta 1a: Elija una ley de corte para modelamiento")
    st.markdown("")
    st.markdown("Tiene la tarea de construir un dominio de recursos minerales para un depósito de oro orogénico típico de Ontario.")
    st.markdown("La mineralización es errática y, en su mayor parte, está alojada dentro de un basalto fracturado.")
    st.markdown("Revise las siguientes secciones transversales que muestran la mineralización en una variedad de leyes de corte, así como la litología y responda las siguientes preguntas:")

    q1_options = ["Selecione una Respuesta",
                  "25% de la ley de corte económica",
                  "50% de la ley de corte económica",
                  "75% de la ley de corte económica",
                  "100% de la ley de corte económica",
                  "Limitar a la roca de caja independiente de la ley"]

    st.radio("¿Qué ley de corte usaría para guiar su Dominio de Mineralización?", options=q1_options, key="q1")
    st.markdown("## Respuesta: 25% de la ley de corte.")
    

    st.markdown("## Question 1b: Cuál es el impacto?")
    q2_options = ["Selecione una Respuesta",
                  "Tendré que manejar las altas leyes.",
                  "Tendré que diseñar cuidadosamente la interpolación para no sobre suavizar leyes.",
                  "Tendré que ser cauteloso sobre cómo conecto la mineralización en áreas menos perforadas.",
                  "Tendré que confirmar esta opción usando análisis exploratorio de datos (EDA)."]

    st.radio("¿Cómo afectará esta elección a la forma en que diseño el flujo de trabajo aguas abajo para la estimación de recursos minerales?", options=q2_options, key="q2")
    st.markdown("## Respuesta: Todas las anteriores.")
    st.write("")       
    st.write("")
    
    st.markdown("## Pregunta 2: Elija una estrategia de modelamiento")
    st.markdown("")
    
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
        
    st.markdown("")
    text = funcs.get_text_block("geo_interp_q2.txt")
    st.markdown(text)
    q3_options = ["Selecione una Respuesta",
                  "Todas combinadas.",
                  "Todas separadas.",
                  "No hay necesidad de modelar fósforo.",
                  "Sílice y hierro juntos, fósforo separado."]

    st.radio("¿Cómo modelaré y estimaré estos elementos?", options=q3_options, key="q3")
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
    st.markdown("## Answer: Silica and iron together, phosphorus separate.")


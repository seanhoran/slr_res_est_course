import streamlit as st
import funcs
import pandas as pd
import numpy as np
import plotly.express as px

def adjust_calculation(df2):
  
  colx1, colx2, colx3, colx4 = st.columns((1,1,1,1))
  
  with colx1:
    st.markdown("Block Grade")
    df2.loc[0, 'Resource COG'] = 1000000
    df2.loc[1, 'Resource COG'] = st.slider("Cu %", 0., 4.0, 0.9, 0.1, key="cgsl2")
    df2.loc[2, 'Resource COG'] = st.slider("Au g/t", 0., 2.0, 0.7, 0.1, key="cgsl3")
    cug = df2.loc[1, 'Resource COG']
    aug = df2.loc[2, 'Resource COG']
  with colx2:
    st.markdown("Recoveries")
    df2.loc[4, 'Resource COG'] = st.slider("Cu Recovery", 60., 95., 87., 1.0, key="cgsl4")
    df2.loc[5, 'Resource COG'] = st.slider("Au Recovery", 60., 95., 90., 1.0, key="cgsl5")
  with colx3:
    st.markdown("Metal Prices")
    df2.loc[16, 'Resource COG'] = st.slider("Cu Price ($/lbs)", 2.5, 10.0, 3.25, 0.1, key="cgsl6")
    df2.loc[17, 'Resource COG'] = float(st.slider("Au Price ($/oz)", 1000.0, 2000.0, 1500.0, 100.0, key="cgsl7"))
  with colx4:
    st.markdown("Other")
    df2.loc[10, 'Resource COG'] = st.slider("Cu Con Grade", 20.0, 35.0, 25.0, 1.0, key="cgsl8")
    df2.loc[13, 'Comments'] = st.slider("Payable Cu", 85., 100., 90., 1.0, key="cgsl9")
    df2.loc[14, 'Comments'] = st.slider("Payable Au", 85., 100., 99., 1.0, key="cgsl10")

  df2.loc[7, 'Resource COG'] = np.round(df2.loc[0, 'Resource COG']*(df2.loc[1, 'Resource COG']/100.)*(df2.loc[4, 'Resource COG']/100.)*2.20462,0)
  df2.loc[8, 'Resource COG'] = np.round(df2.loc[0, 'Resource COG']*(df2.loc[2, 'Resource COG'])/31.1035*(df2.loc[5, 'Resource COG']/100.), 0)
  df2.loc[9, 'Resource COG'] = np.round(df2.loc[7, 'Resource COG']*1000./2204.62/(df2.loc[10, 'Resource COG']/100.), 0)
  df2.loc[11, 'Resource COG'] = np.round(df2.loc[8, 'Resource COG']*31.1035/df2.loc[9, 'Resource COG'],2)

  df2.loc[13, 'Resource COG'] = np.round(df2.loc[7, 'Resource COG']*(df2.loc[13, 'Comments'])/100.,0)
  df2.loc[14, 'Resource COG'] = np.round(df2.loc[8, 'Resource COG']*(df2.loc[14, 'Comments'])/100,0)

  df2.loc[18, 'Resource COG'] = np.round(df2.loc[13, 'Resource COG']*df2.loc[16, 'Resource COG'], 0)
  df2.loc[19, 'Resource COG'] = np.round(df2.loc[14, 'Resource COG']*float(df2.loc[17, 'Resource COG']/1000.), 0)

  df2.loc[20, 'Resource COG'] = df2.loc[18, 'Resource COG']+df2.loc[19, 'Resource COG']

  df2.loc[22, 'Resource COG'] = np.round(df2.loc[9, 'Resource COG']*9.0/1000, 0)
  df2.loc[23, 'Resource COG'] = np.round(df2.loc[13, 'Resource COG']*0.09,0)
  df2.loc[24, 'Resource COG'] = np.round(df2.loc[14, 'Resource COG']*5.0/1000, 0)

  df2.loc[25, 'Resource COG'] = np.round(df2.loc[20, 'Resource COG']-df2.loc[22, 'Resource COG']-df2.loc[23, 'Resource COG']-df2.loc[24, 'Resource COG'], 0)

  df2.loc[27, 'Resource COG'] = np.round((df2.loc[18, 'Resource COG']-df2.loc[22, 'Resource COG']-0.09*df2.loc[13, 'Resource COG']/1000.)/df2.loc[25, 'Resource COG'], 2)
  df2.loc[28, 'Resource COG'] = np.round((df2.loc[19, 'Resource COG']-df2.loc[23, 'Resource COG']-5.0*df2.loc[14, 'Resource COG']/1000.)/df2.loc[25, 'Resource COG'], 2)

  df2.loc[30, 'Resource COG'] = np.round((df2.loc[27, 'Resource COG']*df2.loc[25, 'Resource COG']*1000./(df2.loc[0, 'Resource COG']*df2.loc[1, 'Resource COG'])),0)
  df2.loc[31, 'Resource COG'] = np.round((df2.loc[28, 'Resource COG']*df2.loc[25, 'Resource COG']*1000./(df2.loc[0, 'Resource COG']*df2.loc[2, 'Resource COG'])),0)

  colz1, colz2, colz3 = st.columns((1,1,1))

  metal = ['Cu', 'Au']
  grades = np.array([cug, aug])
  nsr_fact = np.array([df2.loc[30, 'Resource COG'], df2.loc[31, 'Resource COG']])
  blk_rev = grades*nsr_fact
  ddf = pd.DataFrame({'Metal':metal, 'Grade': grades, 'Revenue by Metal Unit': nsr_fact, 'Block Revenue per tonne':blk_rev})

  with colz1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.table(ddf)
  with colz2:
    fig = px.bar(ddf, x='Metal', y='Revenue by Metal Unit', color='Metal')
    fig.update_yaxes(range=(0,200))
    st.plotly_chart(fig,  use_container_width=True)

  with colz3:
    fig = px.bar(ddf, x='Metal', y='Block Revenue per tonne', color='Metal')
    fig.update_yaxes(range=(0,200))
    st.plotly_chart(fig,  use_container_width=True)

  # st.table(df2)

def cut_off():

  st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)

  df = pd.read_csv("..//slr_res_est_course//data//Worksheet COGs.csv")
  df = df.fillna("")
  df = df[:32].copy()

  st.title("Ejercico de ley de corte")
  st.write("")
  st.markdown("## Pregunta 1: ¿Enviamos este bloque a la planta de procesamiento?")
  st.write("")

  col1, col2 = st.columns([1, 2])

  with col1:
    st.image("..//slr_res_est_course//images//cog1_block.jpg", width=300)
  with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown('### Operating costs:')
    st.markdown('* Mining: $50/t')
    st.markdown('* Process: $20/t')
    st.markdown('* G&A: $15/t')

  q1_options = ['yes', 'no']
  cog_q1_answer = st.radio("¿Enviamos este bloque a la planta de procesamiento?", options=q1_options, key='cog_q1')
#   st.markdown("## Respuesta: Depende, nos falta informacion, fundamentalmente los precios de los metales y las recuperaciones")

  st.write("")
  st.markdown("## Pregunta 2: Calculo Complejo de Ley de Corte")
  st.write("")
  st.markdown("### Teniendo en cuenta la ley del bloque de la Pregunta 1, analice el calculo de NSR y responda la pregunta a continuacion.")
  st.write("")
  col3, col4 = st.columns([1, 2])
  with col3:
    text = funcs.get_text_block("cog_q2_intro.txt")
    st.markdown(text)
  with col4:
    st.image("..//slr_res_est_course//images//nsr_table.png", width=500)
    st.write("*Tenga en cuenta que la ley promedio del deposito no se conoce hasta que se conoce la ley de corte. Esta es normalmente una primera aproximacion y un proceso iterativo. Si bien no afecta los calculos, una vez que se conoce la ley meedia, se puede realizar un analisis de flujo de caja simple.")
  q2_options = ['A. No tengo idea',
                'B. El valor del bloque esta por debajo de todas las leyes de corte',
                'C. El valor del bloque es mayor que el marginal pero menor que el break-even cut-off',
                'D. El valor del bloque excede todas leyes de corte']
  cog_q2_answer = st.radio("Select the appropriate statement:", options=q2_options, key='cog_q2')
#   st.markdown("## Respuesta: C. El valor del bloque es mayor que el marginal pero menor que el break-even cut-off. Cuando multiplica los factores NSR por las leyes, supera el 60 % del costo de extraccion + G&A + Procesamiento, pero no el 100 % de los costos.")

  st.write("")
  st.markdown("## Pregunta 3: Sensibilidades")
  st.write("")
  st.markdown("### Al ajustar los diversos parametros de entrada que se dan a continuacion, comente lo siguiente")
  st.text_area("1. Que precio del cobre da como resultado un ingreso que es el doble de la ley de corte de equilibrio", height=5, key='tt1')
#   st.markdown("## Respuesta: Alrededor US$7/lb")
  st.text_area("2. Que leyo de cobre da como resultado un ingreso que es el doble de la ley de corte de equilibrio", height=5, key='tt2')
#   st.markdown("## Respuesta: La ley de Cu no sube lo suficiente lo que sugiere es >2% Cu.")
  st.write("")
  adjust_calculation(df.copy())
  

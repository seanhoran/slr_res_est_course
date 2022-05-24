import streamlit as st

def capping_ex():
 
  st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)
 
  st.title("Capping Exercise")
  
  count_correct = 0
  
  st.write("El modulo de restriccion de leyes altas tiene algunas herramientas que pueden ayudar a identificar si se requiere una restriccion de las leyes altas. Este ejercicio utiliza datos reales y muestra como el flujo de trabajo de restriccion de leyes altas es iterativo, y que su decision de modelarlas geologicamente y/o cortar o restringir valores extremos debe ser basada en un grupo de herramientas. Por ultimo, es importante tener en cuenta que puede optar por revisar su flujo de trabajo de restriccion de leyes altas despues de validar su estimacion visual y estadisticamente, ya que el impacto de las muestras de leyes altas en la estimacion final de recurso puede ser significativo.")

#   st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)

  st.header("Ejercicio 1 - Deposito de Oro - Pregunta 1")
   
  q1_options = ['Por favor, Seleccione una respuesta', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Otro',
               'Algo esta mal']
  
  
  q1_answer=st.radio('Revise el siguiente histograma, grafico de probabilidad y el analisis de deciles y determine sobre que ley es mas apropiado limitar. Una revision cuidadosa de las plantas y secciones proporciona una mejor idea de la distribucion espacial de los deciles preseleccionados.', options=q1_options, index=0, key='quest1')
  col1, col2, col3 = st.columns((1,1.5,1))
  with col1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG_LG_Decile.jpg", use_column_width=True)
  with col2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_LG_HISTO.jpg", use_column_width=True)
  with col3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_LG_PP.jpg", use_column_width=True)
  
  cola1, cola2 = st.columns((1,1.6))
  with cola1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG_LG_PlanCaps.jpg", use_column_width=True)
  with cola2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG_LG_ObliqueCaps.jpg", use_column_width=True)
   st.subheader("Oblique View - Looking Along Strike")
  st.write("")
  st.subheader("Respuesta: Algo esta mal: el conjunto de datos tiene una poblacion de alta ley que debe evaluarse de forma independiente.")
  st.write("")
  st.write("")
  st.write("")
  
  st.header("Ejercicio 1 - Deposito de Oro - Pregunta 2")
  q2_options = ['Por favor, Seleccione una respuesta', 
             '5 g/t Au', 
             '10 g/t Au', 
             '15 g/t Au',
               'Otro',
               'Algo esta mal']
  
  q2_answer=st.radio('Revise el siguiente histograma, grafico de probabilidad y el analisis de deciles y determine sobre que ley es mas apropiado limitar. Revisie cuidadosamente las plantas y secciones para obtener una mejor idea de la distribucion espacial de los deciles preseleccionados.', options=q2_options, index=0, key='quest2')
  colb1, colb2, colb3 = st.columns((1,1.5,1))
  with colb1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//LG_Decile.jpg", use_column_width=True)
  with colb2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//LG_HISTO.jpg", use_column_width=True)
  with colb3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//LG_PP.jpg", use_column_width=True)
  
  colc1, colc2 = st.columns((1,1.6))
  with colc1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//LG_PlanCaps.jpg", use_column_width=True)
  with colc2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//LG_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
  st.subheader("Respuesta: 5 g/t Au o 10 g/t Au dependiente del practicante.")
  st.write("")
  st.write("")
  st.write("")
  

  
  st.header("Ejercicio 1 - Deposito de Oro - Pregunta 3")
   
  q3_options = ['Por favor, Seleccione una respuesta', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Otro',
               'Algo esta mal']
  
  q3_answer=st.radio('Revise el siguiente histograma, grafico de probabilidad y el analisis de deciles y determine sobre que ley es mas apropiado limitar. Una revision cuidadosa de las plantas y secciones proporciona una mejor idea de la distribucion espacial de los deciles preseleccionados.', options=q3_options, index=0, key='quest3')
  cold1, cold2, cold3 = st.columns((1,1.5,1))
  with cold1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG_Decile.jpg", use_column_width=True)
  with cold2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_HISTO.jpg", use_column_width=True)
  with cold3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_PP.jpg", use_column_width=True)
  
  cole1, cole2 = st.columns((1,1.6))
  with cole1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG_PlanCaps.jpg", use_column_width=True)
  with cole2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
  st.subheader("Respuesta: Algo esta mal: el conjunto de datos tiene una poblacion de alta ley que debe evaluarse de forma independiente.")
  st.write("")
  st.write("")
  st.write("")
  

  st.header("Ejercicio 1 - Deposito de Oro - Pregunta 4")
   
  q4_options = ['Por favor, Seleccione una respuesta', 
             '5 g/t Au', 
             '10 g/t Au', 
             '15 g/t Au',
               'Otro',
               'Algo esta mal']
  
  q4_answer=st.radio('Revise el siguiente histograma, grafico de probabilidad y el analisis de deciles y determine sobre que ley es mas apropiado limitar. Una revision cuidadosa de las plantas y secciones proporciona una mejor idea de la distribucion espacial de los deciles preseleccionados.', options=q4_options, index=0, key='quest4')
  colf1, colf2, colf3 = st.columns((1,1.5,1))
  with colf1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG_2_7_Decile.jpg", use_column_width=True)
  with colf2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_2_7_HISTO.jpg", use_column_width=True)
  with colf3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG_2_7_PP.jpg", use_column_width=True)
  
  colg1, colg2 = st.columns((1,1.6))
  with colg1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG_2_7_PlanCaps.jpg", use_column_width=True)
  with colg2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG_2_7_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
  st.subheader("Respuesta: 10 g/t Au o 15 g/t Au dependiente del practicante.")
  st.write("")
  st.write("")
  st.write("")
  


  st.header("Ejercicio 1 - Deposito de Oro - Pregunta 5")
   
  q5_options = ['Por favor, Seleccione una respuesta', 
             '10 g/t Au', 
             '20 g/t Au', 
             '25 g/t Au',
               'Otro',
               'Algo esta mal']
  
  q5_answer=st.radio('Revise el siguiente histograma, grafico de probabilidad y el analisis de deciles y determine sobre que ley es mas apropiado limitar. Una revision cuidadosa de las plantas y secciones proporciona una mejor idea de la distribucion espacial de los deciles preseleccionados.', options=q5_options, index=0, key='quest5')
  colh1, colh2, colh3 = st.columns((1,1.5,1))
  with colh1:
   st.subheader("Decile Analysis")
   st.image("..//slr_res_est_course//images//HG1_Decile.jpg", use_column_width=True)
  with colh2:
   st.subheader("Histogram")
   st.write("")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG1_HISTO.jpg", use_column_width=True)
  with colh3:
   st.subheader("Probability Plot")
   st.write("")
   st.write("")
   st.write("")
   st.image("..//slr_res_est_course//images//HG1_PP.jpg", use_column_width=True)
  
  coli1, coli2 = st.columns((1,1.6))
  with coli1:
   st.subheader("Plan View - Looking Down")
   st.image("..//slr_res_est_course//images//HG1_PlanCaps.jpg", use_column_width=True)
  with coli2:
   st.subheader("Oblique View - Looking Along Strike")
   st.image("..//slr_res_est_course//images//HG1_ObliqueCaps.jpg", use_column_width=True)
  st.write("")
  st.subheader("Respuesta: 25 g/t Au o potencialmente mas alto basado en una revision espacial mas detallada.")
  st.write("")
  st.write("")
  st.write("")
  
  

  st.image("..//slr_res_est_course//images//wireframe_header.jpg", use_column_width=True)
  
  st.write("Como se habran dado cuenta en las vistas en planta y secciones, el conjunto de datos del deposito de oro de la Pregunta 1 contiene una poblacion de ley alta y baja, donde las vetas de ley alta estan rodeadas por un halo de alteracion de baja ley. El segundo ejercicio es una continuacion del primero y requiere que haga coincidir los dominios que se muestran en las imagenes a continuacion con las estadisticas presentadas en cada una de las preguntas del primer ejercicio. Si tuvo algunas respuestas incorrectas en el primer ejercicio, consulte la informacion y las imagenes a continuacion antes de comenzar el Ejercicio 2.")
  
  st.write("Note: Las siguientes imagenes son vistas inclinadas y miran hacia abajo a lo largo del rumbo, como las presentadas en el Ejercicio 1. Se construyeron solidos para los Dominios 1 y 2 con una ley de corte nominal de 1 g/t Au, mientras que los solidos del Dominio 3 se construyeron a una ley de corte nominal de 0,20 g/t Au.")

  st.subheader("Domains 1, 2 and 3")
  st.image("..//slr_res_est_course//images//Domains123.jpg", use_column_width=True)
  st.subheader("Domains 1, 2 and 3 with Capped Assays")
  st.image("..//slr_res_est_course//images//Domains123_Caps2.jpg", use_column_width=True)
  st.subheader("Capped Assays")
  st.image("..//slr_res_est_course//images//Domains123_Caps.jpg", use_column_width=True)

  st.header("Ejercicio 2 - Deposito de Oro - Pregunta 1")
   
  q6_options = ['Por favor, Seleccione una respuesta', 
             'Dominio 1', 
             'Dominio 2', 
             'Dominio 3',
             'Dominios 1 and 2',
             'Dominios 1 and 3',
             'Dominios 1, 2, and 3']
  
  q6_answer=st.radio('?Que dominio(s) refleja(n) mejor el histograma, la grafica de probabilidad y el analisis de decil presentado en la Pregunta 1 del Ejercicio 1?', options=q6_options, index=0, key='quest6')
  st.write("")
  st.subheader("Respuesta: Dominios 1, 2 y 3")
  st.write("")
  st.write("")
  st.write("")
  

   
  st.header("Ejercicio 2 - Deposito de Oro - Pregunta 2")
   
  q7_options = ['Por favor, Seleccione una respuesta', 
             'Dominio 1', 
             'Dominio 2', 
             'Dominio 3',
             'Dominios 1 and 2',
             'Dominios 1 and 3',
             'Dominios 1, 2, and 3']
  
  q7_answer=st.radio('?Que dominio(s) refleja(n) mejor el histograma, la grafica de probabilidad y el analisis de decil presentado en la Pregunta 2 del Ejercicio 1?', options=q7_options, index=0, key='quest7')
  st.write("")
  st.subheader("Respuesta: Dominio 3")
  st.write("")
  st.write("")
  st.write("")
  

   
  st.header("Ejercicio 2 - Deposito de Oro - Pregunta 4")
   
  q9_options = ['Por favor, Seleccione una respuesta', 
             'Dominio 1', 
             'Dominio 2', 
             'Dominio 3',
             'Dominios 1 and 2',
             'Dominios 1 and 3',
             'Dominios 1, 2, and 3']
  
  q9_answer=st.radio('?Que dominio(s) refleja(n) mejor el histograma, la grafica de probabilidad y el analisis de decil presentado en la Pregunta 3 del Ejercicio 1?', options=q9_options, index=0, key='quest8')

  st.write("")
  st.subheader("Respuesta: Dominios 1 y 2")
  st.write("")
  st.write("")
  st.write("")

  
  st.header("Ejercicio 2 - Deposito de Oro - Pregunta 5")
   
  q9_options = ['Por favor, Seleccione una respuesta', 
             'Dominio 1', 
             'Dominio 2', 
             'Dominio 3',
             'Dominios 1 and 2',
             'Dominios 1 and 3',
             'Dominios 1, 2, and 3']
  
  q9_answer=st.radio('?Que dominio(s) refleja(n) mejor el histograma, la grafica de probabilidad y el analisis de decil presentado en la Pregunta 4 del Ejercicio 1?', options=q9_options, index=0, key='quest9')

  st.write("")
  st.subheader("Respuesta: Dominio 2")
  st.write("")
  st.write("")
  st.write("")
 
    
  st.header("Ejercicio 2 - Deposito de Oro - Pregunta 6")
   
  q10_options = ['Por favor, Seleccione una respuesta', 
             'Dominio 1', 
             'Dominio 2', 
             'Dominio 3',
             'Dominios 1 and 2',
             'Dominios 1 and 3',
             'Dominios 1, 2, and 3']
  
  q10_answer=st.radio('?Que dominio(s) refleja(n) mejor el histograma, la grafica de probabilidad y el analisis de decil presentado en la Pregunta 5 del Ejercicio 1?', options=q10_options, index=0, key='quest10')
  st.write("")
  st.subheader("Respuesta: Dominio 1")1
  st.write("")
  st.write("")
  st.write("")
  


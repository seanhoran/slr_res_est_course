import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import warnings
from matplotlib.patches import Ellipse
warnings.simplefilter("ignore")
import matplotlib as mpl

color_seq = np.array(['grey', 'blue', 'green', 'yellow', 'orange', 'red', 'purple', 'purple'])
cog = np.array([-99, 0., 1.0, 1.5, 2.0, 2.5, 3.0, 3.0001])
cmap = mpl.colors.ListedColormap(color_seq)
norm = mpl.colors.BoundaryNorm(cog, cmap.N)

#@st.cache

def get_text_block(fname):
  # this is how to read a block of text:
  path = ""
  f = open(fname, "r")
  # and then write it to the app
  return f.read();


def rotate(pts, rot):
    c = np.cos(np.radians(rot))
    s = np.sin(np.radians(rot))
    rotmat = np.array([[c, -s], [s, c]])
    pts = np.dot(pts, rotmat)
    return pts;

def plot_samps(df, plot_contour=True):
    aniso = (300.) / (750.)
    fig, ax = plt.subplots(figsize=(15, 15 * aniso * 0.8))
    if plot_contour:
        xx, yy = dgrid(1.)
        rbfi = Rbf(df.YPT, df.ZPT,  df.AU_G_T, function='cubic')
        zz = rbfi(xx, yy)
        ax.contour(xx, yy, zz, cog, colors=color_seq, alpha=0.5)
        ax.imshow(zz, origin='lower', extent=(0., 750, 0., 300.), alpha=0.2, cmap=cmap, norm=norm)
    scat = ax.scatter(df.YPT, df.ZPT, c=df.AU_G_T, cmap=cmap, norm=norm, edgecolor="black", s=40)
    cbar = fig.colorbar(scat, ticks=cog)
    cbar.set_label('Au g/t', rotation=0)
    plt.xlim((0,750))
    plt.ylim((0, 300))
    plt.xlabel('X')
    plt.ylabel('Y')
    return fig, ax;

def block_modelling():

    st.title("Block Modelling Exercise")

    st.markdown("## **Analisis visual de tendencias**")
    st.markdown("La siguiente figura es una proyeccion ortogonal de todo el ancho de interseccion de una veta delgada.")
    st.markdown("Antes de cualquier analisis estadistico, es util mirar los datos." +
                " Trate, busque donde se encuentran las leyes altas y que tendencias puede observar." +
                " Al seleccionar una leyenda de colores, trate de usar una que resalte las tendencias pero considere algunos aspectos economicos." +
                " criterio tambien. Es siempre util tener una o dos leyendas de colores bajo la ley de corte." +
                " El ultimo consejo es, sea coherente con su leyenda, asegurese de que las muestras y los contornos/bloques utilicen el" +
                " mismo esquema de color.")

    df = pd.read_csv(".//slr_res_est_course//data//sim_pts.csv")
    df = df[df.use==1].copy().reset_index(drop=True)
    # fig, ax = plot_samps(df)
    # st.pyplot(fig)
    st.image("..//slr_res_est_course//images//contour.jpg", use_column_width=True)
    
    #-----------------------------------------------------------------------------------------------------------------#
    # Variogram
    # ----------------------------------------------------------------------------------------------------------------#

    st.markdown("## **Actividad: Variograma**")
    st.markdown("El variograma omnidireccional se muestra en el siguiente grafico." +
                " Tenga en cuenta que no se ha elegido ninguna direccion y que el alcance que se muestra sera mas corto que" +
                " la direccion mayor y mas largo que la direccion menor. Su trabajo es estimar el alcance" +
                " en la direccion mayor dadas tus observaciones del grafico anterior.")

    st.image("..//slr_res_est_course//images//interp_var.jpg")

    var_options = ["Seleccione la respuestar",
                   "Mayor = 75m, Semi-Mayor = 75m",
                   "Mayor = 125m, Semi-Mayor = 60m",
                   "Mayor = 75m, Semi-Mayor = 100m",
                   "Mayor = 150m, Semi-Mayor = 75m"]

    st.radio("Cual es su estimacion de los alcances en las direcciones mayor y semi mayor?", options=var_options, key='vv1')

    #-----------------------------------------------------------------------------------------------------------------#
    # Set up search ellipse
    # ----------------------------------------------------------------------------------------------------------------#
    st.markdown("## **Search Ellipse Activity**")

    # scol1, scol2 = st.columns((1, 1))
    # with scol1:
    st.markdown('#### Ellipse Shape')
    rot = st.number_input('Pick a Rotation (-360 to 360)', min_value=-360., max_value=360., value=0., step=5.)
    rot = (360. - rot)
    srange_major = st.number_input('Major Axis Range', min_value=10., max_value=500., value=100., step=5.)
    srange_minor = st.number_input('Semi-Major Axis Range', min_value=10., max_value=500., value=100., step=5.)
    # with scol2:
    #     st.markdown('#### Sample Selection')
    #     min_samps = st.number_input("Minimum Samples", min_value=1, max_value=40, value=2, step=1)
    #     max_samps = st.number_input("Maximum Samples", min_value=1, max_value=40, value=10, step=1)
    fig, ax = plot_samps(df, plot_contour=False)
    e = Ellipse(xy=[350, 150], width=srange_minor * 2, height=srange_major * 2, angle=rot, linewidth=2)
    ax.add_artist(e)
    e.set_facecolor('None')
    e.set_edgecolor('black')
    st.pyplot(fig)
    src_options = ["Selecione la respuesta",
                   "Mayjor = 75m, Semi-Mayor = 75m, Rotada en 90, Min 2 Max 40",
                   "Mayor = 125m, Semi-Mayor = 60m, Rotada -60 hacia el Sureste, Min 3 Max 12",
                   "Mayor = 125m, Semi-Mayor = 60m, Rotada 20 hacia el Suroeste, Min 2 Max 12",
                   "Mayor = 150m, Semi-Mayor = 75m, Min 2 Max 10, Sin Rotacion"]

    st.radio("Seleccionar los parametros de busqueda apropiados?", options=src_options, key='ss1')

    st.markdown("## **Adivina la modelo: Pregunta 1**")
    st.markdown("Las interpolaciones que se dan a continuacion son Vecino mas cercano (NN), Distancia inversa (ID) y Kriging ordinario (OK) respectivamente")
    st.markdown("Las curvas que aumentan hacia la derecha son las leyes para cada tecnica en diferentes leyes de cortes.")
    scol1, scol2 = st.columns((1, 1))
    with scol1:
        st.image("..//slr_res_est_course//images//interp_ests_q1.jpg", use_column_width=True)
    with scol2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image("..//slr_res_est_course//images//interp_gt_q1.jpg", use_column_width=True)

    gt_options = ["Seleccione la respuesta",
                   "El azul claro es NN, el violeta es OK y el rojo es ID",
                   "El azul claro es NN, el violeta es ID y el rojo es OK",
                   "El azul claro es OK, el violeta es NN y el rojo es ID",
                   "El azul claro es OK, el violeta es ID y el rojo es NN"]

    st.radio("Que lineas en la gt_curve pertenecen a que estimacion?", options=gt_options, key='gg1')
    st.text("Any additional comments?")

    st.markdown("## **Adivina la modelo: Pregunta 2**")
    st.markdown("Usa tu conocimiento adquirido para descifrar el misterio de las imagenes a continuacion.")
    st.markdown("Que sabemos:")
    st.markdown("* ID al cuadrado se usa para una estimacion y OK para otra")
    st.markdown("* Se utilizaron parametros de busqueda identicos.")
    st.markdown("* El variograma tiene un efecto pepita de alrededor de 0,3 y la mayor parte de la variabilidad se explica dentro de unos 20-30 m.")

    st.image("..//slr_res_est_course//images//interp_OK_q2.jpg")
    st.image("..//slr_res_est_course//images//interp_ID_q2.jpg")

    est_options = ["Selecione una respuesta",
                   "La estimacion A es mas variable que la estimacion B. La estimacion A es OK y la estimacion B es ID",
                   "La estimacion B es mas variable que la estimacion B. La estimacion A es OK y la estimacion B es ID",
                   "Ambas estimaciones tienen varianzas iguales ya que usan los mismos datos de muestra. La estimacion A es OK y la estimacion B es ID",
                   "La estimacion B es mas variable que la estimacion A. La estimacion A es ID y la estimacion B es OK",]

    st.radio("Select the correct statement", options=est_options, key='est1')





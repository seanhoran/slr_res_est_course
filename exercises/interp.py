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

    st.markdown("## **Visual Trend Analysis**")
    st.markdown("The figure below is an orthogonal projection of full width intercepts within a narrow vein.")
    st.markdown("Prior to any statistical analysis, it is useful just to look at your data." +
                " Take it for a spin, look to see where high grades are located and what trends you can observe." +
                " When selecting a colour profile, try use a scheme that highlights trends but considers some economic" +
                " criteria too. It is always useful to have one or two colour bins below your cut-off grade." +
                " The last tip is, be consistent with your legend,  make sure the samples and contours/blocks use the" +
                " same colour scheme.")

    df = pd.read_csv(".//data//sim_pts.csv")
    df = df[df.use==1].copy().reset_index(drop=True)
    # fig, ax = plot_samps(df)
    # st.pyplot(fig)
    st.image("..//pdac2021_res_est_course//images//contour.jpg", use_column_width=True)
    
    #-----------------------------------------------------------------------------------------------------------------#
    # Variogram
    # ----------------------------------------------------------------------------------------------------------------#

    st.markdown("## **Variogram Activity**")
    st.markdown("The omni-directional variogram is given in the chart that follows." +
                " Keep in mind that no direction has been chosen and that the range shown will be shorter than" +
                " the longest direction and longer than the shortest direction. Your job is to estimate the range" +
                " in the longest direction given your observations from the plot above.")

    st.image("..//pdac2021_res_est_course//images//interp_var.jpg")

    var_options = ["Select and Answer",
                   "Major = 75m, Semi-Major = 75m",
                   "Major = 125m, Semi-Major = 60m",
                   "Major = 75m, Semi-Major = 100m",
                   "Major = 150m, Semi-Major = 75m"]

    st.radio("What is you estimate of the major and semi major direction ranges?", options=var_options, key='vv1')

    #-----------------------------------------------------------------------------------------------------------------#
    # Set up search ellipse
    # ----------------------------------------------------------------------------------------------------------------#
    st.markdown("## **Search Ellipse Activity**")

    # scol1, scol2 = st.beta_columns((1, 1))
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
    src_options = ["Select an Answer",
                   "Major = 75m, Semi-Major = 75m, Rotated by 90, Min 2 Max 40",
                   "Major = 125m, Semi-Major = 60m, Rotated -60 towards South East, Min 3 Max 12",
                   "Major = 125m, Semi-Major = 60m, Rotated 20 towards South West, Min 2 Max 12",
                   "Major = 150m, Semi-Major = 75m, Min 2 Max 10, No Rotation"]

    st.radio("Select the appropriate search parameters?", options=src_options, key='ss1')

    st.markdown("## **Guess the Model: Question 1**")
    st.markdown("The interpolations given below are Nearest Neighbour (NN), Inverse Distance (ID) and Ordinary Kriging (OK) respectively")
    st.markdown("The curves increasing to the right on the grade tonnage curves are the grades foe each technique at different cut-offs.")
    scol1, scol2 = st.beta_columns((1, 1))
    with scol1:
        st.image("..//pdac2021_res_est_course//images//interp_ests_q1.jpg", use_column_width=True)
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
        st.image("..//pdac2021_res_est_course//images//interp_gt_q1.jpg", use_column_width=True)

    gt_options = ["Select an Answer",
                   "Light blue is NN, purple is OK and red is ID",
                   "Light blue is NN, purple is ID and red is OK",
                   "Light blue is OK, purple is NN and red is ID",
                   "Light blue is OK, purple is ID and red is NN"]

    st.radio("Which lines on the gt_curve belong to which estimate?", options=gt_options, key='gg1')
    st.text("Any additional comments?")

    st.markdown("## **Guess the Model: Question 2**")
    st.markdown("Use your knowledge gained to decipher the mystery of the images below.")
    st.markdown("What we know:")
    st.markdown("* ID squared was used for one estimate and OK for another")
    st.markdown("* Identical search parameters were used")
    st.markdown("* The variogram has nugget of around 0.3 and most of the variability is accounted for within about 20-30m.")

    st.image("..//pdac2021_res_est_course//images//interp_OK_q2.jpg")
    st.image("..//pdac2021_res_est_course//images//interp_ID_q2.jpg")

    est_options = ["Select an Answer",
                   "Estimate A is more variable than estimate B. Estimate A is OK and Estimate B is ID",
                   "Estimate B is more variable than estimate B. Estimate A is OK and Estimate B is ID",
                   "Both estimates have equal variances as they use the same sample data. Estimate A is OK and Estimate B is ID",
                   "Estimate B is more variable than estimate A. Estimate A is ID and Estimate B is OK",]

    st.radio("Select the correct statement", options=est_options, key='est1')





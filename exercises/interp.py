import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import scipy.spatial as spatial
from sklearn.neighbors import KDTree
import warnings
from multiprocessing.pool import ThreadPool as Pool
from matplotlib.patches import Ellipse
warnings.simplefilter("ignore")
from scipy.interpolate import Rbf
import matplotlib as mpl
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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


def pad_matrix(mat, dim=2):
    mat = np.array(mat)
    if dim == 2:
        mat = np.pad(mat, (0, 1), 'constant', constant_values=(1))
        mat[-1, -1] = 0.
    else:
        mat = np.pad(mat, (0, 1), 'constant', constant_values=(1, 1))
    return mat;


def variogram(h, var, nugget):
    gamma = nugget
    for i in range(2):
        gam = (var[i, 0]) * ((3 * h) / (2 * var[i, 1]) - (h ** 3) / (2 * var[i, 1] ** 3))
        gam[h > var[i, 1]] = var[i, 0]
        gamma += gam
    gamma[h == 0] = 0.
    return gamma;


def OK(x, y, var, nugget):
    # x is samples
    # y in blocks
    x = np.array(x)
    y = np.array(y)
    xx = spatial.distance_matrix(x, x)
    xx_gamma = variogram(xx, var, nugget)
    xx_gamma = pad_matrix(xx_gamma)
    xy_gamma = variogram(y, var, nugget)
    xy_gamma = pad_matrix(xy_gamma, dim=1)
    xx_inv = np.linalg.inv(xx_gamma)
    return np.dot(xy_gamma, xx_inv)[:-1];


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

def plot_blocks(block_size, grades, df):
    aniso = (300. + block_size) / (750. + block_size)
    fig, ax = plt.subplots(figsize=(15, 15 * aniso))
    xx, yy = dgrid(block_size)
    extents = (0., 750 + block_size, 0., 300. + block_size)
    ax.imshow(np.reshape(grades, xx.shape), origin='lower', extent=extents, alpha=0.8, cmap=cmap, norm=norm)
    scat = ax.scatter(df.YPT, df.ZPT, c=df.AU_G_T, cmap=cmap, norm=norm, edgecolor="black", s=40)
    cbar = fig.colorbar(scat, ticks=cog)
    cbar.set_label('Au g/t', rotation=0)
    plt.xlim((0, 750))
    plt.ylim((0, 300))
    plt.xlabel('X')
    plt.ylabel('Y')
    return fig, ax;


def dgrid(block_size=5.):
    x = np.arange(0., 750. + block_size, block_size)
    y = np.arange(0., 300. + block_size, block_size)
    return np.meshgrid(x, y);

def gtcurve(grades, block_size):

    cogs = [0., 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    grades[grades<0.] = 0.
    grades[np.isnan(grades)]=-99.
    bt = block_size*2.7

    g = []
    t = []
    c = []

    for cog in cogs:
        filt = grades>cog
        if np.sum(filt) > 0:
            g.append(np.average(grades[filt]))
            t.append(np.sum(filt)*bt)
            c.append(cog)

    return pd.DataFrame({'COG':c, 'Tonnes':t, 'Grade':g});

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
    st.image(".//images//contour.jpg", use_column_width=True)
    xx = spatial.distance_matrix(df[['YPT', 'ZPT']], df[['YPT', 'ZPT']])
    xx = np.array(xx)

    #-----------------------------------------------------------------------------------------------------------------#
    # Variogram
    # ----------------------------------------------------------------------------------------------------------------#

    st.markdown("## **Variogram Activity**")
    st.markdown("The omni-directional variogram is given in the chart that follows." +
                " Keep in mind that no direction has been chosen and that the range shown will be shorter than" +
                " the longest direction and longer than the shortest direction. Your job is to estimate the range" +
                " in the longest direction given your observations from the plot above.")

    g1, g2 = np.meshgrid(df.AU_G_T, df.AU_G_T)
    col1, col2, col3  = st.beta_columns((1,1,1))

    with col1:
        st.markdown('#### Experimental Variogram')
        lag_dist = st.slider('Lag Distance', min_value=5., max_value=50., value=10., step=5.,key='var_lag')
        vartype = st.selectbox('Select Experimental Variogram Type',
                               options=['Traditional Variogram', 'Correlogram'],
                               index=0)
    with col2:
        st.markdown('#### Variogram Model (Variances)')
        nugget = st.slider('Nugget Effect',min_value=0.0, max_value=1.0, value=0.1, step=0.05)
        c1 = st.slider('C1', min_value=0.0, max_value=1.0-nugget, value=0.0, step=0.05)
        c2 = 1.0 - (c1 + nugget)
    with col3:
        st.markdown('#### Variogram Model (Ranges)')
        r1 = st.slider('Range s1', min_value=0.0, max_value=200.0, value=10., step=5., key='k1')
        r2 = st.slider('Range s2', min_value=0.0, max_value=200.0, value=10., step=5., key='k2')

    var = np.array([[c1, r1], [c2, r2]])
    h = np.arange(0.,200., 1.)
    vmod = variogram(h, var, nugget)
    lags = np.arange(lag_dist, 200., lag_dist)
    gammas = np.zeros(len(lags))
    numpairs = np.zeros(len(lags))
    fig, ax = plt.subplots()

    for i, lag in enumerate(lags):
        filt = (xx>=lag-lag_dist*0.75)&(xx<lag+lag_dist*0.75)
        sq_dif = np.sum((g1[filt]-g2[filt])**2)
        m = np.average(g1[filt])
        s = np.std(g1[filt])
        ns = np.sum(filt)
        numpairs[i] = ns

        if vartype == 'Traditional Variogram':
            gammas[i] = sq_dif/(2*float(np.sum(filt))) / np.var(df.AU_G_T)
        else:
            gammas[i] = (np.sum(g1[filt]*g2[filt]) - ns*m**2)/(ns*s**2)
            gammas[i] = 1.0 - gammas[i]
        ax.annotate(str(ns), (lag, gammas[i]+0.05), size=5)

    ax.bar(lags, numpairs/np.max(numpairs), width=lag_dist/2)
    ax.plot(lags, gammas, '-or', markeredgecolor='k', markersize=4, markeredgewidth=0.5)
    ax.plot(h, vmod, '-g', markeredgecolor='k', markersize=4, markeredgewidth=0.5)

    plt.xlim((0, 200))
    plt.ylim((0, 1.5))
    ax.plot([0., 200], [1.0, 1.0], '--k')
    plt.xlabel("Separation Distance/Lag Distance")
    plt.ylabel("Gamma")
    st.pyplot(fig)

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
    src_options = ["Select and Answer",
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
        st.image(".//images//interp_ests_q1.jpg", use_column_width=True)
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
        st.image(".//images//interp_gt_q1.jpg", use_column_width=True)

    gt_options = ["Select and Answer",
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

    st.image(".//images//interp_OK_q2.jpg")
    st.image(".//images//interp_ID_q2.jpg")

    est_options = ["Select and Answer",
                   "Estimate A is more variable than estimate B. Estimate A is OK and Estimate B is ID",
                   "Estimate B is more variable than estimate B. Estimate A is OK and Estimate B is ID",
                   "Both estimates have equal variances as they use the same sample data. Estimate A is OK and Estimate B is ID",
                   "Estimate B is more variable than estimate A. Estimate A is ID and Estimate B is OK",]

    st.radio("Select the correct statement", options=est_options, key='est1')





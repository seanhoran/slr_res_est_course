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

@st.cache

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

def plot_samps(df):
    aniso = (300.) / (750.)
    fig, ax = plt.subplots(figsize=(15, 15 * aniso))
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
    st.markdown("The figure below is an orthogonal projection of full width intercepts within a narrow vein.")
    st.markdown("## **Visual Trend Analysis**")
    df = pd.read_csv("..//pdac2021_res_est_course//data//sim_pts.csv")
    df = df[df.use==1].copy().reset_index(drop=True)
    fig, ax = plot_samps(df)
    st.pyplot(fig)
    xx = spatial.distance_matrix(df[['YPT', 'ZPT']], df[['YPT', 'ZPT']])
    xx = np.array(xx)

    #-----------------------------------------------------------------------------------------------------------------#
    # Variogram
    # ----------------------------------------------------------------------------------------------------------------#

    st.markdown("## **Variogram**")
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
        c1 = st.slider('C1', min_value=0.0, max_value=1.0, value=0.2, step=0.05)
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

    #-----------------------------------------------------------------------------------------------------------------#
    # Set up search ellipse
    # ----------------------------------------------------------------------------------------------------------------#
    st.markdown("## **Search Ellipse**")

    scol1, scol2 = st.beta_columns((1, 1))
    with scol1:
        st.markdown('#### Ellipse Shape')
        rot = st.number_input('Pick a Rotation (-360 to 360)', min_value=-360., max_value=360., value=0., step=5.)
        rot = (360. - rot)
        srange_major = st.number_input('Major Axis Range', min_value=10., max_value=500., value=100., step=5.)
        srange_minor = st.number_input('Minor Axis Range', min_value=10., max_value=500., value=100., step=5.)
    with scol2:
        st.markdown('#### Sample Selection')
        min_samps = st.number_input("Minimum Samples", min_value=1, max_value=40, value=2, step=1)
        max_samps = st.number_input("Maximum Samples", min_value=1, max_value=40, value=10, step=1)
    fig, ax = plot_samps(df)
    e = Ellipse(xy=[350, 150], width=srange_minor * 2, height=srange_major * 2, angle=rot, linewidth=2)
    ax.add_artist(e)
    e.set_facecolor('None')
    e.set_edgecolor('black')
    st.pyplot(fig)

    #-----------------------------------------------------------------------------------------------------------------#
    # Block modelling parameters
    # ----------------------------------------------------------------------------------------------------------------#

    st.markdown("## **Additional Parameters**")

    bcol1, bcol2 = st.beta_columns((1, 1))
    with bcol1:
        block_size = st.number_input('Block Size', min_value=5., max_value=100., value=5., step=5.)
    with bcol2:
        id_exponent = st.number_input('ID Exponent', min_value=0.0, max_value=10.0, value=2., step=0.1)

    if st.button("Run Interpolation"):

        xx, yy = dgrid(block_size)
        grid = np.array([xx.flatten(), yy.flatten()]).transpose()
        points = np.array(df.loc[:, ['YPT', 'ZPT']])

        AUID = np.zeros(len(grid))
        AUNN = np.zeros(len(grid))
        AUOK = np.zeros(len(grid))
        NDIST = np.zeros(len(grid))

        AUID[:] = np.nan
        AUID[:] = np.nan
        AUNN[:] = np.nan
        AUOK[:] = np.nan
        NDIST[:] = np.nan

        # rotate
        # grid2 = grid.copy()
        grid = rotate(grid, rot)
        points = rotate(points, rot)
        # apply anisotropy
        grid[:, 0] *= srange_major / srange_minor
        points[:, 0] *= srange_major / srange_minor

        point_tree = KDTree(points)
        idx, dist = point_tree.query_radius(grid, r=srange_major, return_distance=True, sort_results=True)

        for i, ix in enumerate(idx):
            mx = max_samps
            if len(ix) <= mx:
                mx = len(ix)
            dists = dist[i][:mx]
            grades = np.array(df.loc[ix[:mx], 'AU_G_T'])
            if len(ix) >= min_samps:
                AUID[i] = (np.average(grades, weights=1.0 / dists ** id_exponent))
                AUNN[i] = (grades[0])
                NDIST[i] = (dists[0])
                OK_weights = OK(x=points[ix[:mx]], y=dists, var=var, nugget=nugget)
                AUOK[i] = (np.sum(OK_weights * grades))


        fig, ax = plot_blocks(block_size, AUNN, df)
        plt.title("Nearest Neighbour Interpolation")
        st.pyplot(fig)

        fig, ax = plot_blocks(block_size, AUID, df)
        plt.title("Inverse Distance Interpolation")
        st.pyplot(fig)

        fig, ax = plot_blocks(block_size, AUOK, df)
        plt.title("Ordinary Kriging Interpolation")
        st.pyplot(fig)

        st.write("Grade Tonnage Curve:")
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        curve = gtcurve(AUNN, block_size)
        fig.add_trace(
            go.Scatter(x=curve.COG, y=curve.Tonnes, name="NN Tonnes"),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(x=curve.COG, y=curve.Grade, name="NN Grade"),
            secondary_y=True,
        )

        curve = gtcurve(AUID, block_size)
        fig.add_trace(
            go.Scatter(x=curve.COG, y=curve.Tonnes, name="ID Tonnes"),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(x=curve.COG, y=curve.Grade, name="ID Grade"),
            secondary_y=True,
        )

        curve = gtcurve(AUOK, block_size)
        fig.add_trace(
            go.Scatter(x=curve.COG, y=curve.Tonnes, name="OK Tonnes"),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(x=curve.COG, y=curve.Grade, name="OK Grade"),
            secondary_y=True,
        )

        fig.update_xaxes(title_text="Cut-off (Au g/t)")
        fig.update_yaxes(title_text="Tonnes", secondary_y=False)
        fig.update_yaxes(title_text="Grade (Au g/t)", secondary_y=True)

        st.plotly_chart(fig)

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.tri as tri
import numpy as np
import pandas as pd
import math
from sigfig import round

# A) "TwoDim_Contour" : plots 2D contour plot, using a data in the form [[A1, B1, C1], [A2, B2, C2], ...]. Also plots a 2D plot of all of the raw data, for comparison/check of the contours.

def TwoDim_Contour(yData, xData, yMax, yMin, xMax, xMin, NumLevels, Colour, yLabel, xLabel, ContLines, WhiteCutoff=0, ContourValues, FigureSavePath, FileName):
    """
    ** yData : Data to be plotted in the y-axis, in the form of a list [A1, A2, A3, .. An]
    ** xData : Data to be plotted in the x-axis, in the form of a list [B1, B2, B3, .. Bn]
    ** yMax : Coordinate for y-axis maximum of plot.
    ** yMin : Coordinate for y-axis minimum of plot.
    ** xMax : Coordinate for x-axis maximum of plot.
    ** xMin : Coordinate for x-axis minimum of plot.
    ** NumLevels : Number of contour levels.
    ** ContLines : Either 'y' (yes) or 'n' (no), plot or not to plot the lines seperating contour levels.
    ** WhiteCutoff : A value of data density used as the maximum density cutoff for colouring contour levels white (to make a white background). Default value is zero(0), which can be adjusted by trial-and-error (or by reading contour line values with ContourValues='y') to find an appropriate value such that the background is white.
    ** ContourValues : Either 'y' (yes) or 'n' (no), plot or not to plot the values defining each contour level (value is density value). Requires ContLines='y'.
    ** Colour : In quotations (such as 'Blues') the colour of the contour plot. Options available according to 'cmap' of matplotlib (https://matplotlib.org/stable/tutorials/colors/colormaps.html).
    ** yLabel : In quotations ('test' for example), the text to be displayed in the y-axis of the plot.
    ** xLabel : In quotations ('test' for example), the text to be displayed in the x-axis of the plot.
        ** ContLines : Either 'y' (yes) or 'n' (no) to display lines of each contour (as opposed to just the colour contours).
    ** FigureSavePath : Path to folder location where figures should be saved. Must be in single quotations, example : '/Volumes/Samsung_T5/Experiment categories/Laser/Figures/'
    ** FileName : General name of files to be saved. Must be in single quotations, example : 'TEST_DataSet01'
    """
    
    # Peform the kernel density estimate
    xx, yy = np.mgrid[xMin:xMax:300j, yMin:yMax:300j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([xData, yData])

    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, xx.shape)

    fig, ax = plt.subplots()
    
    # Contour shading:
    cfset = ax.contourf(xx, yy, f, NumLevels, cmap=Colour)
    # Making a white background for contour levels below the value specified by the user ('WhiteCutoff')
    cfset.cmap.set_under('w')
    cfset.set_clim(WhiteCutoff)
    # Contour lines:
    if ContLines =='y':
        cset = ax.contour(xx, yy, f, NumLevels, colors='k', alpha=1, linewidths = 0.5, linestyles = '-')
        # Label plot
        if ContourValues == 'y':
            ax.clabel(cset, inline=1, fontsize=5)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_xlim(xMin, xMax)
    ax.set_ylim(yMin, yMax)
    fig.savefig(FigureSavePath + FileName + '.pdf')

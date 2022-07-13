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

def TwoDim_Contour(yData, xData, yMax, yMin, xMax, xMin, NumLevels, Colour, yLabel, xLabel, ContLines, FigureSavePath, FileName):
    """
    ** yData : Data to be plotted in the y-axis, in the form of a list [A1, A2, A3, .. An]
    ** xData : Data to be plotted in the x-axis, in the form of a list [B1, B2, B3, .. Bn]
    ** yMax : Coordinate for y-axis maximum of plot.
    ** yMin : Coordinate for y-axis minimum of plot.
    ** xMax : Coordinate for x-axis maximum of plot.
    ** xMin : Coordinate for x-axis minimum of plot.
    ** NumLevels: Number of contour levels.
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

    fig51, ax51 = plt.subplots()
    
    # Contour shading:
    cfset = ax51.contourf(xx, yy, f, NumLevels, cmap=Colour)
## Or kernel density estimate plot instead of the contourf plot
#ax.imshow(np.rot90(f), cmap='Blues', extent=[xmin, xmax, ymin, ymax])
# Contour lines:
    if ContLines =='y':
        cset = ax51.contour(xx, yy, f, NumLevels, colors='k', alpha=1, linewidths = 0.5, linestyles = '-')
    # Label plot
#    ax51.clabel(cset, inline=1, fontsize=5)
    ax51.set_xlabel(xLabel)
    ax51.set_ylabel(yLabel)
    ax51.set_xlim(xMin, xMax)
    ax51.set_ylim(yMin, yMax)
    fig51.savefig(FigureSavePath + FileName + '.pdf')

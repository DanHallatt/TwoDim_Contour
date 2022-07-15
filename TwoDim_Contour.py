import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import matplotlib.tri as tri
import numpy as np
import pandas as pd
import math
from sigfig import round
from statistics import mean
import scipy.stats as st

# A) "TwoDim_Contour" : plots 2D contour plot, using a data in the form [[A1, B1, C1], [A2, B2, C2], ...]. Also plots a 2D plot of all of the raw data, for comparison/check of the contours.

def TwoDim_Contour(yData, xData, yMax, yMin, xMax, xMin, NumLevels, Colour, ContourValues, ContLines, ContColourFill, DataPointDisp, yLabel, xLabel, FigureSavePath, FileName):
    """
    ** yData : Data to be plotted in the y-axis, in the form of a list of list [ [A11, A12, ... A1n], [A21, A22, ... A2n] , ... [Am1, Am2, ... Amn] ], where n is the numer of datapoint in a given dataset and m is the number of datasets to plot individually. Even if m = 1, data must be in form of [ [A11, A12, .. A1n] ], where dataX[0] = [A11, A12, .. A1n] and not = A11.
    ** xData : Data to be plotted in the x-axis, in the form of a list of lists [ [A11, A12, ... A1n], [A21, A22, ... A2n] , ... [Am1, Am2, ... Amn] ], where n is the numer of datapoint in a given dataset and m is the number of datasets to plot individually. Even if m = 1, data must be in form of [ [B11, B12, .. B1n] ], where dataX[0] = [B11, B12, .. B1n] and not = B11.
            
        !!! NOTE !!! : Data cannot contain 'NaN' values. Must be cleaned prior to input in this function (or this function modified to clean data by removing them).
    
    ** yMax : Coordinate for y-axis maximum of plot.
    ** yMin : Coordinate for y-axis minimum of plot.
    ** xMax : Coordinate for x-axis maximum of plot.
    ** xMin : Coordinate for x-axis minimum of plot.
    ** Colour : In quotations a list of the colour of the contour plots in form of ['Blues', 'Reds', ect..]. Number of colours defined must = m. Options available according to 'cmap' of matplotlib (https://matplotlib.org/stable/tutorials/colors/colormaps.html). Still required to be defined even if ContColourFill == 'n'.
    ** ContLines : Either 'y' (yes) or 'n' (no), plot or not to plot the lines seperating contour levels.
    ** ContourValues : Either 'y' (yes) or 'n' (no), to plot the values defining each contour level (value is density value). Requires ContLines='y'.
    ** ContColourFill : Either 'y' (yes) or 'n' (no), to fill contour values with the colours defined in 'Colour' list.
    ** yLabel : In quotations ('test' for example), the text to be displayed in the y-axis of the plot.
    ** xLabel : In quotations ('test' for example), the text to be displayed in the x-axis of the plot.
        ** ContLines : Either 'y' (yes) or 'n' (no) to display lines of each contour (as opposed to just the colour contours).
    ** FigureSavePath : Path to folder location where figures should be saved. Must be in single quotations, example : '/Volumes/Samsung_T5/Experiment categories/Laser/Figures/'
    ** FileName : General name of files to be saved. Must be in single quotations, example : 'TEST_DataSet01'
    """
    
    ContourLabelTextSize = 0.5
    ContourLineThickness = 0.4
    ContourLineStyle = '-'
    DataPointSize = 3
    
    # Peform the kernel density estimate
    xx, yy = np.mgrid[xMin:xMax:1000j, yMin:yMax:1000j]
    positions = np.vstack([xx.ravel(), yy.ravel()])
    
    fig, ax = plt.subplots()
    for r in range(0,len(xData)):
        values = np.vstack([xData[r], yData[r]])
        kernel = st.gaussian_kde(values)
        f = np.reshape(kernel(positions).T, xx.shape) #Third dimension = 'height' of contours, which is the data-density in x,y-space of.
    
        if ContColourFill == 'y':
            cfset = ax.contourf(xx, yy, f, NumLevels, cmap=Colour[r], locator = ticker.MaxNLocator(prune = 'lower')) # Colours the contour levels
        if ContLines =='y':
            cset = ax.contour(xx, yy, f, NumLevels, colors='k', alpha=1, linewidths=ContourLineThickness, linestyles=ContourLineStyle) # Plots contour lines.
            if ContourValues == 'y':
                ax.clabel(cset, inline=1, fontsize=ContourLabelTextSize) # Labels the contour levels.
        if DataPointDisp == 'y':
            ax.scatter(xData[r], yData[r], color='black', alpha=1, s=DataPointSize) # Includes datapoints over-printed on the contour plot. Usually used to check the appropriatness of the contour levels.
    
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_xlim(xMin, xMax)
    ax.set_ylim(yMin, yMax)
    fig.savefig(FigureSavePath + FileName + '.pdf')

# -*- coding: utf-8 -*-
# =============================================================================
# MIT License
#
# Copyright (c) 2018 Andrés Bernardo
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# =============================================================================

##=============================================================================
## """ locateBubbleOrigin.py """ :
##     Mark the origin of the experimental data
##         based on various techniques on a 2D plot,
##             where Z data is represented with a colormap;
##=============================================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def locateBubbleOrigin(dicFileInput, plotFilePath2D, plotFilePath3D):
    
    ## Note: code for data point annotations have been commented out,
    ## but were left within code for future possible improvements
    
    ##=========================================================================
    ## utilizing np.loadtxt  
    ## see "reduceFileFormatSizeDemo.py" file
    ##=========================================================================
    values = np.loadtxt(dicFileInput, skiprows = 3)
    
    ##=========================================================================
    ## removing data points where Z-displacement is 0mm
    ## see "identifySpecimenDemo.py" file
    ##=========================================================================
    values = values[ (values[:,2] != 0) | (values[:,5] != 0) ]
    
#    print ('\nThere are')
#    print (len(values))
#    print ('data entries when zero-displacement points are removed')
    
    X = values[:,0]
    Y = values[:,1]
    Z = values[:,2]
    dispX = values[:,3]
    dispY = values[:,4]
    dispZ = values[:,5]
    
    # the displaced nodes are equal to "X+dispX", "Y+dispY", "Z+dispZ"
    finalX = X+dispX
    finalY = Y+dispY
    finalZ = Z+dispZ
     
    ##=========================================================================
    ## solving for maximum & minimum values
    ##=========================================================================
    
    # find the minimum and maximum values in the x- and y-directions
    xMin = min(finalX)
    xMax = max(finalX) 
    yMin = min(finalY)
    yMax = max(finalY)
    
    # find the x & y values associated with each extreme
    y_coordinate_of_xMax = finalY[ finalX.argmax() ]
    y_coordinate_of_xMin = finalY[ finalX.argmin() ]
    x_coordinate_of_yMax = finalX[ finalY.argmax() ]
    x_coordinate_of_yMin = finalX[ finalY.argmin() ]
    
    # include x & y values associated with maximum z
    x_coordinate_of_zMax = finalX[ finalZ.argmax() ]
    y_coordinate_of_zMax = finalY[ finalZ.argmax() ]
    
    
    #==========================================================================
    # 2D plot
    #==========================================================================    
    fig2D = plt.figure()
    ax2D = fig2D.add_subplot(111)    
    map2D = ax2D.scatter(finalX, finalY, c=finalZ, s=8, edgecolor='')
    
    # include the colorbar to illustrate Z-values in 2D plot
    plt.colorbar(map2D, ax=ax2D, format='%.0f mm')
    
    # label axes
    plt.xlabel('X+dispX (mm)')
    plt.ylabel('Y+dispY (mm)')
    plt.title('Z-displacement, 2D representation')
    
    # include grid; low alpha value for good visibility
    ax2D.grid(True, alpha = 0.2, ls='dotted')
    
    # x-axis and y-axis
    ax2D.axhline(0, color='k', lw=0.5, ls='dashed')
    ax2D.axvline(0, color='k', lw=0.5, ls='dashed')
    
    ## annotate origin [x = 0 mm, y = 0 mm]
#    plt.scatter(0, 0, c='k', s=10, edgecolor='')
#    ax2D.annotate('(x=0, y=0)',
#                 size=7,
#                 xy = [0, 0],
#                 xytext=(5, -15),
#                 textcoords = 'offset pixels')
    
    # plot & annotate maximum Z value
    ax2D.scatter(x_coordinate_of_zMax, y_coordinate_of_zMax, \
                        s=100, marker='s', facecolors='none', edgecolors='k', \
                        label='Z$_{raw Max}$ = (%.2f, %.2f) mm' \
                        %(x_coordinate_of_zMax, y_coordinate_of_zMax ))
#    ax2D.annotate('Z$_{max}$', 
#                 size=7,
#                 xy = [x_coordinate_of_zMax, y_coordinate_of_zMax],
#                 xytext=(-20, -15),
#                 textcoords = 'offset pixels')
    
    # plot the x & y extrema 
    ax2D.scatter(xMax, y_coordinate_of_xMax, c='orange', marker='x', s=50)
    ax2D.scatter(xMin, y_coordinate_of_xMin, c='orange', marker='x', s=50)
    ax2D.scatter(x_coordinate_of_yMax, yMax, c='orange', marker='x', s=50)
    ax2D.scatter(x_coordinate_of_yMin, yMin, c='orange', marker='x', s=50)
    
    # include perpendicular lines marking the extrema locations
    ax2D.axvline(x_coordinate_of_yMax, color='orange', lw=0.75, ls='dashdot')
    ax2D.axvline(x_coordinate_of_yMin, color='orange', lw=0.75, ls='dashdot')
    ax2D.axhline(y_coordinate_of_xMax, color='orange', lw=0.75, ls='dashdot')
    ax2D.axhline(y_coordinate_of_xMin, color='orange', lw=0.75, ls='dashdot')
    
    # plot lines connecting max & min in the x & y directions
    ax2D.plot([xMax,xMin],
             [y_coordinate_of_xMax,y_coordinate_of_xMin],
             c='r',
             lw=.75,
             ls='dashed')
    
    ax2D.plot([x_coordinate_of_yMax,x_coordinate_of_yMin],
             [yMax,yMin],
             c='r',
             lw=.75,
             ls='dashed')
    
    # calculate point of intersection
    slopeH = (y_coordinate_of_xMin - y_coordinate_of_xMax)/(xMin - xMax)
    slopeV = (yMin - yMax)/(x_coordinate_of_yMin - x_coordinate_of_yMax)
    
    bV = yMax - slopeV*x_coordinate_of_yMax
    bH = y_coordinate_of_xMax - slopeH*xMax
    
    x_intersect = (bH - bV)/(slopeV - slopeH)
    y_intersect = slopeV*x_intersect + bV
    
    # plot & annotate the intersection
    ax2D.scatter(x_intersect, y_intersect, \
                 c='r', s=25, \
                 label='Z$_{intersect}$ = (%.2f, %.2f) mm' \
                     %(x_intersect, y_intersect))
#    ax2D.annotate('(%.2f, %.2f)' %(x_intersect, y_intersect), 
#                 size=7,
#                 color='k',
#                 xy = [x_intersect, y_intersect],
#                 xytext=(120, -75),
#                 textcoords = 'offset pixels',
#                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    
    ##=========================================================================
    ## 3D plot (plot of the surfaces fits of Disp Z)
    ##=========================================================================    
    from doubleVander import doubleVander
    from polySurfaceFit import polySurfaceFit
    from circleFit import circleFit

    x_center, y_center, radius = circleFit(finalX, finalY)
    
    cDispZ, rDispZ, fittedDispZ = \
        polySurfaceFit(finalX, finalY, finalZ, 4)
    
    X,Y = np.meshgrid(np.linspace(min(finalX), max(finalX), 50), \
                      np.linspace(min(finalY), max(finalY), 50))
    
    Axy = doubleVander(X.flatten(),Y.flatten(),4)
    
    ZZ = np.dot(Axy,cDispZ)
    Z = ZZ.reshape(X.shape)
    
    #   3D plot of the X, Y, disp Z
    fig3D = plt.figure()
    ax3D = fig3D.add_subplot(111, projection='3d')
    
    ax3D.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)
    
    ax3D.scatter(finalX, finalY, finalZ, zdir='z', \
                 s=.2,c='b',edgecolor='', depthshade=False)
    
    ax3D.set_aspect('equal')
    
    # suitable axes limits were determined to encompass all data for all
    # bubble tests; the hard-coded limits below are a result of inspecting
    # the resulting fitted graphs from matplotlib's default fitting behavior...
    # ...these limits were selected as a result of the above:
    ax3D.set_xlim3d(-120, 120)
    ax3D.set_ylim3d(-120, 120)
    ax3D.set_zlim3d(-120, 180)
    # (there may be some cut-offs from hyperbolic-shaped polynomial fit curves)
    
    ax3D.set_xlabel('X (mm)')
    ax3D.set_ylabel('Y (mm)')
    ax3D.set_zlabel('Z (mm)')
    
    ax3D.set_title('3D plot of Disp Z over the XY bubble position' + \
                   '\n(with polynomial fit)')
    
    #==========================================================================
    # Marking the highest Z from the fitted polynomial on 2D plot
    #
    # (This method has been commented out; for middle/high pressure data,
    # the max Z value of the polyfit was useful, because the curve of the   
    # polyfit was primarily "parabolic", so Z_polyfit would be at the
    # "top of the dome". However, low-pressure data resulted in curves  
    # that were primarily "hyperbolic", which lead to Z_polyfit lying upon a
    # "corner" of the resulting curve.) 
    #==========================================================================
#    x_polyfit, y_polyfit = np.unravel_index(Z.argmax(), Z.shape)   
#        
#    ax3D.scatter(X[x_polyfit, y_polyfit], \
#                 Y[x_polyfit, y_polyfit], \
#                 Z[x_polyfit, y_polyfit], \
#                 c='k', s=100, edgecolor='', marker='+')
#    
#    ax2D.scatter(X[x_polyfit, y_polyfit], \
#                 Y[x_polyfit, y_polyfit], \
#                 c='k', s=100, edgecolor='', marker='+', \
#                 label='Z$_{polyfit}$ = (%.2f, %.2f) mm' \
#                     %(X[x_polyfit,y_polyfit], Y[x_polyfit,y_polyfit]))
##    ax2D.annotate('Z$_{polyfit}$ = (%.2f, %.2f)' \
##                      %(X[x_coord,y_coord], Y[x_coord,y_coord]), \
##                 size=7,
##                 xy = [X[x_coord,y_coord], Y[x_coord,y_coord]],
##                 xytext=(-20, 15),
##                 textcoords = 'offset pixels',
##                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    
    #==========================================================================
    # Marking the median X & median Y from the fitted polynomial on 2D plot
    #==========================================================================   
    x_median = np.median(X)
    y_median = np.median(Y)
    
    ax2D.scatter(x_median, \
                 y_median, \
                 c='k', s=200, edgecolor='', marker='+', \
                 label='Z$_{poly XY median}$ = (%.2f, %.2f) mm' \
                     %(x_median, y_median))   
    
    # perhaps we can look at the median from the raw data as well??
    x_median = np.median(finalX)
    y_median = np.median(finalY)    
    ax2D.scatter(x_median, \
                 y_median, \
                 s=200, edgecolors='k', marker='^', facecolors='none', \
                 label='Z$_{raw XY median}$ = (%.2f, %.2f) mm' \
                     %(x_median, y_median)) 
    
    #==========================================================================
    # Marking center derived from circleFit function
    #==========================================================================
    ax2D.scatter(x_center, y_center, \
                 s=200, marker='o', facecolors='none', edgecolors='k', \
                 label='Z$_{circlefit}$ = (%.2f, %.2f) mm' \
                     %(x_center, y_center))
#    ax2D.annotate('Z$_{circlefit}$ = (%.2f, %.2f)' %(x_center, y_center), 
#                 size=7,
#                 xy = [x_center, y_center],
#                 xytext=(45, 40),
#                 textcoords = 'offset pixels',
#                 arrowprops=dict(facecolor='white', arrowstyle='->'))
    
    #==========================================================================
    # Resize 2D figure, generate legend, and show and/or save plots 
    #==========================================================================
    fig2D.set_size_inches(np.array([10,10]))
    ax2D.set_aspect('equal')
    ax2D.xaxis.set_ticks(np.arange(-100, 125, 25))
    ax2D.yaxis.set_ticks(np.arange(-100, 125, 25))
    
    ax2D.legend(fancybox=True, fontsize='small', loc='lower right', \
                markerscale=0.5)
    
#    fig2D.show()    
    fig2D.savefig(plotFilePath2D, bbox_inches='tight', dpi=200)
    plt.close(fig2D)

    fig3D.set_size_inches(np.array([6,6]))
#    fig3D.show()
    fig3D.savefig(plotFilePath3D, bbox_inches='tight', dpi=200)
    plt.close(fig3D)

##=============================================================================

###############################################################################
    
# =============================================================================
# locatebubbleOrigin.py loop
# =============================================================================

plt.ioff()
## used when running locateBubbleOrigin.py in the following loop;
## this will help suppress figure output (see plt.close() commands above)

import os
import os.path as path
import glob

datFolderNameList = \
    [ \
    'C:\\temp\Blue_PVC_Valmex_BubbleTest00',\
    'C:\\temp\Blue_PVC_Valmex_BubbleTest01',\
    'C:\\temp\Blue_PVC_Valmex_BubbleTest02',\
    'C:\\temp\Blue_PVC_Valmex_BubbleTest03',\
    'C:\\temp\Black_PVC_Cape_Coaters_BubbleTest01',\
    'C:\\temp\Black_PVC_Cape_Coaters_BubbleTest02',\
    'C:\\temp\Black_PVC_Cape_Coaters_BubbleTest03',\
    'C:\\temp\Black_PVC_Cape_Coaters_BubbleTest04' \
    ]

for line in datFolderNameList :

    baseName = path.basename(line)
    plotFolderName2D = baseName + '_origin2Dplots'
    plotFolderPath2D = path.normpath(path.join('C:\\temp', plotFolderName2D))
    plotFolderName3D = baseName + '_poly3Dplots'
    plotFolderPath3D = path.normpath(path.join('C:\\temp', plotFolderName3D)) 
       
    os.makedirs(plotFolderPath2D)
    os.makedirs(plotFolderPath3D)

    line = path.join(line, '*.dat')
    
    datList = glob.glob(line)    
    
    for line in datList:
        plotFilePath = path.splitext(path.basename(line))[0]
        plotFilePath = baseName + '_' + plotFilePath
        plotFilePath2D = plotFilePath + '_origin2Dplot.png'
        plotFilePath2D = path.join(plotFolderPath2D, plotFilePath2D)
        plotFilePath3D = plotFilePath + '_poly3Dplot.png'
        plotFilePath3D = path.join(plotFolderPath3D, plotFilePath3D)
        locateBubbleOrigin(line, plotFilePath2D, plotFilePath3D)
#        print(line)
#        print(plotFilePath2D)
#        print(plotFilePath3D)
#    print('\n\n')
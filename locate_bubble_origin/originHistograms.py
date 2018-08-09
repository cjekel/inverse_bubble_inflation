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
## """ originHistograms.py """ :
##     Develop histograms for origin X & Y coordinates
##          based on 4 origin-locating methods from locateBubbleOrigin.py:
##               ZcircleFit, Zintersect, ZrawXYmedian, ZpolyXYmedian
##               (Zmax is not the best origin choice by visual inspection)
##=============================================================================

from time import time

t0 = time()

import os
import os.path as path
import numpy as np
import matplotlib.pyplot as plt
import glob
from circleFit import circleFit

import seaborn as sns

###############################################################################
def generateHistogramFigure(origin_CircleFit_data,
                            origin_Intersect_data,
                            origin_RawMedian_Data,
                            origin_PolyMedian_Data,
                            titleString,
                            dicFolderInput,
                            histogramFolder):
    fig = plt.figure()
    fig.set_size_inches(np.array([8.8,6]))
    fig.suptitle(titleString, fontsize=11)
    
    ax_circleFit = fig.add_subplot(221)
    ax_circleFit.set_title('CircleFit', fontsize='small')
#    ax_circleFit.hist(x = origin_CircleFit_data, \
#                      bins = 10,                 \
#                      alpha= 0.75,               \
#                      facecolor = 'blue',        \
#                      edgecolor = 'black')      
    sns.distplot(a = origin_CircleFit_data, \
                 hist = True,               \
                 bins = 10,                 \
                 color = 'blue')
            
    ax_intersect = fig.add_subplot(222)
    ax_intersect.set_title('Intersection', fontsize='small')
#    ax_intersect.hist(x = origin_Intersect_data, \
#                      bins = 10,                 \
#                      alpha= 0.75,               \
#                      facecolor = 'red',         \
#                      edgecolor = 'black')    
    sns.distplot(a = origin_Intersect_data, \
                 hist = True,               \
                 bins = 10,                 \
                 color = 'red')
    
    ax_rawMedian = fig.add_subplot(223)
    ax_rawMedian.set_title('Raw Median', fontsize='small')
#    ax_rawMedian.hist(x = origin_RawMedian_Data, \
#                      bins = 10,                 \
#                      alpha= 0.75,               \
#                      facecolor = 'green',       \
#                      edgecolor = 'black')
    sns.distplot(a = origin_RawMedian_Data, \
                 hist = True,               \
                 bins = 10,                 \
                 color = 'green')
    
    
    ax_polyMedian = fig.add_subplot(224)
    ax_polyMedian.set_title('PolyFit Median', fontsize='small')
#    ax_polyMedian.hist(x = origin_PolyMedian_Data, \
#                       bins = 10,                  \
#                       alpha =0.75,                \
#                       facecolor = 'yellow',       \
#                       edgecolor = 'black')   
    sns.distplot(a = origin_PolyMedian_Data,
                 hist = True,               \
                 bins = 10,                 \
                 color = 'yellow')
    
    
    fig.tight_layout()
    fig.subplots_adjust(top=0.90)


    ##=========================================================================
    ##    Save .png files of histograms here
    ##=========================================================================    
    plotFile = path.normpath( \
                   path.join(histogramFolder, \
                             path.split(dicFolderInput)[1]+'_Histogram.png'))
    
    plt.savefig(plotFile, bbox_inches='tight', dpi=100)
#    fig.show()
    plt.close(fig)

###############################################################################
def originHistograms(dicFolderInput, histogramFolder, originNPYfolder):
        
    dicFolderInput = path.normpath(dicFolderInput)
    
    baseName = path.basename(dicFolderInput)
    
    datFileList = glob.glob(path.join(dicFolderInput, '*.dat'))
    
    plotTitleX = baseName + ': Origin X-Values (mm)'
    plotTitleY = baseName + ': Origin Y-Values (mm)'

    for datFile in datFileList:
        values = np.loadtxt(datFile, skiprows = 3)
        values = values[ (values[:,2] != 0) | (values[:,5] != 0) ] 
        # from previous scripts:
#        X = values[:,0]
#        Y = values[:,1]
#        Z = values[:,2]
#        dispX = values[:,3]
#        dispY = values[:,4]
#        dispZ = values[:,5]
#        finalX = X+dispX
#        finalY = Y+dispY
#        finalZ = Z+dispZ        
        finalX = values[:,0] + values[:,3]
        finalY = values[:,1] + values[:,4]
#        finalZ = values[:,2] + values[:,5]
        ##=====================================================================
        ## circlefit
        ##=====================================================================        
        x_center, y_center, r = circleFit(finalX, finalY)        
        circleFit_X_bucket.append(x_center[0])
        circleFit_Y_bucket.append(y_center[0])
        
        ##=====================================================================
        ## raw Median
        ##=====================================================================
        rawMedian_X_bucket.append(np.median(finalX))
        rawMedian_Y_bucket.append(np.median(finalY))
        
        ##=====================================================================
        ## polyfit Median
        ##=====================================================================    
        X,Y = np.meshgrid(np.linspace(min(finalX), max(finalX), 50), \
                          np.linspace(min(finalY), max(finalY), 50))
        polyMedian_X_bucket.append(np.median(X))
        polyMedian_Y_bucket.append(np.median(Y))

        ##=====================================================================
        ## intersection
        ##=====================================================================
        xMin = min(finalX)
        xMax = max(finalX) 
        yMin = min(finalY)
        yMax = max(finalY)
        y_coordinate_of_xMax = finalY[ finalX.argmax() ]
        y_coordinate_of_xMin = finalY[ finalX.argmin() ]
        x_coordinate_of_yMax = finalX[ finalY.argmax() ]
        x_coordinate_of_yMin = finalX[ finalY.argmin() ]
    
        slopeH = (y_coordinate_of_xMin - y_coordinate_of_xMax)/(xMin - xMax)
        slopeV = (yMin - yMax)/(x_coordinate_of_yMin - x_coordinate_of_yMax)
        
        bV = yMax - slopeV*x_coordinate_of_yMax
        bH = y_coordinate_of_xMax - slopeH*xMax
        
        x_intersect = (bH - bV)/(slopeV - slopeH)
        y_intersect = slopeV*x_intersect + bV
        intersect_X_bucket.append(x_intersect)
        intersect_Y_bucket.append(y_intersect)
        ##=====================================================================
    
    generateHistogramFigure(circleFit_X_bucket, \
                            intersect_X_bucket, \
                            rawMedian_X_bucket, \
                            polyMedian_X_bucket,\
                            plotTitleX,
                            dicFolderInput,
                            histogramFolder)
    
    generateHistogramFigure(circleFit_Y_bucket, \
                            intersect_Y_bucket, \
                            rawMedian_Y_bucket, \
                            polyMedian_Y_bucket,\
                            plotTitleY,
                            dicFolderInput,
                            histogramFolder)
    
# =============================================================================
# =============================================================================
# # Comment out this section if you want bypass the numpy saving section
# =============================================================================
    ##=========================================================================
    ##    Save .npy files of origin X & Y values here
    ##=========================================================================
    circleFile = path.normpath( \
                   path.join(originNPYfolder, \
                             path.split(dicFolderInput)[1]+'_circleFit.npy'))
    
    np.save(circleFile, np.array([circleFit_X_bucket,circleFit_Y_bucket]))
    
    intersectFile = path.normpath( \
                    path.join(originNPYfolder, \
                              path.split(dicFolderInput)[1]+'_intersect.npy'))
    
    np.save(circleFile, np.array([circleFit_X_bucket,circleFit_Y_bucket]))
    
    rawMedianFile = path.normpath( \
                   path.join(originNPYfolder, \
                             path.split(dicFolderInput)[1]+'_rawMedian.npy'))
    
    np.save(circleFile, np.array([circleFit_X_bucket,circleFit_Y_bucket]))
    
    polyMedianFile = path.normpath( \
                     path.join(originNPYfolder, \
                              path.split(dicFolderInput)[1]+'_polyMedian.npy'))
    
    np.save(circleFile, np.array([circleFit_X_bucket,circleFit_Y_bucket]))
    np.save(intersectFile, np.array([intersect_X_bucket,intersect_Y_bucket]))
    np.save(rawMedianFile, np.array([rawMedian_X_bucket,rawMedian_Y_bucket]))
    np.save(polyMedianFile,np.array([polyMedian_X_bucket,polyMedian_Y_bucket]))
# =============================================================================
# =============================================================================
    
    return len(datFileList)
    
###############################################################################

##=============================================================================
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

counter = 0

histogramFolder = 'C:\\temp\Histograms'
if not path.isdir(histogramFolder):
    os.makedirs(histogramFolder)
originNPYfolder = 'C:\\temp\OriginNPYs'
if not path.isdir(originNPYfolder):
    os.makedirs(originNPYfolder)

plt.ioff()

for datFolderString in datFolderNameList:
    print(datFolderString)
    
    circleFit_X_bucket = list()
    circleFit_Y_bucket = list()
    
    polyMedian_X_bucket = list()
    polyMedian_Y_bucket = list()
    
    rawMedian_X_bucket = list()
    rawMedian_Y_bucket = list()
    
    intersect_X_bucket = list()
    intersect_Y_bucket = list()
    
    len_datFileList = originHistograms(datFolderString, \
                                       histogramFolder, \
                                       originNPYfolder)
    
    counter += len_datFileList
    print('.dat Files in this folder:', len_datFileList)
    print()

print('Total# of .dat files:', counter)
print('Total elapsed time:', time()-t0, 'seconds =', (time()-t0)/60, 'minutes')
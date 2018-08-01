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

#import os
import os.path as path
import numpy as np
import matplotlib.pyplot as plt
import glob

all_X_values = np.empty([0, 0])
all_Y_values = np.empty([0, 0])

def originHistograms(dicFileInput):
    
#    print(dicFileInput)
    
    baseName = path.basename(dicFileInput)
#    print(baseName)
    
    datFileList = glob.glob(dicFileInput + '*\*.dat')
#    for datFile in datFileList: print(datFile)
    
    plotTitleX = baseName + ': Origin X-values'
    plotTitleY = baseName + ': Origin Y-values'
    
#    print(plotTitleX)
#    print(plotTitleY)
    
#    circleFit_histogram_Title = 'CircleFit'
#    intersect_histogram_Title = 'Intersection'
#    rawMedian_histogram_Title = 'Raw Median'
#    polyMedian_histogram_Title = 'PolyFit Median' 
    
#    print()

    figX = plt.figure()
    figX.set_size_inches(np.array([8.8,6]))
    figX.suptitle(plotTitleX, fontsize=11)
    ax_X_circleFit = figX.add_subplot(221)
    ax_X_circleFit.set_title('CircleFit', fontsize='small')
    ax_X_intersect = figX.add_subplot(222)
    ax_X_intersect.set_title('Intersection', fontsize='small')
    figX.subplots_adjust(hspace=2)
    ax_X_rawMedian = figX.add_subplot(223)
    ax_X_rawMedian.set_title('Raw Median', fontsize='small')
    ax_X_polyMedian = figX.add_subplot(224)
    ax_X_polyMedian.set_title('PolyFit Median', fontsize='small')
    figX.tight_layout()
    figX.subplots_adjust(top=0.90)
    figX.show()
#    figX.close()
    
    figY = plt.figure()
    figY.set_size_inches(np.array([8.8,6])) 
    figY.suptitle(plotTitleY, fontsize=11)
    ax_Y_circleFit = figY.add_subplot(221)
    ax_Y_circleFit.set_title('CircleFit', fontsize='small')
    ax_Y_intersect = figY.add_subplot(222)
    ax_Y_intersect.set_title('Intersection', fontsize='small')
    figY.subplots_adjust(hspace=2)
    ax_Y_rawMedian = figY.add_subplot(223)
    ax_Y_rawMedian.set_title('Raw Median', fontsize='small')
    ax_Y_polyMedian = figY.add_subplot(224)
    ax_Y_polyMedian.set_title('PolyFit Median', fontsize='small')
    figY.tight_layout()
    figY.subplots_adjust(top=0.90)
    figY.show()
#    figY.close()


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
    
for line in datFolderNameList: originHistograms(line)
    
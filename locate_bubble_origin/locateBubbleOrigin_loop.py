# -*- coding: utf-8 -*-
# =============================================================================
# locatebubbleOrigin.py Loop
# =============================================================================

import os
import os.path as path
import glob
from locateBubbleOrigin import locateBubbleOrigin as lbo

import matplotlib.pyplot as plt
plt.ioff()


datFolderNameList = [ \
#                     'C:\\temp\Valmex_BubbleTest00', \
                     'C:\\temp\Valmex_BubbleTest01', \
                     'C:\\temp\Valmex_BubbleTest02', \
#                     'C:\\temp\Valmex_BubbleTest03' \
                     ]


for line in datFolderNameList :

    baseName = path.basename(line)
    baseName = baseName + '_2Dplots'
    baseName = path.normpath(path.join('C:\\temp', baseName)) 
    
    os.makedirs(baseName)

    line = path.join(line, '*TecData\*.dat')
#    line = path.join(line, '*TecData*\*.dat')
    
    datList = glob.glob(line)
    
    for line in datList:
        fileName = path.splitext(path.basename(line))[0]
        fileName += '_2Dplot.png'
        fileName = path.join(baseName, fileName)
        lbo(line, fileName)
#        print(line, fileName)
    print()
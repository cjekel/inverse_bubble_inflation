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
## """ identifySpecimenDemo_BDH.py """ :
##        simple dispZ threshold script: isolate important data...
##        (this script is an edited version of Charles Jekel's
##        "readDataPlotDispField.py" file)
##        run this script in the same folder as file "B00015.npz"
##=============================================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dicFile = 'B00015.npz'

with np.load(dicFile) as unzipArray: values = unzipArray['zippedArray']

print ('\nThere are')
print (len(values))
print ('data entries')

X = values[:,0]
Y = values[:,1]
Z = values[:,2]
dispX = values[:,3]
dispY = values[:,4]
dispZ = values[:,5]

#==============================================================================
#   plots of the specimen in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

finalX = X+dispX
finalY = Y+dispY
finalZ = Z+dispZ

ax.scatter(finalX, finalY, finalZ, zdir='z',\
           s=.2, c='b', depthshade=False, edgecolor='')
## "  zdir='z'  " orients the data so the Z axis is the chosen vertical axis
## "s" = "size"; sets the desired marker size for each data point
##               (per documentation, units are "points^2")
## "c" = "color"; sets the color of the data points
##                ('b' for "blue"; can be set equal to "finalZ" for gradient)
## "depthshade=False"; turns off the depthshade effect, which assigns a lower
##                     alpha value to points "in back" and a higher alpha to 
##                     points "in front"--turning this off results in 
##                     significantly shorter runtime, and due to the large #
##                     of data points, the depthshade effect is not necessary
## "edgecolor=''"; sets the edgecolor to "None" via the blank string ''--
##                 default bahavior of matplotlib is to set the edgecolor of 
##                 markers to the same color as set to the marker, which 
##                 interfered with the desired size of the markers

## axes limits were chosen by rounding the max & min values 
## and increasing the range by 5mm for maximums and -5mm for minimums
## (conditions were added to handle situations when 0 data points remain)
if len(values) > 0: 
    xMin = np.round( np.min(finalX) ); xMax = np.round( np.max(finalX) ) 
    yMin = np.round( np.min(finalY) ); yMax = np.round( np.max(finalY) ) 
    zMin = np.round( np.min(finalZ) ); zMax = np.round( np.max(finalZ) ) 
    ax.set_xlim3d( xMin-5, xMax+5 ) 
    ax.set_ylim3d( yMin-5, yMax+5 )
    ax.set_zlim3d( zMin-5, zMax+5 )
else:
    ax.set_xlim3d(-100, 100)
    ax.set_ylim3d(-100,100)
    ax.set_zlim3d(-8,50)

ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
plt.show()
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
##
##
##
##=============================================================================

import numpy as np
import matplotlib.pyplot as plt

dicFile = 'C:\\temp\\Valmex_BubbleTest01_TecData_demo\\B00015.dat'
## the .dat file is hard-coded for demo purposes...

##=============================================================================
## utilizing np.loadtxt  
## see "reduceFileFormatSizeDemo.py" file
##=============================================================================
values = np.loadtxt(dicFile, skiprows = 3)

##=============================================================================
## removing data points where Z-displacement is 0mm
## see "identifySpecimenDemo.py" file
##=============================================================================
values = values[ (values[:,2] != 0) | (values[:,5] != 0) ]

print ('\nThere are')
print (len(values))
print ('data entries when zero-displacement points are removed')

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
 

##=============================================================================
## solving for maximum & minimum values
##=============================================================================

# find the minimum and maximum values in the x- and y-directions
xMin = min(finalX)
xMax = max(finalX) 
yMin = min(finalY)
yMax = max(finalY)

# find the maximum value in the z-direction
zMax = np.max(finalZ)

# find the x & y values associated with each extreme
y_coordinate_of_xMax = finalY[ finalX.argmax() ]
y_coordinate_of_xMin = finalY[ finalX.argmin() ]
x_coordinate_of_yMax = finalX[ finalY.argmax() ]
x_coordinate_of_yMin = finalX[ finalY.argmin() ]

# include x & y values associated with maximum z
x_coordinate_of_zMax = finalX[ finalZ.argmax() ]
y_coordinate_of_zMax = finalY[ finalZ.argmax() ]


#==============================================================================
# 2D plot
#==============================================================================

newFig = plt.figure()
axNewFig = newFig.add_subplot(111)

plt.scatter(finalX, finalY, c=finalZ, s=8, edgecolor='')
#plt.scatter(finalX, finalY, c=finalZ, s=5, edgecolor='', cmap=plt.cm.Pastel1)

# include the colorbar
plt.colorbar()

# label axes
plt.xlabel('X+dispX $\mathregular{\mathit{(mm)}}$')
plt.ylabel('Y+dispY $\mathregular{\mathit{(mm)}}$')
plt.title('Z-displacement, 2D representation')

# include grid; low alpha value for good visibility
plt.grid(True, alpha = 0.2, ls='dotted')

# x-axis and y-axis
plt.axhline(0, color='k', lw=0.5, ls='dashed')
plt.axvline(0, color='k', lw=0.5, ls='dashed')

# annotate origin [x = 0 mm, y = 0 mm]
#plt.scatter(0, 0, c='k', s=10, edgecolor='')
plt.annotate('(x=0, y=0)',
             size=7,
             xy = [0, 0],
             xytext=(5, -15),
             textcoords = 'offset pixels')

# plot & annotate maximum Z value
plt.scatter(x_coordinate_of_zMax, y_coordinate_of_zMax, c='b', s=25)
plt.annotate('Z$_{max}$', 
             size=7,
             xy = [x_coordinate_of_zMax, y_coordinate_of_zMax],
             xytext=(-20, -15),
             textcoords = 'offset pixels')

# plot the x & y extrema 
plt.scatter(xMax, y_coordinate_of_xMax, c='orange', marker='x', s=50)
plt.scatter(xMin, y_coordinate_of_xMin, c='orange', marker='x', s=50)
plt.scatter(x_coordinate_of_yMax, yMax, c='orange', marker='x', s=50)
plt.scatter(x_coordinate_of_yMin, yMin, c='orange', marker='x', s=50)

# include perpendicular lines marking the extrema locations
plt.axvline(x_coordinate_of_yMax, color='orange', lw=0.75, ls='dashdot')
plt.axvline(x_coordinate_of_yMin, color='orange', lw=0.75, ls='dashdot')
plt.axhline(y_coordinate_of_xMax, color='orange', lw=0.75, ls='dashdot')
plt.axhline(y_coordinate_of_xMin, color='orange', lw=0.75, ls='dashdot')

# plot lines connecting max & min in the x & y directions
plt.plot([xMax,xMin],
         [y_coordinate_of_xMax,y_coordinate_of_xMin],
         c='r',
         lw=.75,
         ls='dashed')

plt.plot([x_coordinate_of_yMax,x_coordinate_of_yMin],
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
plt.scatter(x_intersect, y_intersect, c='r', s=25)

intersect_coordinate_str = '(%.2f, %.2f)' %(x_intersect, y_intersect)

plt.annotate(intersect_coordinate_str, 
             size=7,
             color='k',
             xy = [x_intersect, y_intersect],
             xytext=(-120, -75),
             textcoords = 'offset pixels',
             arrowprops=dict(facecolor='black', arrowstyle='->'))

#plt.show()


#==============================================================================
# 3D plot (plot of the surfaces fits of Disp Z)
#==============================================================================

from doubleVander import doubleVander
from polySurfaceFit import polySurfaceFit
from correctZ import correctZ

newFinalX, newFinalY, newFinalZ = correctZ(X, Y, Z, dispX, dispY, dispZ)

cDispZ, rDispZ, fittedDispZ = polySurfaceFit(newFinalX,newFinalY,newFinalZ, 4)

X,Y = np.meshgrid(np.linspace(min(newFinalX), max(newFinalX), 20), \
                  np.linspace(min(newFinalY), max(newFinalY), 20))

Axy = doubleVander(X.flatten(),Y.flatten(),4)

ZZ = np.dot(Axy,cDispZ)
Z = ZZ.reshape(X.shape)

#   3D plot of the X, Y, disp Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)

ax.scatter(newFinalX, newFinalY, newFinalZ, zdir='z',s=.2,c='b',edgecolor='')

ax.set_aspect('equal')
#ax.view_init(90, 90)

if len(values) > 0: 
     xMin = np.round( np.min(finalX) ); xMax = np.round( np.max(finalX) ) 
     yMin = np.round( np.min(finalY) ); yMax = np.round( np.max(finalY) ) 
#     zMin = np.round( np.min(finalZ) );
     zMax = np.round( np.max(finalZ) ) 
     ax.set_xlim3d( xMin-5, xMax+5 ) 
     ax.set_ylim3d( yMin-5, yMax+5 )
     ax.set_zlim3d(-100, zMax+5)
else:
    ax.set_xlim3d(-100, 100)
    ax.set_ylim3d(-100,100)
    ax.set_zlim3d(-100,100)
 
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')

ax.set_title('3D plot of Disp Z over the XY bubble position')


#==============================================================================
# Marking the highest Z from the fitted polynomial on 2D plot
#==============================================================================

#correctedMaxZ = max(ZZ)
#correctedMaxZ_xCoordinate = X[np.argmax(Z)]
#correctedMaxZ_yCoordinate = Y[np.argmax(Z)]

x_coord, y_coord = np.unravel_index(Z.argmax(), Z.shape)

ax.scatter(X[x_coord,y_coord], Y[x_coord,y_coord], \
           c='k', s=100, edgecolor='', marker='+')

axNewFig.scatter(X[x_coord,y_coord], Y[x_coord,y_coord], \
                 c='k', s=100, edgecolor='', marker='+')

axNewFig.annotate('Z-polyfit$_{max}$', 
             size=7,
             xy = [X[x_coord,y_coord], Y[x_coord,y_coord]],
             xytext=(20, 15),
             textcoords = 'offset pixels',
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()
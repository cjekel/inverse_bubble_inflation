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
## """ identifySpecimenDemo.py """ :
##        simple dispZ threshold script: isolate important data...
##        (this script is an edited version of Charles Jekel's
##        'readDataPlotDispField.py' file)
##        run this script in the same folder as file 'B00015.dat'
##=============================================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dicFile = 'B00015.dat'
## the .dat file is hard-coded for demo purposes...

##=============================================================================
## utilizing np.loadtxt  
## see 'reduceFileFormatSize.py' file
##=============================================================================
values = np.loadtxt(dicFile, skiprows = 3)

##    the counting standard in python starts iterations with 0...
##    therefore, the 1st column of a 2D array is assigned to [:,0] and
##    the 2nd column is assigned to [:,2] and so on; 
##    the use of ":" indicates "all rows" since python follows
##    the standard [row, column] notation.
 
##    dispZ is in the 6th column of "values", a.k.a. "values[:,5]"
##    initial Z is in the 3rd column of "values" a.k.a. "values[:,2]"

##    the logical constraint "only keep rows with nonzero dispZ"
##    is equivalent to "only keep rows with nonzero initial Z"
##    due to the material thickness of the specimen; check to see:
##    both lines below result in the same # of remaining data entries

values_ZeroDispRemoved = values[values[:,5] != 0]
#values_ZeroDispRemoved = values[values[:,2] != 0]

##    the line "values_ZeroDispRemoved = values[values[:,N] != 0]" is read as:
##    "values_ZeroDispRemoved" equals all rows of "values"
##    where the number in the Nth column is not equal to 0

##    furthermore: the logical constraint "only keep rows with nonzero dispZ"
##    is also equivalent to "only keep rows with nonzero dispX" 
##    and also is equivalent to "only keep rows with nonzero dispY"...
##    although all initial X & initial Y are nonzero,
##    a displacement in Z will always coincide with a displacement
##    in both X & Y...
##    check to see: using either line below to define "values_ZeroDispRemoved"
##    will also result in the same # of remaining data entries 
##    (dispX = 4th column = values[:,3] ; dispY = 5th column = [values[:,4])

#values_ZeroDispRemoved = values[values[:,3] != 0]
#values_ZeroDispRemoved = values[values[:,4] != 0]

print ('There are')
print (len(values)) 
print ('data entries')

## note: the python length command "len()" has interesting default behavior:
## "len()" will always return the number of rows of a list or array,
## no matter the dimension; therefore in this context, "len(values)"
## returns the total number of (X,Y,Z) data points

## these lines are used when plotting original data:
#X = values[:,0]
#Y = values[:,1]
#Z = values[:,2]
#dispX = values[:,3]
#dispY = values[:,4]
#dispZ = values[:,5]

print ('\nThere are')
print (len(values_ZeroDispRemoved))
#print ('data entries when zero-displacement points are removed')
#
X = values_ZeroDispRemoved[:,0]
Y = values_ZeroDispRemoved[:,1]
Z = values_ZeroDispRemoved[:,2]
dispX = values_ZeroDispRemoved[:,3]
dispY = values_ZeroDispRemoved[:,4]
dispZ = values_ZeroDispRemoved[:,5]

#==============================================================================
#   plots of the specimen in 3D
#==============================================================================
fig = plt.figure() # creating a figure object...
ax = fig.add_subplot(111, projection='3d') # adding an empty plot to figure...

## the displaced nodes are equal to "X+dispX", "Y+dispY", "Z+dispZ"
finalX = X+dispX
finalY = Y+dispY
finalZ = Z+dispZ

ax.scatter(finalX, finalY, finalZ, zdir='z', s=.05, c='b')
## "  zdir='z'  " orients the data so the Z axis is the chosen vertical axis
## "s" = "size"; sets the desired marker size for each data point
##               (per documentation, units are "points^2")
## "c" = "color"; sets the color of the data points ('b' for "blue") 

## defining axes limits: the specimen is revealed when "values_ZeroDispRemoved"
## is plotted; "values" shows the specimen plus test apparatus data points
## (nodes from the apparatus have 0mm Z-displacement by default)

## the maximum and minimum values for both "values" & "values_ZeroDispRemoved"
## can be viewed with the following commands:
#np.max(X+dispX), np.min(X+dispX)
#np.max(Y+dispY), np.min(Y+dispY)
#np.max(Z+dispZ), np.min(Z+dispZ)

## axes limits were chosen by rounding the max & min values 
## and increasing the range by 5mm for maximums and -5mm for minimums

xMin = np.round( np.min(finalX) ); xMax = np.round( np.max(finalX) ) 
yMin = np.round( np.min(finalY) ); yMax = np.round( np.max(finalY) ) 
zMin = np.round( np.min(finalZ) ); zMax = np.round( np.max(finalZ) ) 

ax.set_xlim3d( xMin-5, xMax+5 ) 
ax.set_ylim3d( yMin-5, yMax+5 )
ax.set_zlim3d( zMin-5, zMax+5 )

ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
plt.show()

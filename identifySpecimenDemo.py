##    simple dispZ threshold script: isolate important data...
##    (this script is an edited version of 'readDataPlotDispField.py' file)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dicFile = 'B00015.dat'

"""utilizing option 1""" #see 'reduceFileFormatSize.py' file
values = np.loadtxt(dicFile, skiprows = 3)

##    dispZ is in the 5th column; initial Z is in the 2nd column;
##    logical constraint "only keep rows with nonzero dispZ"
##    is equivalent to "only keep rows with nonzero initial Z"
##    due to the material thickness of the specimen; check to see:
##    both lines below result in the same # of filtered data entries
filteredValues = values[values[:,2] != 0]
#filteredValues = values[values[:,5] != 0]

##    furthermore: constraint also equivalent to 
##    "only keep rows with nonzero dispX"/"only keep rows with nonzero dispY"
##    although all initial X & initial Y are nonzero,
##    a displacement in Z will always coincide with a displacement in X & Y
##    check to see: both lines below also result in the same # of
##    filtered data entries (dispX = 3rd column, dispY = 4th column)
#filteredValues = values[values[:,3] != 0]
#filteredValues = values[values[:,4] != 0]

print ('There are')
print (len(values))
print ('data entries')

print ('\nThere are')
print (len(filteredValues))
print ('filtered data entries')

X = filteredValues[:,0]
Y = filteredValues[:,1]
Z = filteredValues[:,2]
dispX = filteredValues[:,3]
dispY = filteredValues[:,4]
dispZ = filteredValues[:,5]

#==============================================================================
#   plots of the specimen in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X+dispX, Y+dispY, Z+dispZ, zdir='z', s=.1, c='b')
#ax.set_aspect('equal')
ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100,100)
ax.set_zlim3d(-8,50)
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
plt.show()
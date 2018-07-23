# -*- coding: utf-8 -*-
# =============================================================================
# MIT License
#
# Copyright (c) 2018 Charles Jekel, Andrés Bernardo
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

# Note: this is an updated version of Charles Jekel's original
# "readDataPLotDispField.py" file.

#    Read Data from the DIC
#    import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#   ***** I've commented out the export functionality of this program *****
dicFile = 'C:\\temp\\demo\\B00015.dat'
exportFile = 'coeffs20'
#   Define a function that combines two vander matricies for use with least
#   Square polynomial regression fitting for three dimensional data
#   Useage A = doubleVander(X,Y,degree)
#   Where X, Y are your vectors
#   Degree = the order of the desired polynomial
#   A is the resulting double vander matrix
def doubleVander(x,y,Degree):
    N = Degree + 1
    Ax = np.vander(x,Degree+1)
    Ay = np.vander(y,Degree+1)
    Aout = np.zeros((len(x),N*N))
    count = 0
    for i in range(0,N):    
        for j in range(0,N):
            Aout[:,count] = Ax[:,i]*Ay[:,j]
            count = count +1
    return Aout;
#    Define a function that deterimines the circle of best fit for a two 
#    dimensional data set. Simply supply the X and Y data vectors of the data 
#    set, and the function returns the x and y center points of the circle, as 
#    well as the radius of the circle
#    Useage: xCenter, yCenter, r = circleFit(X,Y)
def circleFit(X,Y):
    import math
    # convert the input vectors to numpy arrays
    X = np.array(X)
    Y = np.array(Y)
    #   Assemble the A matrix
    A = np.zeros((len(X),3))
    A[:,0] = X*2
    A[:,1] = Y*2
    A[:,2] = 1

    #   Assemble the f matrix
    f = np.zeros((len(X),1))
    f[:,0] = (X*X) + (Y*Y)
    C, residules, rank, singval = np.linalg.lstsq(A,f)

    #   solve for r
    r = math.sqrt((C[0]*C[0])+(C[1]*C[1])+C[2])
    return C[0], C[1], r;
#   Define a function that fits a polynomial surface to given x y and z
#   The fit finds the dgree polynomail that fits to the z given xy ie finds
#   z(x,y). This uses the least squares fitting method
def polySurfaceFit(x, y, z, degree):
    A = doubleVander(x,y,degree)
    c, r, rank, singval = np.linalg.lstsq(A,z)
    ZZ = np.dot(A,c)
    
    #   Calculate the coefficition of determination r
    sTot = z - np.mean(z)
    sRes = ZZ - z
    SSR = np.dot(sRes,sRes)
    SST = np.dot(sTot,sTot)
    rSquared = 1 - (SSR/SST)
    print('SSR is ', SSR, 'for the '+str(degree)+'th order fit')
    print('r squared is ', rSquared, 'for the '+str(degree)+'th order fit')
    
    #   Plot the residuals
#    fig = plt.figure()
    plt.figure()
#    ax = fig.add_subplot(111)
    plt.plot(z,ZZ,'o', ms=1, mew=0)
    st = np.arange(min(ZZ),max(ZZ))
    plt.plot(st,st,'-k')
    plt.axis('equal')
    plt.title(''+str(degree)+'th order fit. R^2 = %.5f' %rSquared, fontsize=26)
    plt.xlabel('the suplied z values', fontsize=20)
    plt.ylabel('Polynomial Fitted Z values', fontsize=20)
    plt.grid()
    plt.show()
    return c, r, ZZ;



values = np.loadtxt(dicFile, skiprows = 3)

values = values[ (values[:,2] != 0) | (values[:,5] != 0) ]

X = values[:,0]
Y = values[:,1]
Z = values[:,2]
dispX = values[:,3]
dispY = values[:,4]
dispZ = values[:,5]


print('There are')
print(len(values))
print('data entries when zero-displacement points are removed')


#   Find the best fit circle of the disc. 
xCenter, yCenter, radius = circleFit(X,Y)
print('xCenter', xCenter, 'yCenter', yCenter)


#   Now that the center of the disc is known, shift X and Y Values
Y = Y - yCenter
X = X - xCenter


#   find the best fit circle of the disc for all values 
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)
dispX = np.array(dispX)
dispY = np.array(dispY)
dispZ = np.array(dispZ)


correctX = dispX + X
correctY = dispY + Y
correctZ = dispZ + Z
print('max of Z before slip correction', max(correctZ))
print('min of Correct Z', min(correctZ))
print('min of dispZ', min(dispZ))

correctZ = correctZ - min(correctZ)

numberOfDiscPoints = len(correctX)


#   Get rid of all data points with a correct Z < 5
finalX = []
finalY = []
finalDispX = []
finalDispY = []
finalDispZ = []
correctX1 = []
correctY1 = []
correctZ1 = []
for i in range(0,len(correctX)):
    if correctZ[i] >= 5:
        finalX.append(X[i])
        finalY.append(Y[i])
        finalDispX.append(dispX[i])
        finalDispY.append(dispY[i])
        finalDispZ.append(correctZ[i]) 
        #    The reason this is Correct Z and not 
        #    disp Z is really Z + dispZ defined as correct Z, this occurs
        #    because if you look at the Z, the surface mesh from the dic on
        #    the bubble isn't flat. It has cureves. This assumes a formulation 
        #    that all Z values making the bubble surface are 0. Then the Disp 
        #    on the bubble surface  
        correctX1.append(correctX[i])
        correctY1.append(correctY[i])
        correctZ1.append(correctZ[i])

finalX = np.array(finalX)
finalY = np.array(finalY)
finalDispX = np.array(finalDispX)
finalDispY = np.array(finalDispY)
correctX1 = np.array(correctX1)
correctY1 = np.array(correctY1)
correctZ1 = np.array(correctZ1)



#   convert Z values to numpy arrays
correctZ1 = np.array(correctZ1)
finalDispZ = np.array(finalDispZ)



cDispX, rDispX, fittedDispX = polySurfaceFit(finalX, finalY, finalDispX, 4)
cDispY, rDispY, fittedDispY = polySurfaceFit(finalX, finalY, finalDispY, 4)
cDispZ, rDispZ, fittedDispZ = polySurfaceFit(finalX, finalY, finalDispZ, 4)


#==============================================================================
#   plots of the surfaces fits  of Disp X
X,Y = np.meshgrid(np.linspace(min(finalX), max(finalX), 20), \
                  np.linspace(min(finalY), max(finalY), 20))
Axy = doubleVander(X.flatten(),Y.flatten(),4)
ZZ = np.dot(Axy,cDispX)
Z = ZZ.reshape(X.shape)
#   3D plot of the X, Y, disp X
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, alpha=0.2, label='fitted surface')
ax.scatter(finalX, finalY, finalDispX, zdir='z', s=.2, c='b', \
           label='disp X', edgecolor='')
#ax.set_aspect('equal')
ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100,100)
ax.set_zlim3d(-8,8)
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('disp X (mm)')
ax.set_title('Disp Y data on fitted surface')
plt.show()

#   Plot of the  X disp X values
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(finalX,finalDispX,'bo',mew=0,ms=2,alpha=0.5,label='disp X')
plt.plot(finalX,fittedDispX,'ro',mew=0,ms=.75,alpha=.8,label='fitted Disp X')
plt.xlabel('X (mm)')
plt.ylabel('disp X (mm)')
plt.title('The X and disp X values')
plt.legend(loc=4,markerscale=5)
ax.grid(True)
plt.show()

#   Plot of the new Y disp X values
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(finalY,finalDispX,'bo',mew=0,ms=2,alpha=0.5,label='disp X',)
plt.plot(finalY,fittedDispX,'ro',mew=0,ms=.75,alpha=.8,label='fitted Disp X')
plt.xlabel('Y (mm)')
plt.ylabel('disp X (mm)')
plt.title('The Y and disp X values')
plt.legend(markerscale=5)
ax.grid(True)
plt.show()
#==============================================================================


#==============================================================================
#   plots of the surfaces fits  of Disp Y
ZZ = np.dot(Axy,cDispY)
Z = ZZ.reshape(X.shape)
#   3D plot of the X, Y, disp Y
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, alpha=0.2, label='fitted surface')
ax.scatter(finalX, finalY, finalDispY, zdir='z', s=.2, c='b', edgecolor='')
#ax.set_aspect('equal')
ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100,100)
ax.set_zlim3d(-8,8)
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('disp Y (mm)')
ax.set_title('Disp Y data on fitted surface')
plt.show()

#   Plot of the  X disp Y values
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(finalX,finalDispY,'bo',mew=0,ms=2,alpha=0.5,label='disp Y')
plt.plot(finalX,fittedDispY,'ro',mew=0,ms=.75,alpha=.8,label='fitted Disp Y')
plt.xlabel('X (mm)')
plt.ylabel('disp Y (mm)')
plt.title('The X and disp Y values')
plt.legend(markerscale=5)
ax.grid(True)
plt.show()

#   Plot of the new Y disp Y values
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(finalY,finalDispY,'bo',mew=0,ms=2,alpha=0.5,label='disp Y')
plt.plot(finalY,fittedDispY,'ro',mew=0,ms=.75,alpha=.8,label='fitted Disp Y')
plt.xlabel('Y (mm)')
plt.ylabel('disp Y (mm)')
plt.title('The Y and disp Y values')
plt.legend(loc=4,markerscale=5)
ax.grid(True)
plt.show()
#==============================================================================


#==============================================================================
#   plots of the surfaces fits  of Disp Z
ZZ = np.dot(Axy,cDispZ)
Z = ZZ.reshape(X.shape)
#   3D plot of the X, Y, disp Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, alpha=0.2, label='fitted surface')
ax.scatter(finalX, finalY, finalDispZ, zdir='z', s=0.2, c='b', edgecolor='')
ax.set_aspect('equal')
ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100,100)
ax.set_zlim3d(-100,100)
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('disp Z (mm)')
ax.set_title('3D plot of Disp Z over the XY bubble position')
plt.show()


#   Plot of the  X disp Z values
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(finalX,finalDispZ,'bo',mew=0,ms=2,alpha=0.5,label='dispZ')
plt.plot(finalX,fittedDispZ,'ro',mew=0,ms=.75,alpha=.8,label='fitted DispZ')
plt.xlabel('X (mm)')
plt.ylabel('disp Z (mm)')
plt.title('The X and disp Z values')
plt.legend(markerscale=5)
ax.grid(True)
plt.show()

#   Plot of the new Y disp Z values
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(finalY,finalDispZ,'bo',mew=0,ms=2,alpha=0.5,label='disp Z')
plt.plot(finalY,fittedDispZ,'ro',mew=0,ms=.75,alpha=.8,label='fitted Disp Z')
plt.xlabel('Y (mm)')
plt.ylabel('disp Z (mm)')
plt.title('The Y and disp Z values')
plt.legend(markerscale=5)
ax.grid(True)
plt.show()
#==============================================================================
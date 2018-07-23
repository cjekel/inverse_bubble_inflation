# -*- coding: utf-8 -*-
# =============================================================================
# MIT License
#
# Copyright (c) 2018 Charles Jekel
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

from circleFit import circleFit

def correctZ(X, Y, Z, dispX, dispY, dispZ):
    
    #   Find the best fit circle of the disc. 
    xCenter, yCenter, radius = circleFit(X, Y)

    #   Now that the center of the disc is known, shift finalX and Y Values
    Y = Y - yCenter
    X = X - xCenter


    #   find the best fit circle of the disc for all values 
    correctX = dispX + X
#    correctY = dispY + Y
    correctZ = dispZ + Z
    
    correctZ = correctZ - min(correctZ)
    
    #   Get rid of all data points with a correct Z < 5
    finalX = []
    finalY = []
#    finalDispX = []
#    finalDispY = []
    finalDispZ = []
#    correctX1 = []
#    correctY1 = []
#    correctZ1 = []
    for i in range(0,len(correctX)):
        if correctZ[i] >= 5:
            finalX.append(X[i])
            finalY.append(Y[i])
#            finalDispX.append(dispX[i])
#            finalDispY.append(dispY[i])
            finalDispZ.append(correctZ[i]) 
        #    The reason this is Correct Z and not 
        #    disp Z is really Z + dispZ defined as correct Z, this occurs
        #    because if you look at the Z, the surface mesh from the dic on
        #    the bubble isn't flat. It has cureves. This assumes a formulation 
        #    that all Z values making the bubble surface are 0. Then the Disp 
        #    on the bubble surface  
#            correctX1.append(correctX[i])
#            correctY1.append(correctY[i])
#            correctZ1.append(correctZ[i])
    
    
    return finalX, finalY, finalDispZ, xCenter, yCenter;
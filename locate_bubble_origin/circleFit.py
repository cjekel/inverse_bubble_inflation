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

import numpy as np 
import math

#    Define a function that deterimines the circle of best fit for a two 
#    dimensional data set. Simply supply the X and Y data vectors of the data 
#    set, and the function returns the x and y center points of the circle, as 
#    well as the radius of the circle
#    Useage: xCenter, yCenter, r = circleFit(X,Y)
def circleFit(X,Y):
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
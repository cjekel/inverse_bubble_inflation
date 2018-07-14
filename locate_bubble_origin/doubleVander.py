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

#   Define a function that combines two vander matricies for use with least
#   Square polynomial regression fitting for three dimensional data
#   Useage A = doubleVander(X,Y,degree)
#   Where X, Y are your vectors
#   Degree = the order of the desired polynomial
#   A is the resulting double vander matrix

import numpy as np

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
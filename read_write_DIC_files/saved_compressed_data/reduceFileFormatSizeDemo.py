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
## """ reduceFileFormatSize.py """ :
##           reducing filesize/memory of bubble test data ".dat" file...
##           run this script in the same folder as file "B00015.dat"
##=============================================================================

from time import time # used in order to analyze the runtime of code sections
t0 = time()

# =============================================================================
# 
# "np.loadtxt"; skip first 3 rows to avoid headers & string error
# 
# =============================================================================
import numpy as np

dicFile = 'B00015.dat'
# the .dat file is hard-coded for demo purposes...

testResult_LoadText = np.loadtxt(dicFile, skiprows = 3)
# parameter "skiprows" is used to remove headers in ".dat" file

np.save('testResult_LoadText.npy', testResult_LoadText)
# saves a new file called "testResult_LoadText.npy" onto hard drive
# (in the same location of this script); ".npy" means "numpy array file" 

test_LoadText_retrieved = np.load('testResult_LoadText.npy')
# loads numbers from "testResult_LoadText.npy" file into a numpy array;
# "testResult_LoadText" and "test_LoadText_retrieved" are equivalent

##=============================================================================
##    note: "np.genfromtxt" accomplishes the same thing,
##    and can handle any possible blank elements in the data:
#testResult_LoadText = np.genfromtxt(dicFile, skip_header = 3)
#np.save('testResult_LoadText.npy', testResult_LoadText)
##=============================================================================

t1 = time()
# print out the elapsed time for option "np.loadtxt" operation...
print('Run time in seconds, Load Text option:', t1-t0)



# =============================================================================
# 
#  "np.memmap", memory mapping, along with "np.loadtxt"...
#  (unfortunaely, this resulted in a similar process to utilizing "np.loadtxt"
#   by itself; see pros/cons @ end of this section)
# 
# =============================================================================
import os.path as path

newFilePath = path.dirname( path.abspath(dicFile) )
# this saves the file path of this script's current directory on disk
# into a string variable named "newFilePath"

newFilePath = path.join(newFilePath, 'testResult_MemoryMap.npy')
# this updates the string of this script's current directory by concatenating 
# the string "testResult_MemoryMap.npy" to the end; the resulting string
# represents the desired name & location of the new file to be saved on disk

fp = np.memmap(newFilePath, \
               dtype='float32', mode='w+', shape=np.shape(testResult_LoadText))
# note: the "np.memmap" process is dependent on the "np.loadtxt" process due to
# the need to remove headings from the original text data (see lines 45-46),
# and also due to the required "shape" parameter, which gives the necessary
# array dimensions matching the dimensions of the original data;
# also, " mode='w+' " is explained per documentation:
#    the file is created or the existing file is overwritten 
#    for both reading & writing priveleges
# also, note how the data type is set to "float32" with the parameter "dtype";
# this will be explained in the pros/cons section to follow

# at this point, the file "testResult_MemoryMap.npy" is saved onto disk,
# however, it cannot be deleted or edited directly due to the open memory map

# "fp" represents the memory map with all entries "0" and with the
# same dimensions as the test data... 
fp[:] = testResult_LoadText[:]
# ...this command assigns every element in "testResult_LoadText" to the 
# corresponding array location into "fp" 
# (note: documentation describes "memmap" objects as "array-like objects")

del fp
# object "fp" is now deleted, however, "testResult_MemoryMap.npy" is populated
# with data from "testResult_LoadText"; the file "testResult_MemoryMap.npy" 
# on disk can now be deleted or edited directly
# from documentation...
#    deletion flushes memory changes to disk before removing the object

# to retrieve data, a new memory map object is created:
newfp = np.memmap(newFilePath, \
                dtype='float32', mode='r', shape=np.shape(testResult_LoadText))
# using " mode='r' ", the map is "read only" to protect from possible edits
# note that the new memory map also requires the correct dimensions
# for the "shape" paramter

# data is retrievable using the newly created memory mapping:
test_MemoryMap_retrieved = np.array(newfp)
# at this point the file "testResult_MemoryMap.npy" is again open not editable
# or able to be deleted due to the open memory map
del newfp
# now, the file "testResult_MemoryMap.npy" can be deleted because the 
# memory mapping is once again closed

t2 = time()
# print out the elapsed time for option "np.memmap" operation...
print('Run time in seconds, Memory Map option:', t2-t0)

##=============================================================================
## cons: can only save memory space if dtype='float32', 
##       if the parameter "dtype" is set to the the original precision float64,
##       the resulting file size is the same as with the "np.loadtext" option;
##       basically, the memory mapping option is equivalent to "np.loadtext"
##       when setting the parameter "dtype" to float32 precision, e.g.:
##       testResult_LoadText = np.loadtxt(dicFile, dtype='float32', skiprows=3)    
## 
## pros: data is still accurate to 5 decimal places, which may be negligible;
##       size of "testResult_MemoryMap.npy" is half of "testResult_LoadText";
##       the additional runtime is quite negligible compared to the runtime
##       seen with the "np.loadtext" option, so this leaves possibilties to 
##       utilize the temp folder or temporary files & delete them after
##       
## see documentation:
##     https://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html
##=============================================================================



# =============================================================================
# 
# utilizing "numpy.savez_compressed", along with "np.loadtxt"...
# (this one might be the winner!! down from 15 MB to 3 MB)
#
# =============================================================================

np.savez_compressed('testResult_Zip.npz', zippedArray = testResult_LoadText)
# uses the values from the "np.loadtext" option (and so is also dependent);
# values from the "testResult_LoadText" variable are saved to a new file on
# disk; the new file is named "testResult_Zip.npz" and is saved in the same
# location as this script for the purposes of this demo...
# the ".npz" file extension means "zipped numpy file"
# note: "zippedArray" is an arbitrary callback name to retrieve data, 
# which will be seen later

with np.load('testResult_Zip.npz') as unzipArray:
    test_Zip_retrieved = unzipArray['zippedArray']
# loads the values from "testResult_Zip.npz" into a dictionary-like variable
# called "unzipArray"; this particular syntax using the "with" command makes
# sure that the associated files saved on disk are closed after use 

# the callback "zippedArray" retrieves numbers from the dictionary-like 
# "unzipArray" object...
# per documentation, this is how to retrieve data from compressed numpy files:
#unzipArray = np.load('testResult_Zip.npz')
#test_Zip_retrieved = unzipArray['zippedArray']

t3 = time() 
# print out the elapsed time for option "numpy.savez_compressed" operation...
print('Run time in seconds, Compressed Array option:', (t3-t0) - (t2-t1) )
##=============================================================================
## note: "np.savez_compressed" has non-negligible runtime (see print outputs)
##=============================================================================



##=============================================================================
##    Other notes:
##    consider using the %timeit command:
#%timeit np.random.random(200)
## 
##    python "pickle" may also be an explorable option
##
##    perhaps look into faster functions besides numpy.save
##=============================================================================

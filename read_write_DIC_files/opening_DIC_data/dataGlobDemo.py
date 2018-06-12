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
##  """ dataGlobDemo.py """ :
##    utilizing 'glob.py' module to reduce file size of multiple .dat files...
##    be sure to run this script in the same folder as 
##    the folder that contains a collection of 'B#####.dat' files...
##=============================================================================

import os
import os.path as path
import glob
import numpy as np

from time import time # used in order to analyze the runtime of code sections
t0 = time()

##    currently, the script simply calls the filepath of its own location:
dir_path = path.dirname(path.realpath(__file__))

##    the folder of .dat files is hard-coded for demo purposes...
datFolderName = 'Valmex_BubbleTest01_TecData_demo'

# create folder filepath string
datFolder = path.join(dir_path, datFolderName) 

# =============================================================================
# """
#    utilizing "np.savez_compressed" & "np.loadtext" methods
#    from 'reduceFileFormatSize.py' file
# """
#       GOAL:
#       iterate over each file in "Valmex_BubbleTest01_TecData_demo" folder,
#       create a compressed numpy array file (".npz") 
#       from each text data file (".dat"),
#       and save the resulting ".npz" files into a new folder.
# =============================================================================

datList = glob.glob('**/*.dat')
## create list of data filename strings that we plan to convert
## utilizes the "global" method to find files with ".dat" extension

npzFolder = path.join(dir_path, 'CompressedNumpyData_'+datFolderName)
## create new folder name string in which to save the converted data files

if not path.exists(npzFolder) :
    ## if the new folder can be created, continue;
    ## otherwise the script ends to avoid overwriting
    ## (see "else" statement below)                               
    
    os.makedirs(npzFolder) 
    ## create the new folder & save it to the hard drive;
    ## by default, the new folder will be saved in the same location as
    ## this script's current location upon the hard drive
    
    for line in datList :
        fileNameNoExtension = path.splitext( path.basename(line) )[0]
        ## splits the actual filename from its extension, e.g.:
        ## "B00001.dat" --> ("B00001", ".dat")
        ## using [0] selects the firt element, "B00001"
        
        datNumpyArray = np.loadtxt(line, skiprows = 3)
        ## load data file into a numpy array
        ## parameter "skiprows" is used to remove headers in ".dat" files
        
        np.savez_compressed( path.join(npzFolder, fileNameNoExtension), \
                             zippedArray = datNumpyArray) 
        ## save numbers into a compressed numpy array (headers are removed)
        ## note: "zippedArray" is an arbitrary callback name to retrieve data
        ## (see data retrieval section below)
else :
    print('There is already a folder named '+\
          'CompressedNumpyData_'+datFolderName)
    # if a folder already exists with the same name as the new folder,
    # output this warning message and stop the operation

t1 = time() # print out the elapsed time for the conversion opeation...
print('\nRun time in seconds, data compression:', (t1 - t0))

# =============================================================================
# 
# here is how to retrieve data from the zipped ".npy" files...
# (zipped numpy file extension = ".npz")
# 
# =============================================================================

t2 = time() # used to analyze the runtime of the data retrieval section

datZippedList = glob.glob( '**/*.npz' )
# creates list of strings of zipped numpy filenames that we plan to retrieve
## utilizes the "global" method to find files with ".npz" extension

unzippedDictionary = {} 
# initialize empty dictionary; 
# data will be saved into this variable

for line in datZippedList :
## uncomment these 2 lines for further understanding of file manipulation 
#    print( path.splitext( path.basename(line) )[0] )   
#    print( path.join(dir_path, line) )

    with np.load(path.join(dir_path, line)) as unzipArray:
        test_Zip_retrieved = unzipArray['zippedArray']
        # loads the values into a dictionary-like variable
        # called "unzipArray"; this particular syntax using "with" command
        # makes sure the associated files saved on disk are closed after use 

        unzippedDictionary[ path.splitext( path.basename(line) )[0] ] = \
            unzipArray['zippedArray']   

##    to retrieve data from B00001.npz, use unzippedDictionary['B00001']
##    to retrieve data from B00002.npz, use unzippedDictionary['B00002']
##    etc.
##    this is so we can use the filenames, B00001 etc., as variable names     

t3 = time() # print out elapsed time of data retrieval section
print('\nRun time in seconds, data retrieval:', (t3 - t2))

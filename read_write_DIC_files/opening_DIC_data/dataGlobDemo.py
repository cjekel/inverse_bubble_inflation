##    Created by Andy Bernardo https://github.com/a-bernardo

##    utilizing 'glob.py' module to reduce file size of multiple .dat files...
##    run this script in the same folder as the folder that contains
##    a collection of 'B#####.dat' files...

import os
import os.path as path
import glob
import numpy as np

from time import time

t0 = time()

##    currently, the script simply calls the filepath of this file's location:
dir_path = path.dirname(path.realpath(__file__))

##    the folder of .dat files is hard-coded for demo purposes...
datFolderName = 'Valmex_BubbleTest01_TecData_demo'
datFolder = path.join(dir_path, datFolderName)

"""
utilizing options 1 & 3 from 'reduceFileFormatSize.py' file
('numpy.savez_compressed' method)
"""

##    GOAL:
##    iterate over each file in 'Valmex_BubbleTest01_TecData_demo' folder,
##    compress each .dat into .npz,
##    and save the resulting .npz files into a new folder.

datList = glob.glob('**/*.dat')

npzFolder = path.join(dir_path, 'CompressedNumpyData_'+datFolderName)

if not path.exists(npzFolder) :
    os.makedirs(npzFolder)

    for line in datList :
        fileNameNoExtension = path.splitext( path.basename(line) )[0]
        datNumpyArray = np.loadtxt(line, skiprows = 3)
        np.savez_compressed( path.join(npzFolder, fileNameNoExtension), \
                             zippedArray = datNumpyArray)
        # note: "zippedArray" is an arbitrary callback name to retrieve data
else :
    print('There is already a folder named '+\
          'CompressedNumpyData_'+datFolderName)


t1 = time()

print('\nRun time in seconds, data compression:', (t1 - t0))


##    here is how to retrieve data from the zipped .npy files...

t2 = time()

datZippedList = glob.glob( '**/*.npz' )

unzippedDictionary = {}

for line in datZippedList :
#    print( path.splitext( path.basename(line) )[0] )
#    print( path.join(dir_path, line) )
    unzipArray = np.load( path.join(dir_path, line) )
    unzippedDictionary[ path.splitext( path.basename(line) )[0] ] = \
        unzipArray['zippedArray']

#    to retrieve data from B00001.npz, use unzippedDictionary['B00001']
#    to retrieve data from B00002.npz, use unzippedDictionary['B00002']
#    etc.

t3 = time()

print('\nRun time in seconds, data retrieval:', (t3 - t2))

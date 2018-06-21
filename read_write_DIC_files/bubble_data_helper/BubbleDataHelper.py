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
## """ Bubble Test Data Helper """ :
##         File compression;
##             zero-Z-displacement data removal to isolate specimen;
##                 optional plot output & grid @ apparatus surface 
##                 (work in progress--to be completed)
##=============================================================================
# =============================================================================
#    This function has 2 required arguments and 2 optional arguments.

#    Required argument 1, "dataFolderDirectory": 
#        filepath of folder containing TecData ".dat" files.
#        By default, this script will save resulting ".npz" files in a new 
#        folder under the same directory as this script's current directory.

#    Required argument 2, "bool_removeZeroZdisp":
#        boolean to turn on/off "dispZ != 0" data removal tool.
#        Setting this to "Y" will remove all data points that have an 
#        displaced Z value of 0mm; this removes data with 0 displacement,
#        i.e., data points that are not relevent to the specimen.
#        Setting this to "N" keeps data unaffected. 

#    Optional argument 1, "output3Dplot": (work in progress--to be completed)
#        boolean to deliver 3D plots of the displacement field
#        from given TecData, which will be saved in ".png" format
#        in the same location as the compressed ".npz" files.
#        Default is "false".

#    Optional argument 2: "plotSurfaceGrid" (work in progress--to be completed)
#        boolean to turn on/off grid representing apparatus surface @ Z=10mm. 
#        This grid is added to the 3D plots as a visual aid,
#        replacing the data points where Z displacement = 0mm.
#        Default is "false".
#        If optional argument 1 "output3Dplot" is "false",
#        OR if required argument 2 "bool_removeZeroZdisp" is "N",
#        then this option is also "false" by default.
# =============================================================================

###############################################################################
##=============================================================================
## How to use BubbleDataHelper:
## 
## -> add the Python interpreter to your "Path" Environment Variable  
###============================================================================
###        If you are not sure if Python is added to your path,
###        here are some resources to assist you:
### Windows:
###   https://superuser.com/questions/143119/
###           how-do-i-add-python-to-the-windows-path
###   https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-
###           as-an-internal-or-external-command/
###   (you will need to know the location of your python interpreter, 
###    a.k.a. the folder where "python.exe" file is located; common locations
###    are C:\Python27, C:\Python36, C:\Users\[name]\Anaconda3, etc.)
###
### Linux: 
###   https://stackoverflow.com/questions/18247333/python-pythonpath-in-linux
###
### MacOS:
###   https://docs.python.org/2/using/mac.html
###   https://stackoverflow.com/questions/3387695/add-to-python-path-mac-os-x
###   https://stackoverflow.com/questions/3696124/changing-python-path-on-mac
###============================================================================
##
## -> copy directory (a.k.a. filepath) of folder containing this script 
##    (use keyboard shortcut "ctrl+c")
##
## -> open command prompt
###============================================================================
###        If you are not sure how to open a command prompt/terminal,
###        here are some resources to assist you:
### Windows:
###   https://www.howtogeek.com/235101/10-ways-to-open-
###           the-command-prompt-in-windows-10/
###
### Linux: 
###   https://askubuntu.com/questions/196212/how-do-you-open-a-command-line
###
### MacOS:
###   https://www.howtogeek.com/210147/how-to-open-terminal-
###           in-the-current-os-x-finder-location/
###   http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line
###============================================================================
##
## -> change command directory by typing the command "cd " (with a space),
##    then paste the filepath of this script's containing folder 
##    (using the keyboard shortcut "ctrl+v"), e.g., cd C:\temp
##
##    --> note: if necessary, use the commands "C:" or "cd /d C:"
##              to switch disks to the C drive (or any drive of your choosing)
##
## -> press "enter" (you should see the directory change on the command line)
## 
## -> type "python BubbleDataHelper.py" (without quotation marks)
##    and press "enter"
##
## -> follow prompts provided by the function
##    (use "ctrl+c" & "ctrl+v" to copy & paste the directory of the data folder
##    containing the ".dat" files once prompted)
##
##    note: if there are spaces within folder names in the necessary paths, 
##          you may use quotation marks to avoid errors, e.g., instead of 
##          cd C:\temp\Example with Space\Example, you can type
##          cd C:\temp\"Example with Space"\Example, or
##          cd "C:\temp\Example with Space\Example" 
##=============================================================================
###############################################################################

import sys
import os
import os.path as path
import glob
import numpy as np

# print out the user's current version of python
sys.stdout.write('\n\nPython %s\n\n\n' % (sys.version))

# print welcome message & instructions; use string "quitBDH" to exit script
print('Welcome to BubbleDataHelper!\n\n')
print('Type "quitBDH" and press "Enter" to exit out of BubbleDataHelper.\n')

# this function evaluates the given folder path argument
# to determine if it is valid
def is_folderPathStr_valid(prompt):
    while True:
        try:
            folderPath = input(prompt)
            folderPath = folderPath.strip()
            folderPath = folderPath.lower()
        except ValueError:
            print('Unknown error encountered.\n')
            continue
        
        if folderPath == 'quitbdh':            
            print('\nExiting BubbleDataHelper...')
            sys.exit()
        
        elif not path.isdir(folderPath):
            print('Sorry, that is not a valid folder directory. ' \
                  'Please try again.\n')
            continue
        
        else:
            print('Valid folder directory given!\n')
            break

    return folderPath

# this function evaluates the given boolean string argument
# to determine if it is valid
def is_bool_input_valid(prompt):
    while True:
        try:
            bool_str_input = input(prompt)
            bool_str_input = bool_str_input.strip()
            bool_str_input = bool_str_input.lower()
        except ValueError:
            print('Unknown error encountered.\n')
            continue
    
        if bool_str_input == 'quitbdh':            
            print('\nExiting BubbleDataHelper...')
            sys.exit()
            
        elif (bool_str_input != 'yes') & (bool_str_input != 'no'):
            print('Sorry, please type only "Yes" or "No" and try again.')
            print('You may type "quitBDH" and press "Enter" to exit.')
            continue
            
        else:
            break
    
    return bool_str_input

###############################################################################

# prompt user input for the path of the folder containing ".dat" files
# and check if it is valid
folderPathStr = is_folderPathStr_valid('Input data folder directory: ')

# use the python "global" module to find all ".dat" files in the given folder
datFileList = glob.glob( path.join(folderPathStr, '*.dat') )

# print out the total # of ".dat" files found in the given folder
print('Found', len(datFileList), '".dat" files in folder', folderPathStr)

# if there are 1 or more ".dat" files, continue; otherwise, stop operation
if len(datFileList) > 0:
    
    # print out each ".dat" filepath to show the user
    for line in datFileList: print(line)

    # variable "dirpath" is the path of the folder containing this script
    dir_path = path.dirname(path.realpath(__file__))

    # create a path for a new folder in which the compressed data will be saved
    npzFolder = path.join(dir_path, 'CompressedNumpyData_' + \
                          path.basename( path.split(folderPathStr)[1] ))
    
    # if the new folder in which compressed data will be saved already exists,
    # cancel the operation & display a message; otherwise, continue
    if not path.exists(npzFolder):
        
        # prompt user input for yes/no decision on 
        # whether or not points with 0mm Z-displacement should be removed
        bool_removeZeroZdisp = is_bool_input_valid( \
        '\nDo you want to remove data where dispZ=0mm? [Yes/No]: ')

        # print out the location of the new folder where compressed data
        # will be saved (same location as this script's path)
        print('\nCompressed numpy files (".npz") will be saved to the folder',\
              npzFolder)
    
        # create the new folder where compressed data will be saved
        os.makedirs(npzFolder)
        
        # loop is iterated over each filepath stored in variable "datFileList"        
        for line in datFileList :
            fileNameNoExtension = path.splitext( path.basename(line) )[0]
            ## splits the actual filename from its extension, e.g.:
            ## "B00001.dat" --> ("B00001", ".dat")
            ## using [0] selects the firt element, "B00001"
        
            datNumpyArray = np.loadtxt(line, skiprows = 3)
            ## load data file into a numpy array
            ## parameter "skiprows" is used to remove headers in ".dat" files
        
            # if user selects "y", remove 0mm Z-displacment data points;
            # otherwise, continue
            if (bool_removeZeroZdisp == 'yes'):
                datNumpyArray = datNumpyArray[ (datNumpyArray[:,2] != 0) \
                                              | (datNumpyArray[:,5] != 0)]
                # the 6th column contains Z-displacement data,
                # the 3rd column contains initial Z data;
                # datNumpyArray = datNumpyArray[ (datNumpyArray[:,2] != 0) \
                #                               | (datNumpyArray[:,5] != 0)]
                # is read as:
                # "keep all rows of 'datNumpyArray' where the number in the
                # 6th column of 'datNumpyArray' is nonzero
                # OR where the number in 3rd column is nonzero"
                
            ## save numbers into a compressed numpy array (headers are removed)
            ## note: "zippedArray" is an arbitrary callback to retrieve data
            np.savez_compressed(path.join(npzFolder, fileNameNoExtension), \
                                zippedArray = datNumpyArray) 

    else:
        # cancel the operation & display a message if the new folder
        # in which compressed data would have been saved already exists
        print('\nThere is already a folder', npzFolder, '\nPlease try again.')    

##=============================================================================
## here is an example on how to retrieve data from the zipped ".npy" files...
## (zipped numpy file extension = ".npz")
#             
#datZippedList = glob.glob( path.join(npzFolder, '*.npz') )
## creates list of strings of zipped numpy filenames that we plan to retrieve
## utilizes the "global" method to find files with ".npz" extension
#
#unzippedDictionary = {} 
## initialize empty dictionary; data will be saved into this variable
#
#for line in datZippedList :
## uncomment these 2 lines for further understanding of file manipulation 
##    print( path.splitext( path.basename(line) )[0] )   
##    print( path.join(dir_path, line) )
#
#    with np.load(path.join(dir_path, line)) as unzipArray:
#        test_Zip_retrieved = unzipArray['zippedArray']
#        ## loads the values into a dictionary-like variable
#        ## called "unzipArray"; this particular syntax using "with" command
#        ## makes sure the associated files saved on disk are closed after use 
# 
#        unzippedDictionary[ path.splitext( path.basename(line) )[0] ] = \
#            unzipArray['zippedArray']   
# 
##    to retrieve data from B00001.npz, use unzippedDictionary['B00001']
##    to retrieve data from B00002.npz, use unzippedDictionary['B00002']
##    etc.
##    this is so we can use the filenames, B00001 etc., as variable names
##=============================================================================

### to do:
### add option to output plots of data in each ".dat" file
### add option to place grid @ Z = 10mm and/or output
### (not entirely necessary but may be a good visual aid)
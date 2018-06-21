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
## """ Bubble Test Data Helper (command line version) """ :
##         File compression;
##             zero-Z-displacement data removal to isolate specimen;
##                 optional plot grid @ apparatus surface 
##                 (work in progress--to be completed)
##=============================================================================
# =============================================================================
#    This function has 1 required argument and 3 optional arguments.

#    Required argument 1, "dataFolderDirectory": 
#        string of the filepath of folder containing TecData ".dat" files.
#        By default, this script will save resulting ".npz" files in a new 
#        folder under the same directory as this script's current directory.

#    Optional Argument 1, "bool_removeZeroZdisp":
#        boolean to turn on/off "dispZ != 0" data removal tool.
#        Setting this to 1 will remove all data points that have an 
#        displaced Z value of 0mm; this removes data with 0 displacement,
#        i.e., data points that are not relevent to the specimen.
#        Setting this to 0 keeps data unaffected. 
#        Default is 0 a.k.a. False.

#    Optional argument 2, "output3Dplot": (work in progress--to be completed)
#        boolean to deliver 3D plots of the displacement field
#        from given TecData, which will be saved in ".png" format
#        in the same location as the compressed ".npz" files.
#        Default is 0 a.k.a. False.

#    Optional argument 3: "plotSurfaceGrid" (work in progress--to be completed)
#        boolean to turn on/off grid representing apparatus surface @ Z=10mm. 
#        This grid is added to the 3D plots as a visual aid,
#        replacing the data points where Z displacement = 0mm.
#        Default is 0 a.k.a. False.
#        If optional argument 2 "output3Dplot" is 0,
#        OR if optional argument 1 "bool_removeZeroZdisp" is 0,
#        then this option is also 0 by default, regardless of cmd line input.
# =============================================================================

###############################################################################
##=============================================================================
## How to use cmd_BubbleDataHelper:
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
## -> type "python cmd_BubbleDataHelper.py arg1 arg2 arg3 arg4" 
##    where "arg1", "arg2", "arg3", and "arg4" are replaced with the
##    correct argument inputs as described in the previous section:
##    
##    --> "arg1" is "dataFolderDirectory", a string of the file path of the 
##        folder that contains the ".dat" files to be compressed;
##        e.g.: C:\temp\Example
##
##    --> "arg2" is "bool_removeZeroZdisp", a boolean that decides whether 
##        or not to remove data points where Z displacement is 0mm;
##        use 1 for true, 0 for false; if no input is given, the script
##        will use default value of 0
##    
##    --> "arg3" is "output3Dplot", a boolean that decides whether or not to    
##        output plots of the given data, which will be saved in ".png" format
##        in the same location as the compressed ".npz" files;
##        use 1 for true, 0 for false; if no input is given, the script
##        will use default value of 0
##        (work in progress--to be completed)
##
##    --> "arg4" is "plotSurfaceGrid", a boolean that decides whether or not
##        to include a 2D grid representing the apparatus surface @ Z=10mm;        
##        use 1 for true, 0 for false; as said earlier,
##        if "bool_removeZeroZdisp"=0 or "output3Dplot"=0, the script
##        will use default value of 0; also, if no input is given, the script
##        will use default value of 0
##        (work in progress--to be completed)
##         
##    e.g., if you wish to compress files in the folder "C:\temp\Example",      
##    and you wish to remove data points where Z displacement is 0mm,
##    and you wish to output 3D plots of the data,
##    and you wish to include a 2D grid at the apparatus surface,
##    type the following:
##
##    python cmd_BubbleDataHelper.py C:\temp\Example 1 1 1
## 
## -> press "enter"
##
##
##    note: if there are spaces within folder names in the necessary paths, 
##          you may use quotation marks to avoid errors, e.g., instead of 
##          cd C:\temp\Example with Space\Example, you can use
##          cd C:\temp\"Example with Space"\Example, or
##          cd "C:\temp\Example with Space\Example" 
##
##    note: this function will also work using "True", "T", or "t" for 1
##          & "False", "F", or "f" for 0)
##
##    note: for the work-in-progress sections, the arguments will be unused
##          until the coding is completed
##=============================================================================
###############################################################################

import sys
import os
import os.path as path
import glob
import numpy as np

# this function evaluates the given folder path argument, dataFolderDirectory,
# to determine if it is valid
def is_folderPathStr_valid(folderPath):
    try:
        folderPath = folderPath.strip() # (remove unnecessary spaces)
        
        if not path.isdir(folderPath):
            print('Sorry, that is not a valid folder directory. ')
            print('Cancelling operation...\n')
            sys.exit()
    
    except ValueError:
        print('Unknown error encountered.\n')
        print('Cancelling operation...\n')
        sys.exit()
        
    return folderPath

# this function validates the various forms of the boolean inputs (str or int)
# and returns True or False values, strictly of type "bool";
# default values of False are enforced if nonsense string inputs are given
def parse_boolean(arg):
    try:
        # from the command line, arguments are passed strictly as strings... 
        if type(arg) == str:
            arg = arg.strip() # (remove unnecessary spaces)
            arg = arg.lower() # (change all capital letters to lowercase)
            arg = (arg in ['1', 'true', 't']) 
            # (if the argument equals '1', 'true', or 't', then it is True;
            #  otherwise, False)
        
        # ...but in the event that this code receives booleans or integers 
        # as arguments in future use, this parser will handle those cases: 
        elif ( type(arg) == bool ) | ( type(arg) == int ):
            arg = bool(arg)
            # bool(1) and bool(True) will both result in True;
            # bool(0) and bool(False) will both result in False
            
    except ValueError:
        print('Error encountered when parsing boolean arguments.')
        print('Cancelling operation...\n')
        sys.exit()
    
    return arg

# the function below checks the input arguments and cancels the operation 
# if the arguments cause unexpected errors, or if no arguments are given;
# otherwise, the script continues
def check_given_arguments():
    try:
        # from the command line, a string of the script's name is automatically 
        # assigned as the first element of "sys.argv", 
        # i.e., sys.argv[0] = 'cmd_BubbleDataHelper.py';
        # if the length of sys.argv is 1, then no arguments were given,
        # and the operation will be cancelled.
        if len(sys.argv) == 1:
            print('Error encountered: no arguments given.')
            print('Cancelling operation...\n')
            sys.exit()
        
        elif len(sys.argv) == 2:
            dataFolderDirectory = is_folderPathStr_valid(sys.argv[1])
            # with only 1 argument given, 
            # the optional arguments default to False:
            bool_removeZeroZdisp = False
            output3Dplot = False
            plotSurfaceGrid = False
        
        elif len(sys.argv) == 3:
            dataFolderDirectory = is_folderPathStr_valid(sys.argv[1])           
            bool_removeZeroZdisp = parse_boolean(sys.argv[2])
            # with 2 arguments given, 
            # the rest of the optional arguments default to False:
            output3Dplot = False
            plotSurfaceGrid = False

        elif len(sys.argv) == 4:
            dataFolderDirectory = is_folderPathStr_valid(sys.argv[1])
            bool_removeZeroZdisp = parse_boolean(sys.argv[2])
            output3Dplot = parse_boolean(sys.argv[3])
            # with 3 arguments given, 
            # the rest of the optional arguments default to False:
            plotSurfaceGrid = False
            
        elif len(sys.argv) >= 5:
            # with all arguments given, the script assigns arguments properly;
            # any other additional arguments provided will be ignored 
            dataFolderDirectory = is_folderPathStr_valid(sys.argv[1])
            bool_removeZeroZdisp = parse_boolean(sys.argv[2])
            output3Dplot = parse_boolean(sys.argv[3])
            plotSurfaceGrid = parse_boolean(sys.argv[4])

    except ValueError:
        print('Error encountered when parsing arguments.')
        print('Cancelling operation...\n')
        sys.exit()
        
    return [dataFolderDirectory, bool_removeZeroZdisp, \
            output3Dplot, plotSurfaceGrid]

###############################################################################

# run the "check_given_arguments()" function to check the given arguments;
# operation will either continue with the proper arguments as given
# or end without further action        
[dataFolderDirectory, bool_removeZeroZdisp, output3Dplot, plotSurfaceGrid] = \
    check_given_arguments()

# if output3Dplot is False, or if bool_removeZeroZdisp is False,
# then plotSurfaceGrid must be false by default, regardless of user input:
if not bool_removeZeroZdisp : plotSurfaceGrid = False
if not output3Dplot : plotSurfaceGrid = False

# use the python "global" module to find all ".dat" files in the given folder
datFileList = glob.glob( path.join(dataFolderDirectory, '*.dat') )

# print out the total # of ".dat" files found in the given folder
print('Found', len(datFileList), '".dat" files in folder', dataFolderDirectory)

# if there are 1 or more ".dat" files, continue; otherwise, stop operation
if len(datFileList) > 0:
    
    # print out each ".dat" filepath to show the user
    for line in datFileList: print(line)

    # variable "dirpath" is the path of the folder containing this script
    dir_path = path.dirname(path.realpath(__file__))

    # create a path for a new folder in which the compressed data will be saved
    npzFolder = path.join(dir_path, 'CompressedNumpyData_' + \
                          path.basename( path.split(dataFolderDirectory)[1] ))
    
    # if the new folder in which compressed data will be saved already exists,
    # cancel the operation & display a message; otherwise, continue
    if not path.exists(npzFolder):
        
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
        
            # if argument "bool_removeZeroZdisp" is True,
            # remove 0mm Z-displacment data points;
            # otherwise, continue without affecting data
            if bool_removeZeroZdisp:
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
        print('Cancelling operation...\n')

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

#### to do:
### add option to output plots of data in each ".dat" file
### add option to place grid @ Z = 10mm and/or output 
### (not entirely necessary but may be a good visual aid )
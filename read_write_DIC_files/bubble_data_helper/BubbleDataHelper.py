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
##=============================================================================
# =============================================================================
#    This function has 1 required argument and 3 optional arguments.

#    Required argument 1, "dataFolder": 
#        string of the filepath of folder containing TecData ".dat" files.
#        By default, this script will save resulting ".npz" files in a new 
#        folder under the same directory as this script's current directory.

#    Optional Argument 1, "removeZeroZ":
#        boolean to turn on/off "dispZ != 0" data removal tool.
#        Setting this to 1 will remove all data points that have an 
#        displaced Z value of 0mm; this removes data with 0 displacement,
#        i.e., data points that are not relevent to the specimen.
#        Setting this to 0 keeps data unaffected. 
#        Default is 0 a.k.a. False.

#    Optional argument 2, "outputPlot": (work in progress--to be completed)
#        boolean to deliver 3D plots of the displacement field
#        from given TecData, which will be saved in ".png" format
#        in the same location as the compressed ".npz" files.
#        Default is 0 a.k.a. False.

#    Optional argument 3: "surfaceGrid" (work in progress--to be completed)
#        boolean to turn on/off grid representing apparatus surface @ Z=10mm. 
#        This grid is added to the 3D plots as a visual aid,
#        replacing the data points where Z displacement = 0mm.
#        Default is 0 a.k.a. False.
#        If optional argument 2 "outputPlot" is 0,
#        OR if optional argument 1 "removeZeroZ" is 0,
#        then this option is also 0 by default, regardless of cmd line input.
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
## -> type 
##
##    python BubbleDataHelper.py --dataFolder arg1 --removeZeroZ arg2
##    --outputPlot arg3 --surfaceGrid arg4 
##
##    where "arg1", "arg2", "arg3", and "arg4" are replaced with the
##    correct argument inputs as described in the previous section:
##    
##    --> "arg1" is "dataFolder", a string of the file path of the 
##        folder that contains the ".dat" files to be compressed;
##        e.g.: C:\temp\Example
##
##    --> "arg2" is "removeZeroZ", a boolean that decides whether 
##        or not to remove data points where Z displacement is 0mm;
##        use 1 for true, 0 for false; if no input is given, the script
##        will use default value of 0
##    
##    --> "arg3" is "outputPlot", a boolean that decides whether or not to    
##        output plots of the given data, which will be saved in ".png" format
##        in the same location as the compressed ".npz" files;
##        use 1 for true, 0 for false; if no input is given, the script
##        will use default value of 0
##
##    --> "arg4" is "surfaceGrid", a boolean that decides whether or not
##        to include a 2D grid representing the apparatus surface @ Z=10mm;        
##        use 1 for true, 0 for false; as said earlier,
##        if "removeZeroZ"=0 or "outputPlot"=0, the script
##        will use default value of 0; also, if no input is given, the script
##        will use default value of 0
##         
##    e.g., if you wish to compress files in the folder "C:\temp\Example",      
##    and you wish to remove data points where Z displacement is 0mm,
##    and you wish to output 3D plots of the data,
##    and you wish to include a 2D grid at the apparatus surface,
##    type the following:
##
##    python BubbleDataHelper.py --dataFolder C:\temp\Example
##    --removeZeroZ 1 --outputPlot 1 --surfaceGrid 1
## 
## -> press "enter"
##
##
##    note: the arguments can be given in any order, for example...
##          python cmd_BubbleDataHelper.py --surfaceGrid 1 --outputPlot 1 
##          --removeZeroZ 1 --dataFolder C:\temp\Example
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
import argparse
import glob
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# this function evaluates the given folder path argument, dataFolder,
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
        # from the command line, the argument parser will interpret the 
        # given arguments as strings; if the required argument (dataFolder) 
        # is not given, then an error message is shown,
        # and the operation will be cancelled.
        
        parser = argparse.ArgumentParser()
        parser.add_argument('--dataFolder', required=True)
        parser.add_argument('--removeZeroZ', default=False)
        parser.add_argument('--outputPlot', default=False)
        parser.add_argument('--surfaceGrid', default=False)
        
        args = parser.parse_args()
        
        argDictionary= {'dataFolder' : args.dataFolder,
                        'removeZeroZ' : args.removeZeroZ,
                        'outputPlot' : args.outputPlot,
                        'surfaceGrid' : args.surfaceGrid} 
        
        # the code continues only if the required dataFolder argument is given        
        dataFolder = is_folderPathStr_valid(argDictionary['dataFolder'])
            
        if argDictionary['removeZeroZ'] is None:
            removeZeroZ = False
        else:
            removeZeroZ = parse_boolean(argDictionary['removeZeroZ'])

        if argDictionary['outputPlot'] is None:
            outputPlot = False
        else:
            outputPlot = parse_boolean(argDictionary['outputPlot'])
                
        if argDictionary['surfaceGrid'] is None:
            surfaceGrid = False
        else:
            surfaceGrid = parse_boolean(argDictionary['surfaceGrid'])

    except ValueError:
        print('Error encountered when parsing arguments.')
        print('Cancelling operation...\n')
        sys.exit()
        
    return [dataFolder, removeZeroZ, outputPlot, surfaceGrid]

###############################################################################

# run the "check_given_arguments()" function to check the given arguments;
# operation will either continue with the proper arguments as given
# or end without further action        
[dataFolder, removeZeroZ, outputPlot, surfaceGrid] = check_given_arguments()
dataFolder = path.normpath(dataFolder)

# if outputPlot is False, or if removeZeroZ is False,
# then surfaceGrid must be false by default, regardless of user input:
if not removeZeroZ : surfaceGrid = False
if not outputPlot : surfaceGrid = False

# use the python "global" module to find all ".dat" files in the given folder
datFileList = glob.glob( path.join(dataFolder, '*.dat') )

# print out the total # of ".dat" files found in the given folder
print('\nFound', len(datFileList), '".dat" files in folder', dataFolder)

###############################################################################        
# if there are 1 or more ".dat" files, continue; otherwise, stop operation
if len(datFileList) > 0:
    
    # print out each ".dat" filepath to show the user
    for line in datFileList: print(line)

    # variable "dirpath" is the path of the folder containing this script
    dir_path = path.dirname(path.realpath(__file__))

    # create a path for a new folder in which the compressed data will be saved
    npzFolder = path.join(dir_path, 'CompressedNumpyData_' + \
                          path.basename(dataFolder) )
    
#==============================================================================
    # if the new folder in which compressed data will be saved already exists,
    # cancel the operation & display a message; otherwise, continue
    if not path.exists(npzFolder):
        
        # print out the location of the new folder where compressed data
        # will be saved (same location as this script's path)
        print('\nCompressed numpy files (".npz") will be saved to the folder',\
              npzFolder)
    
        # create the new folder where compressed data will be saved
        os.makedirs(npzFolder)
        
###############################################################################
        # if argument "outputPlot" is True, create the folders 
        # in which plots are to be saved
        if outputPlot:
            plotFolder = path.join(dir_path, 'Plots_' + \
                                   path.basename( dataFolder ) )
            if not path.exists(plotFolder):
                os.makedirs(plotFolder)
                print('\nDefault plots will be saved in the folder', \
                      plotFolder)
                plotFolderAlreadyExists = False
            else:
                print('\nThere is already a folder', plotFolder)
                print('No default plots will be saved.')
                plotFolderAlreadyExists = True
            
            plotHQFolder = path.join(dir_path, 'PlotsHQ_' + \
                                     path.basename( dataFolder ) )
            if not path.exists(plotHQFolder):
                os.makedirs(plotHQFolder)
                print('\nHigh-quality plots will be saved in the folder', \
                      plotHQFolder)
                plotHQFolderAlreadyExists = False
            else:
                print('\nThere is already a folder', plotHQFolder)
                print('No high-quality plots will be saved.')
                plotHQFolderAlreadyExists = True
###############################################################################

#==============================================================================
        # loop is iterated over each filepath stored in variable "datFileList"        
        for line in datFileList :
            fileNameNoExtension = path.splitext( path.basename(line) )[0]
            ## splits the actual filename from its extension, e.g.:
            ## "B00001.dat" --> ("B00001", ".dat")
            ## using [0] selects the firt element, "B00001"
        
            datNumpyArray = np.loadtxt(line, skiprows = 3)
            ## load data file into a numpy array
            ## parameter "skiprows" is used to remove headers in ".dat" files

###############################################################################        
            # if argument "removeZeroZ" is True,
            # remove 0mm Z-displacment data points;
            # otherwise, continue without affecting data
            if removeZeroZ:
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

###############################################################################                
            # if argument "outputPlot" is True, save plots in .png format
            # otherwise, continue without affecting data
            if outputPlot:
                if not (plotFolderAlreadyExists & plotHQFolderAlreadyExists):
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                
                    X = datNumpyArray[:,0]
                    Y = datNumpyArray[:,1]
                    Z = datNumpyArray[:,2]
                    dispX = datNumpyArray[:,3]
                    dispY = datNumpyArray[:,4]
                    dispZ = datNumpyArray[:,5]
                    
                    finalX = X+dispX
                    finalY = Y+dispY
                    finalZ = Z+dispZ
                    
                    ax.scatter(finalX, finalY, finalZ, zdir='z',\
                               s=.2, c='b', depthshade=False, edgecolor='')
                    
                    if len(datNumpyArray) > 0: 
                        xMin = np.round( np.min(finalX) )
                        xMax = np.round( np.max(finalX) ) 
                        yMin = np.round( np.min(finalY) )
                        yMax = np.round( np.max(finalY) ) 
                        zMin = np.round( np.min(finalZ) )
                        zMax = np.round( np.max(finalZ) ) 
                        ax.set_xlim3d( xMin-5, xMax+5 ) 
                        ax.set_ylim3d( yMin-5, yMax+5 )
                        ax.set_zlim3d( zMin-5, zMax+5 )
                    else:
                        xMin = -100; xMax = 100
                        yMin = -100; yMax = 100
                        zMin = -8; zMax = 50
                        ax.set_xlim3d(xMin, xMax)
                        ax.set_ylim3d(yMin, yMax)
                        ax.set_zlim3d(zMin, zMax)
                        
                    ax.set_xlabel('X (mm)')
                    ax.set_ylabel('Y (mm)')
                    ax.set_zlabel('Z (mm)')

###############################################################################                   
                    # if argument "surfaceGrid" is True, add a 2D grid @ Z=10mm
                    # otherwise, continue without affecting data
                    if surfaceGrid:
                        x_surf=np.arange(xMin-5, xMax+5, 1)
                        y_surf=np.arange(yMin-5, yMax+5, 1)
                        x_surf, y_surf = np.meshgrid(x_surf,y_surf,sparse=True)
                        z_surf = 10             
                        ax.plot_wireframe(x_surf, y_surf, z_surf, color='k', \
                                          linewidth=0.5, linestyle='--', \
                                          rcount=10, ccount=10)
                        
###############################################################################                    
                ## save plot: default size & resolution
                if not (plotFolderAlreadyExists):
                    plt.savefig(path.join(plotFolder, \
                                          fileNameNoExtension+'.png'), \
                                bbox_inches='tight', dpi=100)
                
                ## save plot: high-quality size & resolution
                if not (plotHQFolderAlreadyExists):
                    ## sets the dimensions of the high-quality image;
                    ## the dimensions [13.66,7.02] are in inches
                    ## and were chosen as a suitable high-definition size
                    fig.set_size_inches(np.array([13.66,7.02]))
                    plt.savefig(path.join(plotHQFolder, \
                                      fileNameNoExtension+'_HQ.png'), \
                            bbox_inches='tight', dpi=300)
            
###############################################################################                
            ## save numbers into a compressed numpy array (headers are removed)
            ## note: "zippedArray" is an arbitrary callback to retrieve data
            np.savez_compressed(path.join(npzFolder, fileNameNoExtension), \
                                zippedArray = datNumpyArray) 
                
#==============================================================================
## end of "for line in datFileList" loop            
#==============================================================================
            
###############################################################################        
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
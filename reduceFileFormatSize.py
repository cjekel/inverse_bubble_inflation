##    reducing filesize/memory of bubble test data .dat files...
##    run this script in the same folder as file 'B00015.dat'

from time import time
t0 = time()

"""
OPTION 1: 'np.loadtxt'; skip first 3 rows to avoid headers & string error
"""
import numpy as np

dicFile = 'B00015.dat'

test1 = np.loadtxt(dicFile, skiprows = 3)
np.save('testResult1.npy', test1)
test1_retrieved = np.load('testResult1.npy')

##    note: 'np.genfromtxt' accomplishes the same thing,
##    and can handle any possible blank elements in the data:
#test1 = np.genfromtxt(dicFile, skip_header = 3)
#np.save('testResult1.npy', test1)

t1 = time()
print('run time in seconds, option 1:', t1-t0)


"""
OPTION 2: utilizing 'np.memmap', memory mapping, along with option 1...
(unfortunaely, this resulted in essentially the same process as option 1;
feel free to ignore)
"""
import os.path as path
newFilePath = path.dirname(path.abspath(dicFile))
newFilePath = path.join(newFilePath,'testResult2.npy')
##    dependent on option 1 due to 'shape' parameter & headings
fp = np.memmap(newFilePath, dtype='float32', mode='w+', shape=np.shape(test1))
fp[:] = test1[:]
#  from documentation...
#  Deletion flushes memory changes to disk before removing the object:
del fp
# information is retrievable and we can specify read/write priveleges
newfp = np.memmap(newFilePath, dtype='float32', mode='r', \
                  shape=np.shape(test1))
##    comment out the line below to see newfp object has desired values,
##    accurate to 5 decimal places: 
del newfp

t2 = time()
print('run time in seconds, option 2:', t2-t0)

"""
cons: can only save memory space if dtype='float32', 
      file size is the same with the preferred dtype='float64'; 
      basically all this does is reduce data from 64bit to 32 bit floats,
      it's equivalent to option 1 with parameter dtype='float32':
      test1 = np.loadtxt(dicFile, dtype='float32', skiprows = 3)    

pros: data is still accurate to 5 decimal places;
      file size of 'testResult2.npy', half that of 'testResult1.npy';
      additional runtime negligible compared to option 1;
      maybe temp folder / temp files could be utilized? 
      
see documentation:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html
"""


"""
OPTION 3: utilizing 'numpy.savez_compressed', along with option 1...
(this one might be the winner!! down from 15 MB to 3 MB)
"""

np.savez_compressed('testResult3.npz', zippedArray = test1)
unzipArray = np.load('testResult3.npz')
test3_retrieved = unzipArray['zippedArray']

t3 = time()
print('run time in seconds, option 3:', (t3-t0) - (t2-t1) )

"""NOTE: option 3 has non-negligible additional runtime"""

##    Other notes:
##    consider using the %timeit command:
#%timeit np.random.random(200)
# 
##    python 'pickle' is also still an explorable option
#
##    perhaps look into faster functions besides numpy.save

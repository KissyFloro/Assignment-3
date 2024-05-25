#  Load data from files using numpy

# Example 1: load single array in .npy file
import numpy as np
data = np.load('array1.npy')
print('Loaded Array:', data)
 
# Example 2: load multiple array in .npz file
import numpy as np
data = np.load('arrays.npz')
a1 = data['a1']
a2 = data['a2']

print('Array 1:', a1)
print('Array 2:', a2)

# Example 3: load data from text file
import numpy as np
data = np.loadtxt('array.txt')
print('Loaded Array from text file:', data)

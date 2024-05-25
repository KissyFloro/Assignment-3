# Saving and Writing files using Numpy

# Example 1: Using .npy file - to save single numpy array
import numpy as np
array1 = np.array([11,16,4,9,8,3])
np.save('array1.npy', array1)


# Example 2: Using .npz file - to save multiple array
# import numpy as np
# a1 = np.array([7,9,12,21,8,42,5])
# a2 = np.array([16,2,8,5,11,34,9])
# np.savez('arrays.npz', a1=a1, a2=a2)


#  Example 3: save as text file
# import numpy as np 
# array = np.array([[3,7,9,2,0], [12,5,11,10,6]])
# np.savetxt('array.txt', array)


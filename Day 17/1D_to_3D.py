#onvert 1D array with 8 elements to 3D array with 2x2 elements

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
array_3D=arr.reshape((2,2,2))
print("1D array to 3D array:",array_3D)
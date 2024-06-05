import numpy as np

#shape of 1D array
arr=np.array([5,9,8,6,1,6])
print("array 1D : ",arr)
print("shape of array 1D : ",arr.shape)

#reshape 1D to 2D 
arr1=arr.reshape((2,3))
print("reshaped 2D array :",arr1)
print("shape of the 2D array:",arr1.shape)

#reshape 1d to 3d
arr2=arr.reshape((3,2))
print("reshaped 3D array :",arr2)
print("shape of the 3D array:",arr2.shape)

#reshape 3d to 1d
arr2_arr=arr2.reshape((1,6))
print("reshaped 3D to 1D array :",arr2_arr)
print("shape of the 3D to 1D array:",arr2_arr.shape)

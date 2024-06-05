import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
concat_array=np.concatenate((arr1,arr2))
print("joined array :",concat_array)

#join multidimensional array
arr2D_1=np.array([[2,4,6],[5, 7,8]])
arr2D_2=np.array([[3,4,2],[6,45,43]])

#vertically
vstack_array=np.vstack((arr2D_1,arr2D_2))
print("vertical stacked array:",vstack_array)

#horizontally
hstack_array=np.hstack((arr2D_1,arr2D_2))
print("horizontally stacked array:",hstack_array)
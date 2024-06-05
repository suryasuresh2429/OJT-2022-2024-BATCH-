import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
split_array=np.split(arr,3)
print("split array:",split_array)

#multidimensional
#horizontally and vertically 
arr2D=np.array([[1,2,3],[4,5,6]])
vsplit_array=np.vsplit(arr2D,2)
print("vertically splited array:",vsplit_array)
hsplit_array=np.hsplit(arr2D,3)
print("horizontally splited array:",hsplit_array)


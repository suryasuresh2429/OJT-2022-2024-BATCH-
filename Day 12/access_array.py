import numpy as np

array_2D=np.array([[1,2,3],[4,5,6]])

#accessing a single element
element=array_2D[1,2]
print("element of [1,2] : ",element)

#access by 2 row
row =array_2D[0,:]
print("first row : ",row)

#access by column
column=array_2D[:,1]
print("second column :",column)

#slicing
slice_array=array_2D[0:2,1:3]
print("sliced array : ",slice_array)


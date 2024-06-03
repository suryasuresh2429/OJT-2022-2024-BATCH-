import numpy as np

original_array=np.array([1,2,3,4,5])
print("original array : ",original_array)

#view for the array
view_array=original_array.view()
print("view of the original array:",view_array)

view_array[2]=30
print("modified view:",view_array) #the changes that has made in view will reflect on the original array too
print("original array after modifying it:" ,original_array)

copy_array=original_array.copy()
print("copy array:",copy_array)

#modify element in copy_array
copy_array[0]=34
print("modified copy_array:",copy_array) #in the case copy_array the changes won't make any reflection in the original array
print("original array after modifying it:",original_array)

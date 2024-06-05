import numpy as np

arr=np.array([1,2,3,5,6])
print("1d array:",arr)

for elements in arr:
    print(elements)

#iterating 3d array with for-in loop
arr_2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D array:",arr_2D)
for i in arr_2D:
    for j in i:
        print(j)


#iteration using nditer()
for elements in np.nditer(arr_2D):
    print(elements)

#iterate the elements with index
for index,element in np.ndenumerate(arr_2D):
    print(f"index:{index},element:{element}")
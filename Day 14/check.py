import numpy as np

#elements greater than 15 using where()
arr=np.array([10,20,30,40,50,60])
# elements=np.where(arr>15)
elements=np.where(arr>15,0,arr)
# print("elements",arr[elements])
print(elements)

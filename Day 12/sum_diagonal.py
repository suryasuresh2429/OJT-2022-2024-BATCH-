import numpy as np

arr = np.array([[1,2,8,9],[4,5,0,2],[7,8,4,3]])
sum_diagonal_arr = np.trace(arr)
print("Sum of the diagonal elements of the 4x4 matrix:", sum_diagonal_arr)

arr1=np.array([[2,3,5],[8,6,9],[6,4,8]])
sum_diagonal_arr1 = np.trace(arr1)
print("Sum of the diagonal elements of the 3x3 matrix:", sum_diagonal_arr1)
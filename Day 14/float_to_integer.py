#Change data type from float to integer by using 'i' as parameter value
import numpy as np

float_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
int_array = float_array.astype('i')

print(f'Original array: {float_array}')
print(f'Converted array: {int_array}')
print(f'Data type of the converted array: {int_array.dtype}')

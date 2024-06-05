#Change data type from integer to boolean
import numpy as np

int_array = np.array([0, 1, 2, 0, 5])
bool_array = int_array.astype(bool)

print(f'Original array: {int_array}')
print(f'Converted array: {bool_array}')
print(f'Data type of the converted array: {bool_array.dtype}')

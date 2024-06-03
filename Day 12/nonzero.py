import numpy as np

# Example array
array = np.array([0, 1, 2, 0, 3, 7, 4])

# Count the number of non-zero values
non_zero_count = np.count_nonzero(array)

print(f'The number of non-zero values in the array is: {non_zero_count}')

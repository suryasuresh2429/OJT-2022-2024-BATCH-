# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4

import numpy as np
a = np.array([1,2,3,4], ndmin=5)
print(a.shape)
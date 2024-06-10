#A scatter plot with 1000 dots

import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(1000)
y=np.random.rand(1000)
plt.scatter(x,y,color="blue")
plt.show()
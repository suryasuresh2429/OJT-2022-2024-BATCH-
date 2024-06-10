#Use the scatter() method to draw a scatter plot diagram

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5,6])
y=np.array([1,4,9,16,25,36])
plt.scatter(x,y,color="red")
plt.show()

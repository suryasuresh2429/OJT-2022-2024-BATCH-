import numpy as np
from sklearn.linear_model import LinearRegression
import  matplotlib.pyplot as plt

height=np.array([150,160,164,165,173]).reshape(-1,1)
weight=np.array([50,65,63,68,72]).reshape(-1,1)

model=LinearRegression()
model.fit(height,weight)

predicted_weight=model.predict(height)
print(f'intercept:{model.intercept_}')
print(f'coefficients:{model.coef_[0]}')

plt.scatter(height,weight,color='red')
plt.plot(height,predicted_weight, color='blue')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Linear Regression')
plt.show()


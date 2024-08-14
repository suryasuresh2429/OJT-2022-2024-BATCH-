import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Conv2D,MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#load the MNIST dataset

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#normalize the dataset
x_train,x_test=x_train/255.0,x_test/255.0

#reshape the data for CNN
x_train_cnn=x_train.reshape(-1,28,28,1)
x_test_cnn=x_test.reshape(-1,28,28,1)

y_train_oh=to_categorical(y_train,10)
y_test_oh=to_categorical(y_test,10)

ann_model=Sequential([
    Flatten(input_shape=(28,28)),


#first hidden layer
Dense(128,activation='relu'),

#second hidden layer
Dense(64,activation='relu'),

Dense(10,activation='softmax')
])
#compile the model 
ann_model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

#train ANN model
ann_model.fit(x_train,y_train_oh,epochs=5,batch_size=32,validation_data=(x_test,y_test_oh))

#build the CNN model
#first convolutional layer
cnn_model=Sequential([Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),

#pool layer
MaxPooling2D((2,2)),
#second cn layer and pool layer
Conv2D(64,(3,3),activation='relu'),
MaxPooling2D((2,2)),
#flattened the features to 1 dimension vector
Flatten(),
#fully connected layer
Dense(64,activation='relu'),
#output layer
Dense(10,activation='softmax')
])

#compile our model
cnn_model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

#train ANN model
cnn_model.fit(x_train,y_train_oh,epochs=5,batch_size=32,validation_data=(x_test,y_test_oh))

#build the model with KNN
x_train_knn=x_train.reshape(-1,28*28)
x_test_knn=x_test.reshape(-1,28*28)

#standardization of the data
scaler=StandardScaler()
x_train_knn=scaler.fit_transform(x_train_knn)
x_test_knn=scaler.transform(x_test_knn)

#create the model
knn_model=KNeighborsClassifier(n_neighbors=3)

#train the model
knn_model.fit(x_train_knn,y_train)

knn_accuracy=knn_model.score(x_test_knn,y_test)

print(f"knn accuracy:{knn_accuracy*100:.2f}%")

#prediction with CNN
prediction=cnn_model.predict(x_test_cnn)

for i in range(5):
    plt.imshow(x_test[i],cmap='grey')
    plt.title(f"true:{y_test[i]},predicted:{np.argmax(prediction[i])}")
    plt.show()

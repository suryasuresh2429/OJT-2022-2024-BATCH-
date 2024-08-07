#
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#create simple data
reviews=[
    "i love the movie, it was good",
    "the movie was boring",
    "excellent movie, actors done well",
    "it was a normal movie, nothing special"
]

labels=[1,0,1,2]

#create vectorization for the above

vectorizer=CountVectorizer()
x=vectorizer.fit_transform(reviews)
y=np.array(labels)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#create our model
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print("accuracy:",accuracy)

#create a sample review for the prediction
new_review=["i really enjoyed the movie"]
new_review_vector=vectorizer.transform(new_review)
predict=model.predict(new_review_vector)
print("prediction:",predict)

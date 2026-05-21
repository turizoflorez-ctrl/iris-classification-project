import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

st.title("Iris Classification Dashboard")

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

st.subheader("Dataset Iris")

df = pd.DataFrame(X, columns=iris.feature_names)
st.write(df.head())

sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 3.0, 1.0)

prediction = model.predict([[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]])

st.write("Prediction:", iris.target_names[prediction][0])

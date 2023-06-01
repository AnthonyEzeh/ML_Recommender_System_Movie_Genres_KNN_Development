from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
import pandas as pd

# Load the CSV file

X = pd.read_csv("genres.csv")

y = pd.read_csv("popularity.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

st.title("Evaluating KNN Performance in Movie Recommender System")

# Get user input for number of neighbors
n_neighbors = st.slider("Number of neighbors:", 2, 30, 10, 1)

# Fit a KNN model to the training data
knn = KNeighborsClassifier(n_neighbors=n_neighbors)
knn.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = knn.predict(X_test)

# Calculate the evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


# Print the evaluation metrics
st.write("Evaluation Metrics for k =", n_neighbors)
st.write("Accuracy:", accuracy)
st.write("Precision:", precision)
st.write("Recall:", recall)
st.write("F1-score:", f1)

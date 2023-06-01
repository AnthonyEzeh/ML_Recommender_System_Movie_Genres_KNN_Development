import streamlit as st
import pickle 
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np
import time

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie, n_neighbors=5):
    movie_index = movies[movies["title"] == movie].index[0]
    distances, indices = knn.kneighbors(similarity[movie_index].reshape(1, -1), n_neighbors=n_neighbors+1)
    indices = indices.flatten()
    
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_genres = []
    for i in indices[1:]:
        movie_id = movies.iloc[i].movie_id
        recommended_movies.append(movies.iloc[i].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_genres.append(genres[i]) # corrected attribute name
    return recommended_movies[:n_neighbors], recommended_movies_posters[:n_neighbors], recommended_movies_genres[:n_neighbors]

movies_dict = pickle.load(open("movie_dick.pkl","rb"))
movies = pd.DataFrame(movies_dict)

# genres = pickle.load(open("genres.pkl"), "rb")
genres = pickle.load(open("genres.pkl", "rb"))


similarity = pickle.load(open("similarity.pkl", "rb"))

knn = NearestNeighbors(metric="cosine", algorithm="brute")
knn.fit(similarity)


st.balloons()


st.title("Movie Genre Recommender System")

selected_movie_name = st.selectbox(
    "Choose a movie to see similar movies:", 
    movies["title"].values)

n_neighbors = st.slider("Number of neighbors:", 2, 30, 10, 1)

if st.button("Recommend"):
    with st.spinner('Loading...'):
        names, posters, genres = recommend(selected_movie_name, n_neighbors=n_neighbors)
        
        num_cols = len(names)
        cols = st.columns(num_cols)
        for i, col in enumerate(cols):
            with col:
                st.text(names[i])
                st.text(genres[i]) 
                st.image(posters[i])

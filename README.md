## 1: Setting up the environment

First, you need to configure the environment. I suggest using `virtualenv` and `pip` to set up the environment:

```

virtualenv movie-genre-implementation

source movie-genre-implementation/bin/activate

pip install -r requirements.txt

Run
streamlit run RQ1-recommend-movie.py
streamlit run RQ2-evaluate-movie.py
streamlit run RQ3-movie-genre.py
```

Then make sure that Jupyter is running in the `venv` environment. One way to guarantee that this is the case is to run `jupyter notebook` after `pip` has finished installing the packages.

# 2: Developing Machine Learning-based recommender System on Movie Genres using KNN

## Background

This thesis provides an overview of movie recommendation systems and their relevance in helping users find movies that match their tastes. It highlights the three main approaches to recommendation systems: collaborative filtering, content-based filtering, and hybrid systems. The use of ML in designing and developing a movie recommendation system is discussed, and various studies that have explored Artificial Intelligence (AI) methods to solve movie recommendation problems are presented. The thesis also discusses the challenges of data sparsity and cold start problems in recommendation systems and various machine learning algorithms, including collaborative filtering, matrix factorization, content-based filtering, and hybrid recommender systems, that have been used to tackle them. Machine learning
algorithms, such as collaborative filtering, content-based filtering, and hybrid systems, have been widely used to address data sparsity and cold start problems in recommender systems. KNN has been utilized in several studies to recommend items based on similarities between users and items. However, there is a lack of studies using KNN with a focus on interest genres, and the goal is to create a machine learning-based movie recommender system using the KNN algorithm to suggest similar movies based on userselected genres on a Streamlit app. This will provide personalized recommendations for movie
enthusiasts.

## Problem

The thesis discusses the common cold start problem in recommender systems, where new users with new profiles make it difficult to provide recommendations. Although hybrid techniques have been implemented to address this issue, there is a lack of studies that use the KNN algorithm with a focus on interest genres in overcoming data sparsity and cold start problems. Another aspect of movie recommendation that is often overlooked is the role of movie popularity in content-based filtering, where the popularity of movie genres based on their content is poorly understood. Understanding the popularity of movie genres based on content can provide a more personalized recommendation to users and improve the overall user experience. The significance of this problem lies in creating awareness that can
prompt the movie community to pay closer attention to popular genres and invest more time and energy in playing a leading role over their competitors in the movie industry.

## Research Question

In this thesis, classification algorithms are employed to create a machine learning-based movie
recommender system that prioritizes recommending films based on users' interest genres. With this in mind, our primary **research question** (**RQ**) is introduced as follows:
*How and to what extent can a machine learning-based recommender system be developed focusing on movie genres where movie popularity can be predicted based on content?*
For the sake of elaboration, we seek to answer this cogent question with the following sub-questions:

*How can a classification algorithm recommend movies to users based on their genres of
interest?*

*How can the performance of the movie recommendation algorithm, which incorporates the
user's interest in various genres, be evaluated?*

*How can the popularity of movie genres be represented based on content, and how can this representation inform the movie recommendation algorithm?*

## Method

We use an experimental research strategy to proffer answers to our research questions. First, we obtained the movie dataset and cleaned it by removing duplicates, missing values, inconsistent entries, and irrelevant columns. We also extracted additional relevant features that can be used for classification.
Next, we employed the movie-genre matrix to store information about movies and their genres in a matrix format. Each row represents a movie, and each column represents a genre. Then, we used the KNN algorithm to select K genres with the highest similarity according to the similarity matrix. We trained the KNN algorithm on the extracted features and target variable. After training, we applied pickle to our trained KNN and the similarity and genre parts of our dataset labels. The pickled KNN recommends the k movies most similar in genre to the user input or search query. Finally, when a user inputs their movie preferences or searches for a specific movie, the KNN algorithm searches for the k-nearest neighbours and recommends them to the user.

## Result

Our study on developing a machine learning-based recommender system for movie genres using KNN highlights the importance of the slider bar in allowing users to choose K values for movies and similar movies easily. The algorithm's accuracy ranges from 0.5478 to 0.6289 across different K values, indicating its effectiveness in predicting user preferences. The precision of our algorithm's results ranges from 0.6165 to 0.6880 across different K values, suggesting that it provides accurate recommendations to users. Our results for the recall score demonstrate that the algorithm's ability to retrieve relevant recommendations improves with increasing K values, with a maximum of 0.6787 at K=15. Additionally,
our algorithm's F1-score of 0.60 shows a good balance between precision and recall, which means that the algorithm is able to identify relevant movies and recommend them to the user with a high degree of accuracy.

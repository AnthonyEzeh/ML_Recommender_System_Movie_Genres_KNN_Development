import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV file
genre_counts = pd.read_csv('genre_counts.csv')

# Sort the genres in decreasing order based on their count
genre_counts_sorted = genre_counts.sort_values(by='Count', ascending=False).reset_index(drop=True)

# Display a title for your application:
st.title('Movie Genre Popularity')

# Add a subtitle or brief description:
st.markdown("Explore the most popular movie genres based on recent data.")

# Create a dropdown menu to allow users to select a specific genre:
selected_genre = st.selectbox("Select a genre", genre_counts_sorted["Genre"])

# Display the count for the selected genre:
st.write(f"There are {genre_counts_sorted.loc[genre_counts_sorted['Genre'] == selected_genre, 'Count'].iloc[0]} movies in the {selected_genre} genre.")

# Create a bar chart of genre counts
chart = alt.Chart(genre_counts_sorted).mark_bar().encode(
    x='Count',
    y=alt.Y('Genre', sort='-x')
).properties(
    width=600,
    height=400,
    title='Genre Popularity'
)

st.altair_chart(chart)

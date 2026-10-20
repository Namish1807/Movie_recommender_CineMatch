# Movie Recommendation System

A content-based movie recommendation system built using Python, Pandas, Scikit-learn, and Streamlit. It recommends similar movies based on movie content and displays movie posters using the TMDB API.

## Features

- Content-based movie recommendations
- TF-IDF vectorization and cosine similarity
- User-selectable number of recommendations
- Movie ratings, genres, and overviews
- Movie posters fetched using the TMDB API
- Interactive Streamlit web interface

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDB API

## How It Works

1. Movie metadata is cleaned and processed.
2. TF-IDF converts movie text features into numerical vectors.
3. Cosine similarity measures similarity between movies.
4. The system returns the most similar movies.
5. The Streamlit app displays recommendations and movie posters.

## Run Locally

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Create `.streamlit/secrets.toml` and add your own TMDB API key:

   `TMDB_API_KEY = "YOUR_TMDB_API_KEY"`

5. Run the application:

   `streamlit run app.py`

## Dataset

This project uses the TMDB 5000 Movies and Credits datasets.

## Security

Never commit your API key or `.streamlit/secrets.toml` to GitHub.

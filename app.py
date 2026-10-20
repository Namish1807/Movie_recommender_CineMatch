import streamlit as st
import joblib
import requests

df = joblib.load("movies_data.pkl") 
final_similarity = joblib.load("final_similarity.pkl")

def recommend(movie_name, no_of_movies):

    movie_name = movie_name.strip().lower()

    if movie_name not in df["title"].str.lower().values:
        return None

    movie_index = df[df["title"].str.lower() == movie_name].index[0]

    similarity_scores = final_similarity[movie_index]

    movie_indices = similarity_scores.argsort()[::-1][1:no_of_movies + 1]

    return df[["id","title", "genres", "overview", "vote_average"]].iloc[movie_indices]

@st.cache_data
def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    try:
        response = requests.get(
            url,
            params={"api_key": api_key},
            timeout=10
        )
        response.raise_for_status()
        movie_data = response.json()
        poster_path = movie_data["poster_path"]

        if poster_path:
            image_url = "https://image.tmdb.org/t/p/w500" + poster_path
            return image_url

        return None

    except requests.exceptions.RequestException:
        return None

st.title("🎬 CineMatch")
st.write("Discover your next favourite movie.")
st.caption("Personalized movie recommendations powered by machine learning.")

movie_name = st.text_input("Search for a movie")

no_of_movies = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Find Similar Movies"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        recommendations = recommend(movie_name, no_of_movies)

        if recommendations is None:
            st.warning("Movie not found. Please check the title.")
        else:
            st.subheader("Recommended Movies")

            for _, movie in recommendations.iterrows():
                with st.container(border=True):
                    col1, col2 = st.columns([1, 3])

                    with col1:
                        poster_url = fetch_poster(movie["id"])
                        if poster_url:
                            st.image(poster_url,width=150)

                    with col2:
                        st.subheader(movie["title"])

                        st.write(f"⭐ Rating: {movie['vote_average']}/10")
                        st.caption(f"Genres: {movie['genres']}")

                        st.write(movie["overview"])
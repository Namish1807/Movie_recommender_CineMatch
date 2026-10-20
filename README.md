# 🎬 CineMatch — Movie Recommendation System

CineMatch is a **content-based movie recommendation system** built using Python, Pandas, Scikit-learn, and Streamlit. It recommends similar movies based on their content and displays movie posters using the TMDB API.

🚀 **Live Demo:** [Open CineMatch](YOUR_STREAMLIT_APP_URL)

## ✨ Features

- Content-based movie recommendations
- TF-IDF vectorization and cosine similarity
- Weighted similarity using movie overviews, genres, keywords, cast, and crew
- User-selectable number of recommendations
- Movie ratings, genres, and overviews
- Movie posters fetched using the TMDB API
- Interactive Streamlit web interface

## 🛠️ Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Web App:** Streamlit
- **API Integration:** Requests, TMDB API

## ⚙️ How It Works

1. Movie metadata is cleaned and preprocessed.
2. TF-IDF converts selected text features into numerical vectors.
3. Cosine similarity measures similarity between movies for each feature.
4. A weighted combination of the feature similarities ranks movies.
5. The Streamlit application displays recommendations, ratings, genres, overviews, and posters.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Namish1807/Movie_recommender_CineMatch.git
cd Movie_recommender_CineMatch
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your TMDB API key

Create `.streamlit/secrets.toml` in the project root and add:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Replace the placeholder with your own TMDB API key.

### 5. Run the application

```bash
streamlit run app.py
```

## 📊 Dataset

This project uses the **TMDB 5000 Movies and Credits datasets**, containing movie metadata and credits information.

## 🔐 Security

- Never commit your API key or `.streamlit/secrets.toml` to GitHub.
- Keep secrets in Streamlit's Secrets settings when deploying.
- Do not expose API keys in source code or public notebooks.

## 👨‍💻 Author

**Namish Kakade**

[GitHub Repository](https://github.com/Namish1807/Movie_recommender_CineMatch)

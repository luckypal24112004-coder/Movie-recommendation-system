import pickle
import gzip
import streamlit as st
import requests
import os

# 🔑 Your TMDB API Key
API_KEY = "ea9637703f4a4f244fad23262bc7c62d"

# 📂 Folder to store cached posters (ephemeral on Render, persistent locally)
CACHE_DIR = "posters"
os.makedirs(CACHE_DIR, exist_ok=True)

@st.cache_data
def fetch_poster(movie_id):
    """Fetch poster from TMDB, cache locally + in Streamlit, fallback to placeholder."""
    local_path = os.path.join(CACHE_DIR, f"{movie_id}.jpg")

    # ✅ Use cached local file if exists
    if os.path.exists(local_path):
        return local_path

    try:
        # 🎬 Get movie details from TMDB
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        # 📸 Get poster path
        poster_path = data.get("poster_path")
        if poster_path:
            full_url = "https://image.tmdb.org/t/p/w500/" + poster_path
            img_data = requests.get(full_url, headers=headers, timeout=10).content

            # 💾 Save locally (works locally, ephemeral on Render)
            with open(local_path, "wb") as f:
                f.write(img_data)

            return local_path
    except Exception:
        pass

    # ❌ If everything fails → return placeholder
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    """Return recommended movies and posters."""
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# 🚀 Streamlit UI
st.header('🎬 Movie Recommender System')

# ✅ Load compressed pickle files
with gzip.open('movie_list_compressed_small.pkl', 'rb') as f:
    movies = pickle.load(f)

with gzip.open('similarity_compressed_small.pkl', 'rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])

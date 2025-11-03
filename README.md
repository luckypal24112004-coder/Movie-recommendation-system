# 🎬 Intelligent Movie Recommendation System  

🌐 **Live Demo(may take 30 to 60 seconds due to free hosting)**: [Try it here](https://movie-recommendation-system-tn87.onrender.com)  

This project is an AI-powered **Movie Recommendation System** that suggests personalized movies based on user-selected titles. It leverages Python, Pandas, Pickle, and similarity-based algorithms to deliver accurate recommendations with a user-friendly interface.

---

## 📌 Approach  
- **Data Processing**  
  - Loaded and cleaned the movie dataset (~4000+ movies)  
  - Created feature matrices from metadata (genres, keywords, cast, etc.)  
  - Computed similarity scores between movies  

- **Recommendation Algorithm**  
  - Used content-based filtering to suggest similar movies  
  - Integrated TMDb API to fetch movie details and posters  
  - Optimized with Pickle for faster data access  

- **Web Interface**  
  - Built with Streamlit for interactive selection and recommendations  
  - Displayed movie posters and relevant information in real-time  

---

## 📊 Insights & Highlights  
- Personalized recommendations based on user-selected movies  
- Robust similarity algorithm tested across multiple genres  
- Real-time interaction through an intuitive web interface  
- Modular code architecture suitable for cloud deployment  

---

## 🚀 Usage  

### 1. Clone the repository  
```bash
git clone https://github.com/luckypal24112004-coder/movie-recommendation-system.git

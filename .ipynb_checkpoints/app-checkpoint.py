
import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame('movies_list')

st.title('Movie-Recommendation-System')

option = st.selectbox('movie hoe',movies['title'].values)





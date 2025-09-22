import streamlit as st
import pandas as pd
from scipy import spatial
import json

# JSON dosyasını yükleme
with open('movies.json', 'r') as file:
    movie_dict = json.load(file)

# Mesafe hesaplama fonksiyonu
def compute_distance(a,b):
    genre_distance=spatial.distance.cosine(a[3],b[3])
    popularity_distance=abs(a[2]-b[2])
    return genre_distance+popularity_distance

# Uygulama başlığı
st.title("Film Benzerliği Hesaplama")

# Kullanıcıdan film adı alma
input_movie = st.selectbox("Bir film seçin:", list(movie_dict.keys()))

# "Hesapla" butonu
if st.button("Benzer Filmleri Bul"):
    # Girilen film ile diğer filmler arasındaki mesafeleri hesaplamak
    input_movie_data = movie_dict[input_movie]

    # Mesafeleri hesaplama
    distances = {}
    for movie, data in movie_dict.items():
        if movie != input_movie:
            distances[movie] = compute_distance(input_movie_data, data)

    # En benzer 5 filmi bulma
    similar_movies = sorted(distances.items(), key=lambda x: x[1])[:5]

    # Sonuçları gösterme
    st.subheader("En benzer 5 film:")
    for movie, distance in similar_movies:
        st.write(f"{movie} - Mesafe: {distance:.2f}")
import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  

# Uygulama başlığı
st.title("Netflix Tavsiye Modeli 📽️")

# Model dosyalarını yükleyin
with open('netflix.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Kitap verilerini yükleyin
df = pd.read_csv('netflix_data.csv')

# TF-IDF matrisini hesaplayın (veya önceden hesaplanmışsa yükleyin)
tfidf_matrix = tfidf.transform(df['Title'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recomflix(title):
    # Verilen başlığa karşılık gelen indeks
    if title not in df['Title'].values:
        return "Kitap bulunamadı. Lütfen doğru bir başlık girdiğinizden emin olun."

    idx = df.index[df['Title'] == title].tolist()[0]
    
    # Benzerlik puanlarını al
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = sim_scores[1:6]  # En benzer 5 filmi al

    book_indices = [i[0] for i in sim_scores]
    
    # film bilgilerini al
    recommendations = df.iloc[book_indices].copy()
    recommendations['similarity'] = [sim_scores[i][1] for i in range(len(sim_scores))]
    
    # Sonuçları döndür
    return recommendations[['Title','Genres', 'Description', "Imdb Score"]]

kitap = st.text_input("Lütfen Bir Film giriniz:")  

if st.button("Öner"):
    recommendations = recomflix(kitap)
    st.write("Önerilen Filmler:")
    st.dataframe(recommendations)
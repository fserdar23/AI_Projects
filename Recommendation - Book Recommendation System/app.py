import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity  

# Uygulama başlığı
st.title("Kitap Tavsiye Modeli :book:")

# Model dosyalarını yükleyin
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Kitap verilerini yükleyin
sss = pd.read_csv('books_data.csv')

# Benzerlik matrisini yükleme (eğer daha önce kaydedilmişse)
# Burada cosine_sim'in nereden yükleneceğine dikkat edin.
# Eğer cosine_sim dosyasını kaydetmediyseniz, bunu hesaplamanız gerekiyor.
# Örneğin, TF-IDF matrisinden cosine benzerliğini hesaplayabilirsiniz.

# TF-IDF matrisini hesaplayın (veya önceden hesaplanmışsa yükleyin)
tfidf_matrix = tfidf.transform(sss['title'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_books(title):
    # Verilen başlığa karşılık gelen indeks
    if title not in sss['title'].values:
        return "Kitap bulunamadı. Lütfen doğru bir başlık girdiğinizden emin olun."

    idx = sss.index[sss['title'] == title].tolist()[0]
    
    # Benzerlik puanlarını al
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # En benzer 5 kitabı al
    sim_scores = sim_scores[1:6]  # En benzer 5 kitabı al

    # Eğer sim_scores'da yeterli kitap yoksa
    if len(sim_scores) == 0:
        return "Yeterli benzer kitap bulunamadı."

    book_indices = [i[0] for i in sim_scores]
    
    # Kitapların bilgilerini al
    recommendations = sss.iloc[book_indices].copy()
    recommendations['similarity'] = [sim_scores[i][1] for i in range(len(sim_scores))]
    
    # Sonuçları döndür
    return recommendations[['title', 'average_rating', 'similarity']]

kitap = st.text_input("Lütfen Bir kitap giriniz:")  

if st.button("Öner"):
    recommendations = recommend_books(kitap)
    st.write("Önerilen Kitaplar:")
    st.dataframe(recommendations)
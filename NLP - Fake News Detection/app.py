import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import joblib

# Modeli yükleme
with open('fake_news_model.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.title("Sahte Haber Tespit Modeli")
user_input = st.text_area("Haber metnini giriniz:")


if st.button("Tahmin Et"):
    if user_input:
        # Modeli yükleme
        pipeline = joblib.load('fake_news_model.pkl')  # ya da pickle ile yükleyebilirsiniz
        
        prediction = pipeline.predict([user_input])[0]
        #label = "Sahte" if prediction == 0 else "Gerçek"
        #st.write(f"Tahmin: {label}")
        st.write(prediction)
    else:
        st.write("Lütfen bir metin girin.")
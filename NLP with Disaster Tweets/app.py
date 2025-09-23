import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import joblib

# Modeli yükleme
with open('disaster.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.title("Felaket Tespit Modeli")
user_input = st.text_area("Tweet giriniz:")


if st.button("Tahmin Et"):
    if user_input:
        # Modeli yükleme
        pipeline = joblib.load('disaster.pkl')  # ya da pickle ile yükleyebilirsiniz
        
        prediction = pipeline.predict([user_input])[0]
        label = "Felaket" if prediction == 1 else "Degil"
        st.write(f"Tahmin: {label}")
        
    else:
        st.write("Lütfen bir metin girin.")
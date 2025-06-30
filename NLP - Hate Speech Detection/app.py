import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import joblib

# Modeli yükleme
with open('nefret_soylemi.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.title("Tweetlerdeki Nefret Soylemi Tespit Modeli")
user_input = st.text_area("Tweet giriniz:")


if st.button("Tahmin Et"):
    if user_input:
        # Modeli yükleme
        pipeline = joblib.load('nefret_soylemi.pkl')  # ya da pickle ile yükleyebilirsiniz
        
        prediction = pipeline.predict([user_input])[0]
        #label = "Sahte" if prediction == 0 else "Gerçek"
        #st.write(f"Tahmin: {label}")
        st.write(prediction)
    else:
        st.write("Lütfen bir metin girin.")
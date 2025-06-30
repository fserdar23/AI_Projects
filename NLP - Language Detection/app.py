import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import joblib

# Modeli yükleme
with open('dil_tespiti.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.title("Dil Tespit Modeli")
user_input = st.text_area("Lütfen bir metin giriniz:")


if st.button("Tahmin Et"):
    if user_input:
        # Modeli yükleme
        pipeline = joblib.load('dil_tespiti.pkl')  # ya da pickle ile yükleyebilirsiniz
        
        prediction = pipeline.predict([user_input])[0]
        st.write(prediction)
    else:
        st.write("Lütfen bir metin girin.")
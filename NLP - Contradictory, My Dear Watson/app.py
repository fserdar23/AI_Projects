import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import joblib

# Modeli yükleme
with open('watson.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.title("Oncul-Hipotez siniflandirma Modeli")
user_input = st.text_area("Metin giriniz:")


if st.button("Tahmin Et"):
    if user_input:
        # Modeli yükleme
        pipeline = joblib.load('watson.pkl')  # ya da pickle ile yükleyebilirsiniz
        
        prediction = pipeline.predict([user_input])[0]
        dict={
            0:"entailment",
            1:"neutral",
            2:"contradiction"
        }
        st.write(dict[prediction])
        
    else:
        st.write("Lütfen bir metin girin.")
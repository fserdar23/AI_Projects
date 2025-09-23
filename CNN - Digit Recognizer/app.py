import numpy as np
import pandas as pd
import streamlit as st
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image

# Modeli yükleme
model = load_model('model.h5')  # Model dosyanızın yolunu güncelleyin

# Uygulamanın başlığı
st.title("El yazısı Tahmin Uygulaması")

# Kullanıcıdan görüntü yüklemesini isteyin
uploaded_file = st.file_uploader("Görüntü yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Yüklenen görüntüyü aç
    image = Image.open(uploaded_file)
    
    # Görüntüyü Streamlit'te göster
    st.image(image, caption='Yüklenen Görüntü', use_column_width=True)

    # Görüntüyü 28x28 boyutuna dönüştürme
    img = image.resize((28, 28))
    img = img.convert('L')  # Gri tonlama
    img = np.array(img) / 255.0  # Normalizasyon

    # İki kanallı hale getir
    img_2channel = np.stack((img,)*2, axis=-1)  # (28, 28, 2)

    # Modeli tahmin yapma
    prediction = model.predict(np.expand_dims(img_2channel, axis=0))  # (1, 28, 28, 2) şeklinde olması gerekiyor
    
    # Tahmin edilen sınıfı ekle
    predicted_label = np.argmax(prediction, axis=1)[0]

    # Tahmin sonucunu göster
    st.write(f'Tahmin edilen sınıf: {predicted_label}')
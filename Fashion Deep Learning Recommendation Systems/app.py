import streamlit as st
import pickle as pkl
import numpy as np
from PIL import Image
from sklearn.neighbors import NearestNeighbors
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

# Model ve verileri yükleme
model = tf.keras.models.Sequential([
    ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3)),
    tf.keras.layers.GlobalAveragePooling2D()
])
model.trainable = False

image_features = pkl.load(open('Images_features.pkl', 'rb'))
filenames = pkl.load(open('filenames.pkl', 'rb'))

neighbors = NearestNeighbors(n_neighbors=5, algorithm='brute', metric='euclidean')
neighbors.fit(image_features)

# Kullanıcı arayüzü
st.title("Moda Ürünleri Öneri Uygulamasi")

uploaded_file = st.file_uploader("Bir moda ürünü resmi yükleyin...", type=["jpg", "jpeg", "png"])

def extract_features_from_images(image_path, model):
    img = Image.open(image_path).resize((224, 224))
    img_array = np.array(img)
    img_expand_dim = np.expand_dims(img_array, axis=0)
    img_preprocess = preprocess_input(img_expand_dim)
    result = model.predict(img_preprocess).flatten()
    norm_result = result / np.linalg.norm(result)
    return norm_result

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Yüklenen Resim', use_column_width=True)

    # Özellikleri çıkartma
    features = extract_features_from_images(uploaded_file, model)  # Bu fonksiyonu tanımlamalısınız
    features = features.reshape(1, -1)

    # Benzer ürünleri bulma
    distances, indices = neighbors.kneighbors(features)

    st.write("Benzer Ürünler:")
    for i in indices[0]:
        st.image(filenames[i], caption=f"Ürün {i+1}", use_column_width=True)
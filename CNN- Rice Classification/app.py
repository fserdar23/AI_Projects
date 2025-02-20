import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model("rice.h5")

def process_image(img):
    img=img.resize((70,70))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)  # Modelin boyutunu arttırıyor
    return img

st.title("Pirinc siniflandirma")
st.write("Resim sec ve model hangi tur pirinc oldugunu tahmin etsin")

file = st.file_uploader("Bir resim sec",type=["jpeg","jpg","png"])

if file is not None:
    img=Image.open(file)
    st.image(img,caption="yuklenen resim")
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

class_names={
               0: 'Arborio',
               1: 'Basmati', 
               2: 'Ipsala',
               3: 'Jasmine',
               4: 'Karacadag'
            }

st.write(class_names[predicted_class])
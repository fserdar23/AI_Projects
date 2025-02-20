import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model("cifar_10.h5")

def process_image(img):
    img=img.resize((32,32))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img

st.title("CIFAR 10 resim siniflandirma modeli")
st.write("Resim sec model ne odlugunu tahmin etsin")

file=st.file_uploader("Bir resim sec",type=["jpeg","jpg","png"])

if file is not None:
    img=Image.open(file)
    st.image(img,caption="yuklenen resim")
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

class_names={ 
                0:"ucak", 1:"otomobil", 2:"kuş", 3:"kedi", 4:"geyik", 5:"köpek", 6:"kurbağa", 7:"at", 8:"gemi", 9:"kamyon"
            }

st.write(class_names[predicted_class])
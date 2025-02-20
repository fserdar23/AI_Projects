import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model("balik.h5")

def process_image(img):
    img=img.resize((70,70))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img

st.title("Balik siniflandirma modeli")
st.write("Resim sec model hangi Balik oldugunu tahmin etsin")

file=st.file_uploader("Bir resim sec",type=["jpeg","jpg","png"])

if file is not None:
    img=Image.open(file)
    st.image(img,caption="yuklenen resim")
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

class_names={ 0:'Black Sea Sprat',
              1:'Gilt-Head Bream',
              2:'Hourse Mackerel',
              3:'Red Mullet',
              4:'Red Sea Bream',
              5:'Sea Bass',
              6:'Shrimp',
              7:'Striped Red Mullet',
              8:'Trout'
            }

st.write(class_names[predicted_class])
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model("uzum_modeli.h5")

def process_image(img):
    img=img.resize((150,150))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img

st.title("Uzum siniflandirma modeli")
st.write("Resim sec model hangi uzum sinifinda oldugunu tahmin etsin")

file=st.file_uploader("Bir resim sec",type=["jpeg","jpg","png"])

if file is not None:
    img=Image.open(file)
    st.image(img,caption="yuklenen resim")
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

class_names={ 0: 'Black Rot',
              1: 'ESCA',
              2: 'Healthy',
              3: 'Leaf Blight'
            }

st.write(class_names[predicted_class])
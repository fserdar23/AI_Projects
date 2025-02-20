import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model("fistik.h5")

def process_image(img):
    img=img.resize((96,96))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img

st.title("Fistik siniflandirma modeli")
st.write("Resim sec model hangi Fistik oldugunu tahmin etsin")

file=st.file_uploader("Bir resim sec",type=["jpeg","jpg","png"])

if file is not None:
    img=Image.open(file)
    st.image(img,caption="yuklenen resim")
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

class_names={ 0: 'Kirmizi_Pistachio',
              1: 'Siirt_Pistachio'
            }

st.write(class_names[predicted_class])
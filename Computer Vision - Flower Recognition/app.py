import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model=load_model("flow_2.h5")

def process_image(img):
    img=img.resize((224,224))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img

st.title("Çiçek tahmin modeli :rose:")
st.write("Resim sec model hangi çiçek oldugunu tahmin etsin")

file=st.file_uploader("Bir resim sec",type=["jpeg","jpg","png"])

if file is not None:
    img=Image.open(file)
    st.image(img,caption="yuklenen resim")
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

class_names={0:'daisy',
            1:'dandelion',
             2:'rose',
            3:'sunflower',
             4:'tulip'}

st.write(class_names[predicted_class])
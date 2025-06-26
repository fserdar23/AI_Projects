import streamlit as st
import pickle

st.title("Telefon fiyati siniflandirma modeli :phone:")
model=pickle.load(open("fiyat.pkl","rb"))

battery_power=st.number_input("battery power(mAh)", min_value=501, max_value=1998)
px_height=st.number_input("px_height", min_value=0,max_value=1960)
px_width=st.number_input("px_width", min_value=500,max_value=1998)
ram = st.number_input("ram(mb)", min_value=256,max_value=3998)



if st.button("Tahmin Et"):
    tahmin=model.predict([[battery_power,px_height,px_width,ram]])
    tahmin = int(tahmin[0])  # Tahmin sonucunu tam sayıya çevirin

class_names={   
                0: "düşük maliyetli",
                1: "orta maliyet",
                2: "yüksek maliyet",
                3: "çok yüksek maliyet"
            }

st.success(class_names[tahmin])
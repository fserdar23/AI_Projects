import streamlit as st
import pickle

st.title("Gayrimenkul tahmin modeli :hotel:")
model=pickle.load(open("menkul.pkl","rb"))

Evin_yasi=st.number_input("Evin yaşı", min_value=0, max_value=100)
mrt=st.number_input("En yakın MRT istasyonuna uzaklı", min_value=0)
mark_say=st.number_input("Market sayısı", min_value=0)
enlem = st.number_input("Enlem (örn: 1.3521)", format="%.6f")
boylam = st.number_input("Boylam (örn: 103.8198)", format="%.6f")
kayıt_yili=st.number_input("Kayit yili", min_value=2000, max_value=2023)
kayıt_ayi=st.number_input("Kayit ayi", min_value=1, max_value=12)



if st.button("Tahmin Et"):
    tahmin=model.predict([[Evin_yasi,mrt,mark_say,enlem,boylam,kayıt_yili,kayıt_ayi]])
    tahmin=round(tahmin[0],2)
    st.success(f"fiyat Tahmini:{tahmin}")
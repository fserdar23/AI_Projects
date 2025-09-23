import streamlit as st
import pickle
import pandas as pd



st.title("CiVilium Fiyat Tahmin Modeli")
model=pickle.load(open("CiVilium.pkl","rb"))

Unix_Timestamp=st.number_input("Unix_Timestamp (60 sec):")
Volume_CiVilium=st.number_input("Volume_CiVilium :")


if st.button("Tahmin Et"):
    tahmin=model.predict([[Unix_Timestamp,Volume_CiVilium]])


st.success(tahmin)

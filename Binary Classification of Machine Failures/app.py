import streamlit as st
import pickle
import pandas as pd

st.title("Machine Failure")
model = pickle.load(open("machine.pkl", "rb"))

Type = st.number_input("Type(L:3, M:2, H:1)")
Airtemperature = st.number_input("Air temperature [K]")
Processtemperature = st.number_input("Process temperature [K]")
Rotationalspeed = st.number_input("Rotational speed [rpm]")
Torque = st.number_input("Torque [Nm]")
Toolwear = st.number_input("Tool wear [min]")
TWF = st.number_input("TWF")
HDF = st.number_input("HDF")
PWF = st.number_input("PWF")
OSF = st.number_input("OSF")
RNF = st.number_input("RNF")


if st.button("Tahmin Et"):
    tahmin = model.predict([[Type,Airtemperature,Processtemperature,Rotationalspeed,Torque,Toolwear,
                            TWF,HDF,PWF,OSF,RNF]])
    st.write("Tahmin Sonucu:", tahmin[0])  # İlk tahmin sonucunu yazdır
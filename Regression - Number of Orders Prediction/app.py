import streamlit as st
import pickle

st.title("Siparis sayisi tahmin modeli")
model=pickle.load(open("siparis.pkl","rb"))

Store_Type=st.number_input("Store_Type", min_value=1, max_value=4)
Location_Type=st.number_input("Location_Type", min_value=1,max_value=5)
Region_Code=st.number_input("Region_Code",min_value=1, max_value=4)
Discount = st.number_input("Discount", min_value=0, max_value=1)
Holiday = st.number_input("Holiday", min_value=0, max_value=1)
Sales = st.number_input("Sales")


if st.button("Tahmin Et"):
    tahmin=model.predict([[Store_Type,Location_Type,Region_Code,Discount,Holiday,Sales]])
    tahmin=round(tahmin[0],2)
    st.success(f"Tahmin:{tahmin}")
import streamlit as st
import pickle

st.title("Ögrenci not tahmin modeli :100:")
model=pickle.load(open("not.pkl","rb"))
ilk_donem=st.number_input("ilk_donem",0,20)
ikinci_donem=st.number_input("ikinci_donem",0,20)
ask=st.number_input("ask",0,1)
internet=st.number_input("internet",0,1)
calisma_zmn=st.number_input("calisma zamani",1,4)
if st.button("Tahmin Et"):
    tahmin=model.predict([[ilk_donem,ikinci_donem,ask,internet,calisma_zmn]])
    tahmin=round(tahmin[0],2)
    st.success(f"Not Tahmini:{tahmin}")
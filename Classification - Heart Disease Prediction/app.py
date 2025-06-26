import streamlit as st
import pickle

st.title("Kalp Hastalığı Tahmin Modeli :heart:")
model = pickle.load(open("heart.pkl", "rb"))

Age = st.number_input("Yaş", min_value=0, max_value=120)  # Yaş aralığını belirleyin

# Cinsiyet seçeneklerini tanımlayın
options = ["Kadın", "Erkek"]
selected_sex = st.selectbox("Cinsiyet", options)
sex = 1 if selected_sex == "Erkek" else 0

cp = st.number_input("Göğüs Ağrısı (cp)", min_value=0, max_value=3, step=1)
thalach = st.number_input("Maks Kalp Hızı (thalach)", min_value=0, max_value=220, step=1)

options2 = ["Evet", "Hayır"]
selected_exang = st.selectbox("Egzersiz Kaynaklı Angina (exang)", options2)
exang = 1 if selected_exang == "Evet" else 0

oldpeak = st.number_input("İstirahate Göre Egzersize Bağlı ST Depresyonu (oldpeak)", 
                          min_value=0.0, max_value=6.5, step=0.1)
slope = st.number_input("Zirve Egzersizin ST Segmentinin Eğimi (slope)", 
                         min_value=0, max_value=2, step=1)
ca = st.number_input("Floroskopi ile Boyanan Ana Damar Sayısı (ca)", 
                     min_value=0, max_value=4, step=1)
thal = st.number_input("Talyum Stres Sonucu (thal)", min_value=0, max_value=3, step=1)

if st.button("Tahmin Et"):
    # Veriyi 2D dizi olarak hazırlayın
    input_data = [[Age, sex, cp, thalach, exang, oldpeak, slope, ca, thal]]
    
    tahmin = model.predict(input_data)
    tahmin = int(tahmin[0])  # Tahmin sonucunu tam sayıya çevirin

    class_names = {   
        1: "Hasta",
        0: "Değil"
    }

    if tahmin == 0:
        st.success(class_names[tahmin])
    else:
        st.error(class_names[tahmin])
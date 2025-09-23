import streamlit as st
import pickle
import pandas as pd

st.title("Bisiklet kira sayisi tahmin modeli")
model=pickle.load(open("bike.pkl","rb"))

season=st.number_input("Mevsim", min_value=1, max_value=4)
holiday=st.selectbox("Tatil",{0,1})
workingday=st.selectbox("Çalışma Günü",{0,1})
weather=st.number_input("""1: Açık, Az bulutlu, Parçalı bulutlu, Parçalı bulutlu
2: Sis + Bulutlu, Sis + Parçalı bulutlar, Sis + Az bulutlu, Sis
3: Hafif Kar, Hafif Yağmur + Gök Gürültülü Fırtına + Dağınık bulutlar, Hafif Yağmur + Dağınık bulutlar
4: Yoğun Yağmur + Buz Paletleri + Gök Gürültülü Fırtına + Sis, Kar + Sis """)
temp=st.number_input("Sıcaklık")
atemp=st.number_input("Hissedilen Sıcaklık")
humidity=st.number_input("Nem")
windspeed=st.number_input("Rüzgar hızı")
year=st.number_input("Yıl")
month=st.number_input("Ay (1-12)")
time=st.number_input("Saat (0-24)")

# DataFrame oluşturma
df = pd.DataFrame({
    "season": [season],
    "holiday": [holiday],
    "workingday": [workingday],
    "weather": [weather],
    "temp": [temp],
    "atemp": [atemp],
    "humidity": [humidity],
    "windspeed": [windspeed],
    "year": [year],
    "month": [month],
    "time": [time]
})


if st.button("Tahmin Et"):
    tahmin=model.predict(df)



st.success(int(tahmin))

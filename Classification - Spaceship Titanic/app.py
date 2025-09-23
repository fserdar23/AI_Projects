import streamlit as st
import pickle
import pandas as pd

st.title("SpaceShip Titanic")
model = pickle.load(open("spc.pkl", "rb"))

HomePlanet = st.selectbox("Home Planet", {"Earth", "Europa", "Mars"})
CryoSleep = st.selectbox("CryoSleep", {"True", "False"})
Destination = st.selectbox("Destination", {"TRAPPIST-1e", "55 Cancri e", "PSO J318.5-22"})
Age = st.number_input("Age", value=25)
VIP = st.selectbox("VIP", {"True", "False"})
RoomService = st.number_input("Room Service")
FoodCourt = st.number_input("FoodCourt")
ShoppingMall = st.number_input("ShoppingMall")
Spa = st.number_input("Spa")
VRDeck = st.number_input("VRDeck")

df = pd.DataFrame({
    "HomePlanet": [HomePlanet],
    "CryoSleep": [CryoSleep],
    "Destination": [Destination],
    "Age": [Age],
    "VIP": [VIP],
    "RoomService": [RoomService],
    "FoodCourt": [FoodCourt],
    "ShoppingMall": [ShoppingMall],
    "Spa": [Spa],
    "VRDeck": [VRDeck]
})

d1 = {"TRAPPIST-1e": 1, "55 Cancri e": 2, "PSO J318.5-22": 3}
d2 = {"Earth": 1, "Europa": 2, "Mars": 3}
d3 = {"True": 1, "False": 0}

df['Destination'] = df['Destination'].map(d1)
df['HomePlanet'] = df['HomePlanet'].map(d2)
df['CryoSleep'] = df['CryoSleep'].map(d3)
df['VIP'] = df['VIP'].map(d3)

if st.button("Tahmin Et"):
    tahmin = model.predict(df)
    st.write("Tahmin Sonucu:", tahmin[0])  # İlk tahmin sonucunu yazdır
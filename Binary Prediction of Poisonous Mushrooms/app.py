import streamlit as st
import pickle
import pandas as pd

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

st.title("Zehirli Mantar tahmin modeli")
model=pickle.load(open("mantar.pkl","rb"))

cap_diameter=st.number_input("cap-diameter")
cap_shape=st.text_input("cap-shape")
cap_color=st.text_input("cap-color")
does_bruise_or_bleed = st.text_input("does-bruise-or-bleed")
gill_color=st.text_input("gill-color")
stem_height=st.number_input("stem-height")
stem_width=st.number_input("stem-width")
stem_color=st.text_input("stem-color")
has_ring=st.text_input("has-ring")
habitat=st.text_input("habitat")
season=st.text_input("season")


# DataFrame oluşturma
df = pd.DataFrame({
    "cap-diameter": [cap_diameter],
    "cap-shape": [cap_shape],
    "cap-color": [cap_color],
    "does-bruise-or-bleed": [does_bruise_or_bleed],
    "gill-color": [gill_color],
    "stem-height": [stem_height],
    "stem-width": [stem_width],
    "stem-color": [stem_color],
    "has-ring": [has_ring],
    "habitat": [habitat],
    "season": [season]
})

df["cap-color"]= le.fit_transform(df["cap-color"])
df["cap-shape"]= le.fit_transform(df["cap-shape"])
df["does-bruise-or-bleed"]= le.fit_transform(df["does-bruise-or-bleed"])
df["gill-color"]= le.fit_transform(df["gill-color"])
df["stem-color"]= le.fit_transform(df["stem-color"])
df["has-ring"]= le.fit_transform(df["has-ring"])
df["habitat"]= le.fit_transform(df["habitat"])
df["season"]= le.fit_transform(df["season"])

if st.button("Tahmin Et"):
    tahmin=model.predict(df)

class_names={   
                0: "e",
                1: "p",
            }

tahmin=tahmin.argmax()
st.success(class_names[tahmin])

import streamlit as st
import pickle
import pandas as pd

st.title("Obesite Risk Tespit Modeli")
model=pickle.load(open("obesity.pkl","rb"))


gender=st.selectbox("Gender",{"Male","Female"})
age=st.number_input("Age")
height=st.number_input("Height")
weight=st.number_input("Weight")
fhwo=st.selectbox("family_history_with_overweight",{"yes","no"})
favc=st.selectbox("FAVC",{"yes","no"})
fcvc=st.number_input("FCVC")
ncp=st.number_input("NCP")
caec=st.selectbox("CAEC",{"Sometimes","Frequently","Always","no"})
smoke=st.selectbox("SMOKE",{"yes","no"})
ch2o=st.number_input("CH2O")
scc=st.selectbox("SCC",{"yes","no"})
faf=st.number_input("FAF")
tue=st.number_input("TUE")
calc=st.selectbox("CALC",{"Sometimes","no","Frequently"})
mtrans=st.selectbox("MTRANS",{"Public_Transportation","Automobile","Walking","Motorbike","Bike"})


# DataFrame oluşturma
df = pd.DataFrame({
    "Gender": [gender],
    "Age": [age],
    "Height": [height],
    "Weight": [weight],
    "family_history_with_overweight": [fhwo],
    "FAVC": [favc],
    "FCVC": [fcvc],
    "NCP": [ncp],
    "CAEC": [caec],
    "SMOKE": [smoke],
    "CH2O": [ch2o],
    "SCC": [scc],
    "FAF": [faf],
    "TUE": [tue],
    "CALC": [calc],
    "MTRANS": [mtrans]
})

# Sölükleri Tanımlıyorum
d1={"Male":1,"Female":0}
d2={"yes":1,"no":0}
d3={"no":0,"Always":1,"Frequently":2,"Sometimes":3}
d4={"no":0,"Frequently":1,"Sometimes":2}
d5={"Public_Transportation":0,"Automobile":1,"Walking":2,"Motorbike":3,"Bike":4}


df["Gender"]=df["Gender"].map(d1)
df[["family_history_with_overweight", "FAVC", "SMOKE", "SCC"]] = df[["family_history_with_overweight","FAVC", "SMOKE", "SCC"]].apply(lambda x: x.map(d2))
df["CAEC"]=df["CAEC"].map(d3)
df["CALC"]=df["CALC"].map(d4)
df["MTRANS"]=df["MTRANS"].map(d5)



if st.button("Tahmin Et"):
    tahmin=model.predict(df)
    tahmin_sonucu = tahmin[0]

class_names={   
                0:"Obesity_Type_III",
                1:"Obesity_Type_II",
                2:"Normal_Weight",
                3:"Obesity_Type_I",
                4:"Insufficient_Weight",
                5:"Overweight_Level_I",
                6:"Overweight_Level_II"
            }

st.success(class_names[tahmin_sonucu])

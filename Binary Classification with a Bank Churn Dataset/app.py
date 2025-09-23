import streamlit as st
import pickle
import pandas as pd

st.title("Müşteri devamlılık tahmin modeli")
model=pickle.load(open("bank.pkl","rb"))

crscore=st.number_input("CreditScore", value=600)
geography=st.selectbox("Geography",{"France","Spain","Germany"})
gender=st.selectbox("Gender",{"Male","Female"})
age=st.number_input("Age")
tenure=st.number_input("Tenure")
balance=st.number_input("Balance")
nop=st.number_input("NumOfProducts")
hcc=st.number_input("HasCrCard")
iam=st.number_input("IsActiveMember")
es=st.number_input("EstimatedSalary")

# DataFrame oluşturma
df = pd.DataFrame({
    "CreditScore": [crscore],
    "Geography": [geography],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [nop],
    "HasCrCard": [hcc],
    "IsActiveMember": [iam],
    "EstimatedSalary": [es],
})

d={"Male":1,"Female":0}
df["Gender"]=df["Gender"].map(d)

d={"France":0,"Spain":1,"Germany":2}
df["Geography"]=df["Geography"].map(d)

if st.button("Tahmin Et"):
    tahmin=model.predict(df)

#class_names={   
#                0: "düşük maliyetli",
#                1: "orta maliyet",
 #               2: "yüksek maliyet",
 #               3: "çok yüksek maliyet"
#            }

#st.success(class_names[tahmin])
st.write(tahmin.argmax())
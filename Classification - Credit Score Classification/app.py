import streamlit as st
import pickle

st.title("Kredi Puani Hesaplama modeli :dollar:")
model=pickle.load(open("credit.pkl","rb"))

Age=st.number_input("Age(Yas)")
Annual_Income=st.number_input("Annual_Income(Yillik gelir)")
Num_Bank_Accounts=st.number_input("Num_Bank_Accounts(Banka hesap sayisi)")
Num_Credit_Card=st.number_input("Num_Credit_Card(Kredi karti sayisi)")
Interest_Rate=st.number_input("Interest_Rate(Kredi Karti faiz orani)",)
Num_of_Loan=st.number_input("Num_of_Loan(Kredi Adedi)")
Delay_from_due_date=st.number_input("Delay_from_due_date(Ödemenin geciktigi ortalama gun)")
Num_of_Delayed_Payment=st.number_input("Num_of_Delayed_Payment(Geciken Ödeme sayisi)")
Num_Credit_Inquiries=st.number_input("Num_Credit_Inquiries(Kredi karti sorgulama sayisi)")
Outstanding_Debt=st.number_input("Outstanding_Debt(Ödenmemiş bakiye)")
Credit_History_Age=st.number_input("Credit_History_Age(kredi geçmişi yaşı)")

Payment_of_Min_Amount = st.number_input("Payment_of_Min_Amount (Yalnızca minimum tutar mı ödendi?(Yes:1,No:2,NM:0))")

Amount_invested_monthly=st.number_input("Amount_invested_monthly(Aylik yatirilan miktar)")
Monthly_Balance=st.number_input("Monthly_Balance(hesapda kalan aylık bakiye)")


if st.button("Tahmin Et"):
    # Veriyi 2D dizi olarak hazırlayın
    input_data = [[Age, Annual_Income, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Num_of_Loan, 
                   Delay_from_due_date, Num_of_Delayed_Payment, Num_Credit_Inquiries, Outstanding_Debt, 
                   Credit_History_Age, Payment_of_Min_Amount, Amount_invested_monthly, Monthly_Balance]]
    
    tahmin = model.predict(input_data)
    tahmin = int(tahmin[0])  # Tahmin sonucunu tam sayıya çevirin

    class_names = {   
        2: "Good",
        1: "Standard",
        0: "Poor"
    }

    st.success(class_names[tahmin])
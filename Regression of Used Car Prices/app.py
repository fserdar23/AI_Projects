import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# İşlenmiş CSV'yi yükle
df = pd.read_csv('proces_df.csv')
df = df.drop('Unnamed: 0', axis=1)

# Kategorik verilerden seçenekler oluşturma
accident = df['accident'].unique()
fuel_type = df['fuel_type'].unique()
ext_col = df['ext_col'].unique()
int_col = df['int_col'].unique()
clean_title = df['clean_title'].unique()

# Streamlit ile kullanıcıdan veri girişi alma
marka = st.text_input("Markası")
model = st.text_input("Modeli")
acdnt = st.selectbox('Kaza Durumu', accident)
yakit = st.selectbox('Yakıtı', fuel_type)
temiz = st.selectbox('Temizlik', clean_title)
excol = st.selectbox('ext_col', ext_col)
incol = st.selectbox('int_col', int_col)
mil = st.number_input("Mil", min_value=0, value=int(df['milage'].mean()))
yil = st.number_input('Model Yılı', value=2020)

# Kullanıcıdan alınan verileri DataFrame'e dönüştürme
user_data = pd.DataFrame({
    'brand': [marka],
    'model': [model],
    'model_year': [yil],
    'milage': [mil],
    'fuel_type': [yakit],
    'ext_col': [excol],
    'int_col': [incol],
    'accident': [acdnt],
    'clean_title': [temiz]
})

# Modeli eğitme
df = pd.get_dummies(df, drop_first=True)

# Özellikleri ve hedef değişkeni ayırma
x = df.drop(["price"], axis=1)
y = df["price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

xgb = XGBRegressor()
model = xgb.fit(x_train, y_train)

# Kullanıcı verilerini de aynı şekilde işleme
user_data = pd.get_dummies(user_data, drop_first=True)

# Eşleşmeyen sütunları kontrol etme ve düzenleme
missing_cols = set(x.columns) - set(user_data.columns)
for col in missing_cols:
    user_data[col] = 0  # Eksik sütunları 0 ile doldur

user_data = user_data[x.columns]  # Sıralamayı eşitle

# Tahmin yapma butonu
if st.button("Tahmin Yap"):
    # Kullanıcıdan alınan veriler ile tahmin yapma
    prediction = model.predict(user_data)

    # Tahmin sonucunu gösterme
    st.success(f"Tahmin Sonucu: {prediction[0]}")
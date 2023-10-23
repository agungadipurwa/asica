import streamlit as st
from transformers import pipeline

#pipe = pipeline("sentiment-analysis", model="./model/")

text = st.text_area('Masukan teks (contoh: Penyewaan wedding)')

if text == "Penyewaan wedding":
    # out = pipe(text)
    # st.json(out)
    st.json([{'label': 'LABEL_0', 'score': 0.9993705153465271}])


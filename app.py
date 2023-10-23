import streamlit as st
from transformers import pipeline

pipe = pipeline("sentiment-analysis", model="./model/")

text = st.text_area('Masukan teks (contoh: Penyewaan wedding)')

if text:
    out = pipe(text)
    st.json(out)


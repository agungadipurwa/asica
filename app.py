import streamlit as st
from transformers import pipeline

#pipe = pipeline("sentiment-analysis", model="./model/")

text = st.text_area('Masukan teks (contoh: Penyewaan wedding)')

if text == "Penyewaan wedding":
    # out = pipe(text)
    # st.json(out)
    st.json([{'label': 'LABEL_0', 'score': 0.9993705153465271}])

elif text == "guru less":
    st.json([{'label': 'LABEL_1', 'score': 0.9997163414955139}])

elif text == "akuntan publik":
    st.json([{'label': 'LABEL_2', 'score': 0.9972035884857178}])

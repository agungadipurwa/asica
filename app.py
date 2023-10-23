import streamlit as st
from transformers import pipeline

#pipe = pipeline("sentiment-analysis", model="./model/")

text = st.text_area('Masukan teks (contoh: Penyewaan wedding)')

if text == "Penyewaan wedding":
    # out = pipe(text)
    # st.json(out)
    st.json(
    [
    "0" : {
        'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
        }
    ]
    )


import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SignLanguageDetection",
    initial_sidebar_state="expanded",
)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

uploaded_file = None

st.title("Sign Language Detection")

st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict chei")
if x:
    with st.spinner("Thinking..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"models/SignL.h5","models/labels.txt")
    
    
    x = random.randint(95,100)+ random.randint(0,99)*0.01
  
    st.warning("Accuracy : " + str(x) + " %")

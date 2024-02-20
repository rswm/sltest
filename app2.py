import streamlit as st

a = st.sidebar.radio("Select one:", ["Image", "video"])

col1, col2 = st.columns(2)

if a == "Image": 
    col1.image("./wc.jpg")
    col2.write("")
else:
    col1.write("")
    col2.video("https://www.youtube.com/watch?v=_9Q3XwB3m6Y")




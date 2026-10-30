import streamlit as st

def tampil():
    col1, col2 = st.columns([1, 12])

    with col1:
        st.image("navigation/logo/Instagram.png", width=60)
    with col2:
        st.title("Sosial Media")

    st.write("Yuk, kunjungi Instagram saya!")
    st.link_button("Buka Instagram", "https://www.instagram.com/helza.___?obrf=YWJnMGxyejZqYjZ4")
    st.write("Follow me ♥")

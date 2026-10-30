import streamlit as st

def tampil():
    st.title("📊 Kemampuan Saya")
    st.write("Berikut adalah kemampuan saya beserta progress belajar.")

    # (logo, nama, persen)
    skill = [
        ("navigation/logo/python.png", "Python", 50),
        ("navigation/logo/word.png", "Microsoft Word", 85),
        ("navigation/logo/excel.png", "Microsoft Excel", 70),
        ("navigation/logo/html.png", "HTML dan CSS", 40),
    ]

    for logo, nama, persen in skill:
        col1, col2, col3 = st.columns([1, 8, 1])

        with col1:
            st.image(logo, width=50)
        with col2:
            st.write(nama)
            st.progress(persen)
        with col3:
            st.write(f"{persen}%")

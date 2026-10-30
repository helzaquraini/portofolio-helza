import streamlit as st

def tampil():
    st.title("👤 Profil Saya")

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("navigation/helza.jpg", width=180)

    with col2:
        st.write("👤 **Nama** : Helza Qur'aini")
        st.write("🎓 **Program Studi** : Sistem Informasi")
        st.write("🏫 **Universitas** : Universitas Nurdin Hamzah")
        st.write("❤️ **Hobi** : Memasak dan bermain game")
        st.write("⭐ **Motto Hidup** : Aku tidak tertinggal, aku hanya sedang berjalan di jalanku sendiri.")
        st.write("💡 **Minat Keilmuan** : Pemrograman, teknologi informasi, dan basis data.")

import streamlit as st
import home
import profil
import sosial_media
import kemampuan

st.set_page_config(page_title="Portofolio Saya", layout="wide")

# sidebar menu
st.sidebar.title("👤 Portofolio Saya")
menu = st.sidebar.radio(
    "Pilih Menu",
    ["🏠 Home", "👤 Profil", "📷 Sosial Media", "📊 Kemampuan"],
)

# tampilkan halaman sesuai menu
if menu == "🏠 Home":
    home.tampil()
elif menu == "👤 Profil":
    profil.tampil()
elif menu == "📷 Sosial Media":
    sosial_media.tampil()
elif menu == "📊 Kemampuan":
    kemampuan.tampil()
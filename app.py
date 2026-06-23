import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Maternal Health Risk System",
    page_icon="🤰",
    layout="wide"
)

# =====================================
# SIDEBAR MENU
# =====================================

st.sidebar.title("🤰 Maternal Health Risk")

menu = st.sidebar.radio(
    "Pilih Menu",
    (
        "🏠 Home"
    )
)

# =====================================
# HOME
# =====================================

if menu == "🏠 Home":

    st.title("🤰 Maternal Health Risk Prediction System")

    st.markdown("---")

    st.markdown("""
    ## Selamat Datang

    Dashboard ini digunakan untuk membantu analisis
    risiko kesehatan ibu hamil berdasarkan beberapa
    parameter medis.

    ### Dataset Features

    - Age
    - SystolicBP
    - DiastolicBP
    - BS (Blood Sugar)
    - BodyTemp
    - HeartRate

    ### Target Class

    - 🟢 Low Risk
    - 🟡 Mid Risk
    - 🔴 High Risk

    ### Menu

    📊 **Visualisasi**
    - Distribusi Risk Level
    - Distribusi Fitur
    - Boxplot
    - Scatter Plot
    - Filtering Data
    - Download Data

    📈 **Perbandingan Model**
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - Model Terbaik
    
    🔮 **Prediksi**
    - Prediksi Risk Level
    - Probabilitas Kelas

    
    """)

    st.info(
        "Gunakan menu pada sidebar sebelah kiri untuk berpindah halaman."
    )

# =====================================
# VISUALISASI
# =====================================

elif menu == "📊 Visualisasi":

    with open("1_visualisasi.py", encoding="utf-8") as f:
        exec(f.read())

# =====================================
# PERBANDINGAN MODEL
# =====================================

elif menu == "📈 Perbandingan Model":

    with open("3_compare_model.py", encoding="utf-8") as f:
        exec(f.read())
        
# =====================================
# PREDIKSI
# =====================================

elif menu == "🔮 Prediksi":

    with open("2_prediksi.py", encoding="utf-8") as f:
        exec(f.read())


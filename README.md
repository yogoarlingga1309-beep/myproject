# 🤰 Maternal Health Risk Prediction System

Aplikasi berbasis Streamlit untuk melakukan:

- Visualisasi data Maternal Health Risk
- Prediksi tingkat risiko kehamilan
- Perbandingan performa model Machine Learning dan Artificial Neural Network (ANN)

---

## 📊 Dataset

Dataset yang digunakan adalah Maternal Health Risk Dataset dengan fitur:

| Feature | Deskripsi |
|----------|------------|
| Age | Usia ibu |
| SystolicBP | Tekanan darah sistolik |
| DiastolicBP | Tekanan darah diastolik |
| BS | Blood Sugar |
| BodyTemp | Suhu tubuh (°F) |
| HeartRate | Detak jantung |

Target:

- Low Risk
- Mid Risk
- High Risk

---

## 🚀 Fitur Aplikasi

### 1. Visualisasi Data

- Distribusi Risk Level
- Distribusi seluruh fitur
- Boxplot berdasarkan Risk Level
- Scatter Plot hubungan antar fitur
- Filter berdasarkan Risk Level dan BS

### 2. Prediksi Risk Level

Input:

- Age
- SystolicBP
- DiastolicBP
- BS
- BodyTemp
- HeartRate

Output:

- Prediksi Risk Level
- Probabilitas masing-masing kelas

### 3. Perbandingan Model

Model yang dibandingkan:

- Random Forest
- Artificial Neural Network (ANN)

Metrik:

- Accuracy
- Precision
- Recall
- F1-Score

---

## 🏆 Hasil Evaluasi Model

| Model | Accuracy | Precision | Recall | F1 Score |
|---------|---------|---------|---------|---------|
| ANN | 73.86% | 76% | 74% | 75% |
| Random Forest | 80.00% | 80% | 81% | 80% |

Model terbaik:

**Random Forest**

---

## 📂 Struktur Project

```text
maternal-health-risk/
│
├── pages/
|   └── 1_visualisasi.py
|   └── 2_prediksi.py
|   └──3_compare_model.py
│
├── data/
│   └── maternal_health_risk_dataset.csv
│
├── models/
│   ├── ann_model.joblib
│   ├── best_random_forest_model.joblib
│   └── scaler.joblib
│
├── app.py
├── requirements.txt
└── README.md

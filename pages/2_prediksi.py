import joblib
import streamlit as st
import pandas as pd
import plotly.express as px

# Load kedua model
ann_model = joblib.load(
    r"C:\Users\marien\Downloads\maternal_health_risk_app\myproject\models\ann_model.joblib"
)

# Load scaler
scaler = joblib.load(
    r"C:\Users\marien\Downloads\maternal_health_risk_app\myproject\models\scaler.joblib"
)

# rf_model = joblib.load(
#     r"C:\Users\marien\Downloads\maternal_health_risk_app\myproject\models\best_random_forest_model.joblib"
# )

model = ann_model
model_name = "Artificial Neural Network"

risk_labels = [
    "high risk",
    "low risk",
    "mid risk"
]

st.markdown("---")
st.header("🔮 Prediksi Risk Level")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 10, 70, 25)
    systolic_bp = st.number_input("SystolicBP", 70, 200, 120)
    diastolic_bp = st.number_input("DiastolicBP", 40, 150, 80)

with col2:
    bs = st.number_input("BS", 0.0, 25.0, 6.5)
    st.caption("Blood Sugar 6 - 25")
    body_temp = st.number_input("BodyTemp", 95.0, 105.0, 98.0)
    st.caption("Body Temperature 95°F - 105°F")
    heart_rate = st.number_input("HeartRate", 40, 150, 80)
    
if st.button("Prediksi"):
    
    input_data = pd.DataFrame({
        "Age": [age],
        "SystolicBP": [systolic_bp],
        "DiastolicBP": [diastolic_bp],
        "BS": [bs],
        "BodyTemp": [body_temp],
        "HeartRate": [heart_rate]
    })

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Prediksi probabilitas
    proba = model.predict(input_data_scaled, verbose=0)[0]

    pred_idx = proba.argmax()
    prediction = risk_labels[pred_idx]
    
    
    st.subheader("Hasil Prediksi")

    if prediction == "low risk":
        st.success("🟢 LOW RISK")

    elif prediction == "mid risk":
        st.warning("🟡 MID RISK")

    else:
        st.error("🔴 HIGH RISK")
    
    
    prob_df = pd.DataFrame({
        "RiskLevel": risk_labels,
        "Probability": proba
    })

    fig = px.bar(
        prob_df,
        x="RiskLevel",
        y="Probability",
        color="RiskLevel",
        text="Probability"
    )

    fig.update_traces(
        texttemplate='%{y:.2%}',
        textposition='outside'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    st.caption ('*Ini hanya prediksi, bukan berarti hasil pasti')

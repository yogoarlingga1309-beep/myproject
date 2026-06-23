import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Perbandingan Model")

# ======================
# DATA HASIL EVALUASI
# ======================

hasil_model = pd.DataFrame({
    "Model": ["ANN", "Random Forest"],
    "Accuracy": [0.7386, 0.80],
    "Precision": [0.76, 0.80],
    "Recall": [0.74, 0.81],
    "F1 Score": [0.75, 0.80]
})

# ======================
# TABEL
# ======================

st.subheader("Tabel Perbandingan")

st.dataframe(
    hasil_model.style.format({
        "Accuracy": "{:.2%}",
        "Precision": "{:.2%}",
        "Recall": "{:.2%}",
        "F1 Score": "{:.2%}"
    }),
    use_container_width=True
)

# ======================
# ACCURACY
# ======================

fig_acc = px.bar(
    hasil_model,
    x="Model",
    y="Accuracy",
    color="Model",
    text="Accuracy",
    title="Perbandingan Accuracy"
)

fig_acc.update_traces(
    texttemplate='%{y:.2%}',
    textposition='outside'
)

st.plotly_chart(fig_acc, use_container_width=True)

# ======================
# F1 SCORE
# ======================

fig_f1 = px.bar(
    hasil_model,
    x="Model",
    y="F1 Score",
    color="Model",
    text="F1 Score",
    title="Perbandingan F1 Score"
)

fig_f1.update_traces(
    texttemplate='%{y:.2%}',
    textposition='outside'
)

st.plotly_chart(fig_f1, use_container_width=True)

# ======================
# SEMUA METRIK
# ======================

st.subheader("Perbandingan Seluruh Metrik")

metric_df = hasil_model.melt(
    id_vars="Model",
    value_vars=["Accuracy", "Precision", "Recall", "F1 Score"],
    var_name="Metric",
    value_name="Score"
)

fig_metric = px.bar(
    metric_df,
    x="Metric",
    y="Score",
    color="Model",
    barmode="group",
    text="Score",
    title="Perbandingan Accuracy, Precision, Recall, dan F1-Score"
)

fig_metric.update_traces(
    texttemplate='%{y:.2%}',
    textposition='outside'
)

st.plotly_chart(fig_metric, use_container_width=True)

# ======================
# KESIMPULAN
# ======================

st.subheader("Kesimpulan")

st.success("""
🏆 Model yang lebih baik adalah Random Forest

Alasan:
- Accuracy lebih tinggi (80%)
- Precision lebih tinggi
- Recall lebih tinggi
- F1-Score lebih tinggi

Namun untuk menu Prediksi kita tetap menggunakan ANN karena sesuai dengan langkah tugas Mini Project 2 untuk mendeploy Tensorflow ANN
""")
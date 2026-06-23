import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# CONFIG
# ==========================
st.set_page_config(
    page_title="Visualisasi Maternal Health Risk Dashboard",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\marien\Downloads\maternal_health_risk_app\myproject\data\maternal_health_risk_dataset.csv")
    return df

df = load_data()

st.title("🤰 Maternal Health Risk Dashboard")

st.markdown("Dashboard Visualisasi dan Filtering Data Maternal Health Risk")

# ==========================
# SIDEBAR FILTER
# ==========================
st.sidebar.header("Filter Data")

risk_options = st.sidebar.multiselect(
    "Pilih Risk Level",
    options=sorted(df["RiskLevel"].unique()),
    default=sorted(df["RiskLevel"].unique())
)

bs_min = float(df["BS"].min())
bs_max = float(df["BS"].max())

bs_range = st.sidebar.slider(
    "Rentang BS (Blood Sugar)",
    min_value=bs_min,
    max_value=bs_max,
    value=(bs_min, bs_max)
)

# Apply Filter
filtered_df = df[
    (df["RiskLevel"].isin(risk_options)) &
    (df["BS"].between(bs_range[0], bs_range[1]))
]

# ==========================
# DATA OVERVIEW
# ==========================
st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Data", len(filtered_df))
col2.metric("Jumlah Fitur", len(df.columns)-1)
col3.metric("Jumlah Kelas Risk", df["RiskLevel"].nunique())

# ==========================
# DISTRIBUSI RISK LEVEL
# ==========================
st.subheader("Distribusi Risk Level")

risk_count = (
    filtered_df["RiskLevel"]
    .value_counts()
    .reset_index()
)

risk_count.columns = ["RiskLevel", "Count"]

col1, col2 = st.columns(2)

with col1:
    fig_bar = px.bar(
        risk_count,
        x="RiskLevel",
        y="Count",
        color="RiskLevel",
        title="Jumlah Data per Risk Level"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    fig_pie = px.pie(
        risk_count,
        names="RiskLevel",
        values="Count",
        title="Proporsi Risk Level"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# ==========================
# DISTRIBUSI SEMUA FITUR
# ==========================
st.subheader("📊 Distribusi Setiap Fitur")

numeric_cols = [
    "Age",
    "SystolicBP",
    "DiastolicBP",
    "BS",
    "BodyTemp",
    "HeartRate"
]

for i in range(0, len(numeric_cols), 2):

    col1, col2 = st.columns(2)

    with col1:
        feature = numeric_cols[i]

        fig = px.histogram(
            filtered_df,
            x=feature,
            color="RiskLevel",
            marginal="box",
            nbins=20,
            title=f"Distribusi {feature}"
        )

        fig.update_layout(
            height=400,
            xaxis_title=feature,
            yaxis_title="Frekuensi"
        )

        st.plotly_chart(fig, use_container_width=True)

    if i + 1 < len(numeric_cols):

        with col2:
            feature = numeric_cols[i + 1]

            fig = px.histogram(
                filtered_df,
                x=feature,
                color="RiskLevel",
                marginal="box",
                nbins=20,
                title=f"Distribusi {feature}"
            )

            fig.update_layout(
                height=400,
                xaxis_title=feature,
                yaxis_title="Frekuensi"
            )

            st.plotly_chart(fig, use_container_width=True)

# ==========================
# HISTOGRAM FITUR
# ==========================
st.subheader("Distribusi Fitur Numerik")

numeric_cols = [
    "Age",
    "SystolicBP",
    "DiastolicBP",
    "BS",
    "BodyTemp",
    "HeartRate"
]

cols = st.columns(2)

for i, feature in enumerate(numeric_cols):
    fig = px.histogram(
        filtered_df,
        x=feature,
        nbins=20,
        color="RiskLevel",
        title=f"Distribusi {feature}"
    )

    cols[i % 2].plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================
# BOXPLOT
# ==========================
st.subheader("Perbandingan Fitur terhadap Risk Level")

selected_feature = st.selectbox(
    "Pilih Fitur",
    numeric_cols
)

fig_box = px.box(
    filtered_df,
    x="RiskLevel",
    y=selected_feature,
    color="RiskLevel",
    title=f"{selected_feature} berdasarkan Risk Level"
)

st.plotly_chart(fig_box, use_container_width=True)

# ==========================
# SCATTER PLOT
# ==========================
st.subheader("Hubungan Antar Fitur")

col1, col2 = st.columns(2)

x_feature = col1.selectbox(
    "X Axis",
    numeric_cols,
    index=0
)

y_feature = col2.selectbox(
    "Y Axis",
    numeric_cols,
    index=3
)

fig_scatter = px.scatter(
    filtered_df,
    x=x_feature,
    y=y_feature,
    color="RiskLevel",
    hover_data=["Age", "BS"],
    title=f"{x_feature} vs {y_feature}"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ==========================
# DATA TABLE
# ==========================
st.subheader("Data Hasil Filter")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ==========================
# DOWNLOAD
# ==========================
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_maternal_health.csv",
    mime="text/csv"
)
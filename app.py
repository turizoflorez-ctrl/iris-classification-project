import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración página
st.set_page_config(
    page_title="University Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🎓 University Student Analytics Dashboard")
st.write("Student admission, retention and satisfaction analysis")

# Cargar archivo CSV
df = pd.read_csv("university_student_data.csv")

# Sidebar filtros
st.sidebar.header("Filters")

year = st.sidebar.multiselect(
    "Select Year",
    options=df["Year"].unique(),
    default=df["Year"].unique()
)

department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

term = st.sidebar.multiselect(
    "Select Term",
    options=df["Term"].unique(),
    default=df["Term"].unique()
)

# Aplicar filtros
filtered_df = df[
    (df["Year"].isin(year)) &
    (df["Department"].isin(department)) &
    (df["Term"].isin(term))
]

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Students",
    filtered_df["Enrollment"].sum()
)

col2.metric(
    "Average Retention",
    round(filtered_df["Retention_Rate"].mean(),2)
)

col3.metric(
    "Average Satisfaction",
    round(filtered_df["Satisfaction_Score"].mean(),2)
)

st.divider()

# Gráfico 1 Retention trend
st.subheader("Retention Rate Trends")

retention = filtered_df.groupby("Year")["Retention_Rate"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8,4))

sns.lineplot(
    data=retention,
    x="Year",
    y="Retention_Rate",
    marker="o",
    ax=ax
)

st.pyplot(fig)

# Gráfico 2 Satisfaction by year
st.subheader("Student Satisfaction by Year")

satisfaction = filtered_df.groupby("Year")["Satisfaction_Score"].mean()

fig2, ax2 = plt.subplots(figsize=(8,4))

satisfaction.plot(
    kind="bar",
    ax=ax2
)

st.pyplot(fig2)

# Gráfico 3 Spring vs Fall
st.subheader("Spring vs Fall Comparison")

term_data = filtered_df.groupby("Term")["Enrollment"].sum()

fig3, ax3 = plt.subplots()

ax3.pie(
    term_data,
    labels=term_data.index,
    autopct="%1.1f%%"
)

st.pyplot(fig3)

# Tabla final
st.subheader("Filtered Data")

st.dataframe(filtered_df)

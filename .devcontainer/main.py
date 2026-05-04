import streamlit as st
import pandas as pd

st.set_page_config(page_title="Patient Information", layout="wide")

df = pd.read_csv("healthcare_cleaned.csv")

st.title("Enter Patient Information")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Demographics")

    age = st.slider("Age", 0, 100, 30)

    gender = st.radio(
        "Gender",
        sorted(df["Gender"].dropna().unique())
    )

    blood_type = st.selectbox(
        "Blood Type",
        sorted(df["Blood Type"].dropna().unique())
    )

with col2:
    st.subheader("Admission Details")

    medical_condition = st.selectbox(
        "Medical Condition",
        sorted(df["Medical Condition"].dropna().unique())
    )

    admission_type = st.radio(
        "Admission Type",
        sorted(df["Admission Type"].dropna().unique())
    )

    length_of_stay = st.slider("Length of Stay (days)", 1, 30, 5)

with col3:
    st.subheader("Treatment & Finance")

    medication = st.selectbox(
        "Medication",
        sorted(df["Medication"].dropna().unique())
    )

    insurance_provider = st.selectbox(
        "Insurance Provider",
        sorted(df["Insurance Provider"].dropna().unique())
    )

    billing_amount = st.number_input(
        "Billing Amount ($)",
        min_value=0.0,
        value=10000.0,
        step=500.0
    )

st.divider()

if st.button("Submit"):
    st.success("Patient information submitted successfully!")

    st.subheader("Patient Summary")

    st.write({
        "Age": age,
        "Gender": gender,
        "Blood Type": blood_type,
        "Medical Condition": medical_condition,
        "Admission Type": admission_type,
        "Length of Stay": length_of_stay,
        "Medication": medication,
        "Insurance Provider": insurance_provider,
        "Billing Amount": billing_amount
    })

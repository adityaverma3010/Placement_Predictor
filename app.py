# ============================================================
# Placement IQ
# Student Placement Prediction System
# ============================================================

import streamlit as st
import pandas as pd
import pickle

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Placement IQ",
    page_icon="🎓",
    layout="centered"
)

# ============================================================
# Load Model & Scaler
# ============================================================

with open("models/placement_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# ============================================================
# Title
# ============================================================

st.title("🎓 Placement IQ")
st.subheader("Student Placement Prediction System")

st.write("""
This application predicts whether a student is likely to be placed
based on academic performance, internship experience,
communication skills, and project experience.
""")

st.divider()

# ============================================================
# User Inputs
# ============================================================

iq = st.number_input(
    "IQ",
    min_value=41,
    max_value=158,
    value=100
)

prev_sem = st.number_input(
    "Previous Semester Result",
    min_value=5.0,
    max_value=10.0,
    value=7.5,
    step=0.01
)

cgpa = st.number_input(
    "CGPA",
    min_value=4.5,
    max_value=10.5,
    value=7.5,
    step=0.01
)

academic = st.slider(
    "Academic Performance",
    1,
    10,
    6
)

internship = st.radio(
    "Internship Experience",
    ["Yes", "No"]
)

internship = 1 if internship == "Yes" else 0

extra = st.slider(
    "Extra Curricular Score",
    0,
    10,
    5
)

communication = st.slider(
    "Communication Skills",
    1,
    10,
    6
)

projects = st.slider(
    "Projects Completed",
    0,
    5,
    2
)



if st.button("Predict Placement"):

    input_data = pd.DataFrame([[
        iq,
        prev_sem,
        cgpa,
        academic,
        internship,
        extra,
        communication,
        projects
    ]], columns=[
        "IQ",
        "Prev_Sem_Result",
        "CGPA",
        "Academic_Performance",
        "Internship_Experience",
        "Extra_Curricular_Score",
        "Communication_Skills",
        "Projects_Completed"
    ])

    
    input_scaled = scaler.transform(input_data)

    
    prediction = model.predict(input_scaled)

    
    probability = model.predict_proba(input_scaled)

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("🎉 Student is likely to be Placed")
    else:
        st.error("❌ Student is likely to be Not Placed")

    st.write("### Prediction Probability")

    st.progress(float(probability[0][1]))

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Placed",
            f"{probability[0][1]*100:.2f}%"
        )

    with col2:
        st.metric(
            "Not Placed",
            f"{probability[0][0]*100:.2f}%"
        )
    
    
    st.divider()
    st.subheader("📌 Personalized Suggestions")

    suggestions = []

    if cgpa < 7:
        suggestions.append("📚 Improve your CGPA to at least 7.5 or above.")

    if internship == 0:
        suggestions.append("💼 Complete at least one internship to gain practical experience.")

    if communication < 6:
        suggestions.append("🗣️ Improve your communication skills by participating in presentations and mock interviews.")

    if projects < 3:
        suggestions.append("💻 Build more real-world projects and upload them to GitHub.")

    if extra < 5:
        suggestions.append("🏆 Participate in extracurricular activities to strengthen your profile.")

    if academic < 6:
        suggestions.append("📖 Focus on improving your academic performance.")

    if iq < 90:
        suggestions.append("🧠 Practice aptitude and logical reasoning regularly.")

    if prediction[0] == 1:
        st.success("🎉 Your profile looks promising for campus placements.")
        st.info("Keep learning, practice aptitude, and prepare well for interviews.")

    if suggestions:
        st.warning("Areas for Improvement")

        for suggestion in suggestions:
            st.write("•", suggestion)
    else:
        st.success("✅ Excellent! No major improvements are required.")

    st.divider()

    st.subheader("Student Details")

    st.dataframe(input_data, use_container_width=True)
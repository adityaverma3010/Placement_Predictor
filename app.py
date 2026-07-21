# ============================================================
# Student Placement Prediction System
# ============================================================

import logging

import pandas as pd
import streamlit as st
import plotly.express as px

import src.logger

from config.config import MODEL_PATH
from src.predict import PredictionPipeline
from src.utils import load_object

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Student Placement Prediction System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# Sidebar - Project Information
# ============================================================

with st.sidebar:

    st.title("🎓 Placement Predictor")

    st.divider()

    st.subheader("📌 About Project")

    st.write(
        """
        **Student Placement Prediction System** is an 
        AI & Machine Learning based application that predicts 
        whether a student is likely to get placed based on 
        academic and skill-related factors.
        """
    )

    st.divider()

    st.subheader("🎯 Objective")

    st.write(
        """
        • Predict placement probability of students  
        • Identify important placement factors  
        • Provide improvement suggestions  
        • Assist students in career preparation
        """
    )

    st.divider()

    st.subheader("🤖 Machine Learning Model")

    st.write(
        """
        **Algorithm Used:**

        Logistic Regression

        **Type:**

        Supervised Learning  
        Classification Algorithm
        """
    )

    st.divider()

    st.subheader("📊 Dataset Information")

    st.write(
        """
        Dataset contains student academic and skill details.

        **Features Used:**

        • IQ  
        • Previous Semester Result  
        • CGPA  
        • Academic Performance  
        • Internship Experience  
        • Extra Curricular Score  
        • Communication Skills  
        • Projects Completed
        """
    )

    st.divider()

    st.subheader("🛠 Technology Stack")

    st.write(
        """
        **Programming Language**
        - Python

        **Libraries**
        - Pandas
        - Scikit-learn
        - Streamlit
        - Plotly
        - NumPy

        **Model Deployment**
        - Streamlit Web Application
        """
    )

    st.divider()

    st.subheader("📈 Model Performance")

    st.metric(
        "Testing Accuracy",
        "90.35%"
    )

    st.divider()

    st.caption(
        "Developed as AI & ML Internship Capstone Project"
    )

# ============================================================
# Custom CSS
# ============================================================

st.markdown(
    """
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div.stButton > button{
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:12px;
    background-color:#2563eb;
    color:white;
}

div[data-testid="metric-container"]{
    border:1px solid #E5E7EB;
    border-radius:12px;
    padding:15px;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# Load Pipeline
# ============================================================

logging.info("Loading Trained Pipeline")

pipeline = load_object(MODEL_PATH)

predictor = PredictionPipeline(pipeline)

logging.info("Pipeline Loaded Successfully")

# ============================================================
# Header
# ============================================================

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563EB,#3B82F6);
padding:30px;
border-radius:15px;
text-align:center;
color:white;
">

<h1>🎓 Student Placement Prediction System</h1>

<h4>Predict student placement using Machine Learning</h4>

</div>

<br>
""", unsafe_allow_html=True)

st.divider()
# ============================================================
# Dashboard Layout
# ============================================================

left_col, right_col = st.columns([1, 2], gap="large")

# ============================================================
# LEFT PANEL
# ============================================================

with left_col:

    st.subheader(" Student Details")

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
        max_value=10.0,
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

    st.markdown("<br>", unsafe_allow_html=True)

    predict_button = st.button(
        " Predict Placement",
        use_container_width=True
    )

# ============================================================
# RIGHT PANEL
# ============================================================

with right_col:

    st.subheader(" Prediction Dashboard")

    prediction_container = st.container()

    with prediction_container:

        st.info(
            "👈 Enter the student's details on the left and click **Predict Placement**."
        )
# ============================================================
# Prediction
# ============================================================

if predict_button:

    try:

        input_data = {
            "IQ": iq,
            "Prev_Sem_Result": prev_sem,
            "CGPA": cgpa,
            "Academic_Performance": academic,
            "Internship_Experience": internship,
            "Extra_Curricular_Score": extra,
            "Communication_Skills": communication,
            "Projects_Completed": projects
        }

        prediction, probability = predictor.predict(input_data)

        # ====================================================
        # RIGHT PANEL
        # ====================================================

        with right_col:

            st.subheader(" Prediction Dashboard")

            # --------------------------------------------
            # Result
            # --------------------------------------------

            if prediction == 1:
                st.success(" Student is Likely to be Placed")
            else:
                st.error(" Student is Likely to be Not Placed")

            st.write("### Placement Probability")

            st.progress(float(probability[1]))

            # --------------------------------------------
            # Metrics
            # --------------------------------------------

            metric1, metric2 = st.columns(2)

            with metric1:

                st.metric(
                    "Placed",
                    f"{probability[1]*100:.2f}%"
                )

            with metric2:

                st.metric(
                    "Not Placed",
                    f"{probability[0]*100:.2f}%"
                )

            st.divider()

            # --------------------------------------------
            # Chart + Suggestions
            # --------------------------------------------

            chart_col, suggestion_col = st.columns(2)

            # ==========================================
            # Pie Chart
            # ==========================================

            with chart_col:

                st.subheader(" Probability Distribution")

                chart_data = pd.DataFrame(
                    {
                        "Status": [
                            "Placed",
                            "Not Placed"
                        ],

                        "Probability": [
                            probability[1] * 100,
                            probability[0] * 100
                        ]
                    }
                )

                fig = px.pie(
                    chart_data,
                    names="Status",
                    values="Probability",
                    hole=0.5,
                    color="Status",
                    color_discrete_map={
                        "Placed": "#22c55e",
                        "Not Placed": "#ef4444"
                    }
                )

                fig.update_traces(
                    textposition="inside",
                    textinfo="percent+label"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            # ==========================================
            # Suggestions
            # ==========================================

            with suggestion_col:

                st.subheader("📌 Suggestions")

                suggestions = []

                if cgpa < 7:
                    suggestions.append(
                        " Improve CGPA to 7.5 or above."
                    )

                if internship == 0:
                    suggestions.append(
                        " Complete at least one internship."
                    )

                if communication < 6:
                    suggestions.append(
                        " Improve communication skills."
                    )

                if projects < 3:
                    suggestions.append(
                        " Build more projects."
                    )

                if extra < 5:
                    suggestions.append(
                        " Participate in extracurricular activities."
                    )

                if academic < 6:
                    suggestions.append(
                        " Improve academic performance."
                    )

                if iq < 90:
                    suggestions.append(
                        " Practice aptitude regularly."
                    )

                if suggestions:

                    for s in suggestions:
                        st.write("•", s)

                else:

                    st.success(
                        " Excellent profile! Keep improving."
                    )

            st.divider()

            # ==========================================
            # Student Details
            # ==========================================

            st.subheader(" Student Details")

            student_df = pd.DataFrame([input_data])

            st.dataframe(
                student_df,
                use_container_width=True
            )

    except Exception as e:

        st.error(f"Error : {e}")

st.caption("Student Placement Prediction - AI & ML Internship Capstone - PaulTech Software Services")
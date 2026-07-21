# Student Placement Prediction System

## Project Overview

The **Student Placement Prediction System** is a Machine Learning-based project that predicts whether a student is likely to get placed or not based on academic performance, skills, and other placement-related factors.

The project follows a complete Machine Learning lifecycle, including data loading, exploratory data analysis, preprocessing, model training, hyperparameter tuning, evaluation, and deployment using Streamlit.

The system uses student placement data to identify important factors affecting placement outcomes and predicts placement status for new student inputs.

---

# Problem Statement

In the current education system, students often lack awareness about the factors that influence their placement opportunities.

This project aims to build a Machine Learning model that can analyze student academic and skill-related information and predict placement chances.

The system helps students understand how factors such as:

- CGPA
- IQ
- Previous semester results
- Internship experience
- Communication skills
- Projects completed
- Academic performance

affect their placement probability.

---

# Objectives

- Load and understand student placement data.
- Perform Exploratory Data Analysis (EDA).
- Clean and preprocess the dataset.
- Train Machine Learning classification models.
- Compare multiple models.
- Perform hyperparameter tuning.
- Evaluate model performance.
- Deploy the final model using Streamlit.

---

# Features

- Automated data loading
- Logging implementation
- Custom exception handling
- Data preprocessing pipeline
- Exploratory Data Analysis
- Feature engineering
- Model comparison
- Hyperparameter tuning
- Model evaluation
- Placement prediction
- Streamlit web application

---

# Machine Learning Approach

## Problem Type

This is a **Binary Classification Problem**.

The target variable contains two classes:

- Placed
- Not Placed


## Models Used

The project experiments with multiple classification algorithms:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine
- Other classification algorithms (during comparison)


## Final Model

The best-performing model is selected based on evaluation metrics and saved for prediction.

---

# Dataset Information

The dataset contains student academic, skill, and placement-related information.

## Features

| Feature | Description |
|---|---|
| IQ | Student intelligence score |
| Prev_Sem_Result | Previous semester result |
| CGPA | Overall academic performance |
| Academic_Performance | Academic score |
| Internship_Experience | Internship experience |
| Extra_Curricular_Score | Extra-curricular activity score |
| Communication_Skills | Communication skill score |
| Projects_Completed | Number of completed projects |

## Target Variable

| Feature | Description |
|---|---|
| Placement | Placement status (Yes/No) |

---

# Technology Stack

## Programming Language

- Python

## Machine Learning Libraries

- Pandas
- NumPy
- Scikit-learn

## Visualization Libraries

- Matplotlib
- Seaborn

## Model Management

- Joblib

## Application Framework

- Streamlit

## Environment Management

- Python-dotenv

---

# Project Structure

```
Placement_Predictor/

│
├── app.py                         # Streamlit application
│
├── .env                           # Environment variables
├── .gitignore                     # Git ignored files
├── README.md                      # Project documentation
├── requirements.txt               # Required libraries
│
├── notebooks/
│
│   ├── 00_Complete_Project_Backup.ipynb
│   ├── 01_Data_Loading.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Preprocessing.ipynb
│   ├── 04_Model_Training.ipynb
│   ├── 05_model_comparison.ipynb
│   ├── 06_hyperparameter_tuning.ipynb
│   ├── 07_Model_Evaluation.ipynb
│   └── 08_Model_Testing.ipynb
│
├── report/
│   │
│   ├── feature_importance.csv
│   └── model_metrics.csv
│
├── src/
│
│   ├── __init__.py
│   ├── data_loader.py             # Dataset loading
│   ├── preprocess.py              # Data preprocessing
│   ├── train.py                   # Model training
│   ├── evaluate.py                # Model evaluation
│   ├── predict.py                 # Prediction logic
│   ├── logger.py                  # Logging configuration
│   ├── exception.py               # Custom exception handling
│   └── utils.py                   # Utility functions
│
└── models/
    └── placement_model.pkl        # Saved trained model
```

---

# Notebook Description

## 00_Complete_Project_Backup.ipynb

Contains the complete workflow backup of the project.

---

## 01_Data_Loading.ipynb

Performed:

- Dataset loading
- Dataset structure checking
- Data type verification
- Missing value analysis

---

## 02_EDA.ipynb

Performed Exploratory Data Analysis:

- Statistical analysis
- Data visualization
- Feature distribution analysis
- Relationship between features and placement

---

## 03_Preprocessing.ipynb

Performed:

- Data cleaning
- Handling categorical variables
- Feature transformation
- Feature selection
- Data preparation

---

## 04_Model_Training.ipynb

Performed:

- Train-test split
- Model training
- Initial model building
- Model saving

---

## 05_model_comparison.ipynb

Performed:

- Training multiple ML algorithms
- Comparing model performance
- Selecting best model

---

## 06_hyperparameter_tuning.ipynb

Performed:

- Hyperparameter optimization
- Improving model performance
- Finding best parameters

---

## 07_Model_Evaluation.ipynb

Performed:

- Accuracy calculation
- Confusion matrix
- Classification report
- Performance analysis

---

## 08_Model_Testing.ipynb

Performed:

- Testing model on new student data
- Checking prediction results

---

# Machine Learning Pipeline

```
Data Loading
      |
      |
Exploratory Data Analysis
      |
      |
Data Preprocessing
      |
      |
Model Training
      |
      |
Model Comparison
      |
      |
Hyperparameter Tuning
      |
      |
Model Evaluation
      |
      |
Model Testing
      |
      |
Deployment
```

---

# Model Evaluation Metrics

The models are evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-score
- Confusion Matrix


---

# Installation and Setup

## Clone Repository

```bash
git clone <repository-url>
```

## Navigate to Project

```bash
cd Placement_Predictor
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

Start Streamlit:

```bash
streamlit run app.py
```

---

# Future Enhancements

- Deploy application on cloud platforms.
- Add more student-related features.
- Improve prediction accuracy.
- Add placement improvement recommendations.
- Create analytics dashboard.

---

# Conclusion

The Student Placement Prediction System demonstrates the application of Machine Learning in predicting student placement outcomes.

The project covers the complete ML workflow from data collection and preprocessing to model training, evaluation, and deployment.

This system can help students understand their placement probability and identify important areas for improvement.

---

# Author

**Aditya Verma**

Student Placement Prediction System  
Machine Learning Project

---

# License

This project is created for educational purposes.
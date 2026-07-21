# 🎓 Student Placement Prediction System

A Machine Learning project that predicts whether a student is likely to be placed based on academic and skill-related attributes.

The project is developed using **Python**, **Scikit-learn**, and **Streamlit**, following a modular project structure with logging, exception handling, and reusable components.

---

## 📌 Features

- Student Placement Prediction
- Data Preprocessing
- Machine Learning Pipeline
- Logistic Regression Model
- Automatic Feature Scaling
- Streamlit Web Application
- Logging and Exception Handling
- Modular Project Structure
- Personalized Improvement Suggestions

---

## 📂 Project Structure

```
Placement_Predictor/
│
├── app.py
│
├── config/
│   └── config.py
│
├── data/
│   └── placement.csv
│
├── logs/
│
├── models/
│   └── placement_model.pkl
│
├── notebooks/
│   ├── 01_Data_Loading.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   ├── 04_Model_Evaluation.ipynb
│   └── 05_Model_Testing.ipynb
│
├── src/
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Logging Module
- Pickle
- Jupyter Notebook

---

## 📊 Dataset

The dataset contains student academic and skill-related information.

### Features

- IQ
- Previous Semester Result
- CGPA
- Academic Performance
- Internship Experience
- Extra Curricular Score
- Communication Skills
- Projects Completed

### Target Variable

- Placement
  - Yes
  - No

---

## 🤖 Machine Learning Model

The project uses a **Machine Learning Pipeline** consisting of:

- StandardScaler
- Logistic Regression

Pipeline:

```
Input Data
      │
      ▼
StandardScaler
      │
      ▼
Logistic Regression
      │
      ▼
Prediction
```

---

## 📈 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Student-Placement-Prediction-System.git
```

### Navigate to the Project

```bash
cd Student-Placement-Prediction-System
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📷 Application Workflow

1. Enter student details.
2. Click **Predict Placement**.
3. View prediction result.
4. Check placement probability.
5. Review personalized improvement suggestions.

---

## 📋 Example Input

| Feature | Value |
|----------|------:|
| IQ | 110 |
| Previous Semester Result | 8.2 |
| CGPA | 8.5 |
| Academic Performance | 8 |
| Internship Experience | Yes |
| Extra Curricular Score | 6 |
| Communication Skills | 9 |
| Projects Completed | 4 |

---

## 📌 Example Output

```
Prediction:
Student is Likely to be Placed

Placement Probability:
95.42%

Not Placed:
4.58%
```

---

## 📜 Logging

The application automatically records:

- Data Loading
- Data Preprocessing
- Model Training
- Model Evaluation
- Prediction Requests
- Exceptions

Logs are stored inside the **logs/** directory.

---

## ⚠ Exception Handling

A custom exception module is implemented to provide detailed error messages and improve debugging.

---

## 🎯 Future Improvements

- Support Multiple Machine Learning Models
- Hyperparameter Tuning
- Cross Validation
- Feature Importance Visualization
- Model Comparison Dashboard
- Cloud Deployment
- Database Integration
- User Authentication

---

## 👨‍💻 Author

**Aditya Verma**

BCA Student

Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.
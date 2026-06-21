# 🩺 Diabetes Prediction using Machine Learning

A web-based machine learning application that predicts the likelihood of diabetes based on medical parameters. The system uses a trained Logistic Regression model and provides real-time predictions through an interactive Flask web interface.

---

## 📌 Project Information

- **Institution:** Bangalore Technological Institute, Bengaluru
- **Department:** Artificial Intelligence & Machine Learning
- **Course:** Mini Project – 6th Semester (2025)
- **Project Guide:** Mrs. Dhivya C, Assistant Professor
- **Head of Department:** Dr. G. Gayatri Tanuja, HOD – AI & ML

---

## 👨‍💻 Team Members

| Name | USN |
|--------|------|
| Eshwar Pawan Peddi | 1BH22AI014 |
| G Udhbav | 1BH22AI016 |
| Sabari Govindhan | 1BH22AI038 |
| Tejas Halemani | 1BH22AI054 |

---

## 📖 Project Overview

Diabetes is one of the most prevalent chronic diseases worldwide. Early detection plays a crucial role in preventing complications and improving quality of life. This project leverages Machine Learning to predict the likelihood of diabetes based on several medical parameters.

Users provide health-related information through a simple web interface, and the trained model instantly returns a prediction. The application demonstrates how Artificial Intelligence can be applied in healthcare to assist in preliminary diagnosis and decision-making.

---

## 🎯 Objectives

- Predict the likelihood of diabetes using Machine Learning.
- Provide real-time predictions through a user-friendly web interface.
- Apply data preprocessing and feature scaling techniques for better model performance.
- Demonstrate the practical application of AI in healthcare.
- Build a deployable end-to-end machine learning application.

---

## 🧠 Machine Learning Model

- **Algorithm Used:** Logistic Regression
- **Dataset:** PIMA Indian Diabetes Dataset
- **Feature Scaling:** StandardScaler
- **Model Saving:** Pickle
- **Programming Language:** Python
- **Framework:** Flask

### Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling using StandardScaler
4. Model Training using Logistic Regression
5. Model Evaluation
6. Model Serialization using Pickle
7. Flask-Based Deployment

---

## 📊 Dataset Information

The project uses the **PIMA Indian Diabetes Dataset**, which contains medical diagnostic measurements used to predict diabetes.

### Features Used

| Feature | Description |
|-----------|------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin level |
| BMI | Body Mass Index |
| Diabetes Pedigree Function | Genetic predisposition to diabetes |
| Age | Age of the individual |

### Target Variable

- **0 → Non-Diabetic**
- **1 → Diabetic**

---

## 📈 Model Performance

| Metric | Value |
|----------|--------|
| Algorithm | Logistic Regression |
| Accuracy | ~85% |
| Feature Scaling | StandardScaler |
| Evaluation Metrics | Accuracy Score, Confusion Matrix |

> *Accuracy may vary depending on train-test split and preprocessing techniques.*

---

## ⚙️ Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap

### Backend
- Python
- Flask

### Machine Learning Libraries
- Scikit-learn
- Pandas
- NumPy
- Pickle

### Development Tools
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```text
Diabetes_Prediction/
│
├── static/
│   ├── style.css
│   └── images/
│
├── templates/
│   └── index.html
│
├── diabetes.csv
├── diabetes_model.pkl
├── app.py
├── model_training.ipynb
├── requirements.txt
└── README.md
```

---

## 🚀 Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/Diabetes-Prediction-Using-ML.git
cd Diabetes-Prediction-Using-ML
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask Application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## 🔄 Working of the System

1. User enters medical parameters.
2. Input data is preprocessed and scaled.
3. The trained Logistic Regression model receives the input.
4. The model predicts whether the person is diabetic or non-diabetic.
5. The result is displayed instantly on the web page.

---

## 🌟 Future Enhancements

- Implement Random Forest and SVM for improved accuracy.
- Add hyperparameter tuning.
- Deploy using Render or Heroku.
- Integrate user authentication.
- Store prediction history in a database.
- Develop a responsive dashboard for analysis.
- Add data visualization and charts.

---

## 📚 Libraries Used

```python
numpy
pandas
scikit-learn
flask
pickle
```

---

## 🏥 Applications

- Healthcare assistance
- Early diabetes risk assessment
- Medical decision support systems
- Educational and research purposes

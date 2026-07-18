# 👨‍💼 Employee Attrition Prediction System

A production-ready end-to-end Machine Learning project that predicts whether an employee is likely to leave an organization based on workplace, demographic, and job-related attributes.

The project follows a modular software engineering architecture with separate components for data ingestion, validation, preprocessing, model training, prediction, and deployment. The application is deployed using Streamlit and demonstrates production-oriented ML development practices.

---

# 🚀 Live Demo

**Application:** https://employee-attrition-prediction-repo.streamlit.app/
**GitHub Repository:** https://github.com/aneeshjo/employee-attrition-prediction

---

# 📌 Project Overview

Employee attrition is one of the most important business problems in Human Resource Analytics. Losing experienced employees increases recruitment costs, training expenses, and impacts organizational productivity.

This project uses Machine Learning to predict employee attrition, allowing organizations to identify employees at risk and make proactive retention decisions.

---

# 🎯 Objectives

- Predict employee attrition using supervised Machine Learning
- Build a modular and scalable ML pipeline
- Apply feature engineering and preprocessing
- Compare multiple classification algorithms
- Deploy the trained model using Streamlit
- Follow production-ready software engineering practices

---

# 📂 Project Structure

```
employee-attrition-prediction/

├── artifacts/
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── data_validation/
│   └── model_trainer/
│
├── config/
│   └── config.yaml
│
├── dataset/
│
├── logs/
│
├── notebook/
│
├── src/
│   └── employee_attrition/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       ├── utils/
│       └── exception/
│
├── app.py
├── main.py
├── params.yaml
├── schema.yaml
├── requirements.txt
└── README.md
```

---

# ⚙️ Machine Learning Pipeline

The project is organized into independent pipeline stages.

### 1. Data Ingestion

- Load employee dataset
- Train/Test split
- Store processed datasets

---

### 2. Data Validation

- Schema validation
- Data type validation
- Column validation
- Validation status reporting

---

### 3. Data Transformation

- Missing value handling
- Categorical encoding
- Numerical scaling
- Feature preprocessing pipeline
- Preprocessor serialization

---

### 4. Model Training

Multiple classification models were evaluated before selecting the final model.

Models experimented:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost
- XGBoost
- LightGBM

The best-performing model was selected based on evaluation metrics.

---

### 5. Prediction Pipeline

The prediction pipeline performs:

- User input collection
- Feature preprocessing
- Model inference
- Prediction generation

---

### 6. Streamlit Deployment

Interactive web application for real-time employee attrition prediction.

Features include:

- User-friendly interface
- Real-time predictions
- Model performance metrics
- Responsive design

---

# 📊 Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 91.04% |
| Precision | 89.04% |
| Recall    | 78.69% |
| F1 Score  | 83.54% |
| ROC-AUC   | 92.04% |

---

# 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- LightGBM
- XGBoost

### Visualization

- Matplotlib
- Seaborn

### Deployment

- Streamlit

### Configuration & Utilities

- PyYAML
- python-box
- Joblib
- Ensure

### Version Control

- Git
- GitHub

---

# 🏗️ Software Engineering Practices

This project follows production-oriented development practices.

- Modular architecture
- Configuration management
- Logging
- Custom exception handling
- Reusable pipelines
- Object-Oriented Programming
- YAML-based configuration
- Serializable preprocessing pipeline
- Production-ready project structure

---

# 📈 Future Improvements

- Docker containerization
- CI/CD pipeline
- Model monitoring
- Drift detection
- Cloud deployment (AWS/Azure/GCP)
- Experiment tracking using MLflow
- REST API using FastAPI
- Automated retraining pipeline

---

# 🧠 Key Learnings

Through this project, I gained practical experience in:

- End-to-end Machine Learning pipeline development
- Data preprocessing and feature engineering
- Model selection and evaluation
- Modular software architecture
- Configuration-driven development
- Streamlit deployment
- Git and GitHub workflows
- Production-ready ML project organization

---

# 👨‍💻 Author

**Aneesh Jose**

AI & Machine Learning Engineer

- GitHub: https://github.com/aneeshjo/employee-attrition-prediction
- LinkedIn: https://www.linkedin.com/in/aneeshjose012/
- Portfolio: https://aneeshjo.github.io/aneesh-portfolio/

---

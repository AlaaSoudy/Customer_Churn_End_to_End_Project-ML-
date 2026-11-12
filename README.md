# Customer Churn Prediction | End-to-End Machine Learning Project

An end-to-end Machine Learning project that predicts customer churn using the Telco Customer Churn dataset. The project covers the complete ML workflow, from data preprocessing and exploratory data analysis to model evaluation, ensemble learning, and deployment using Streamlit and Docker.

## Project Overview

Customer churn is a major challenge for subscription-based businesses. Predicting which customers are likely to leave helps companies take proactive actions to improve customer retention.

This project develops a classification system to identify customers who are likely to churn.

## Project Workflow

The project follows these main stages:

1. **Data Understanding:** Exploring the dataset and understanding its features.
2. **Data Cleaning:** Handling missing values and correcting data types.
3. **Exploratory Data Analysis (EDA):** Analyzing customer behavior and identifying churn patterns.
4. **Feature Engineering:** Preparing features for machine learning.
5. **Data Preprocessing:** Applying encoding and scaling techniques using Scikit-learn pipelines.
6. **Model Training:** Training and comparing multiple classification algorithms.
7. **Hyperparameter Tuning:** Improving model performance using cross-validation and GridSearchCV.
8. **Ensemble Learning:** Combining multiple models using a Voting Classifier.
9. **Model Evaluation:** Comparing models using Accuracy, Precision, Recall, F1-score, and ROC-AUC.
10. **Deployment:** Building an interactive Streamlit application.
11. **Containerization:** Packaging the application using Docker.

## Models Implemented

Several classification algorithms were explored and evaluated, including:

- Logistic Regression
- Naive Bayes
- Decision Tree
- Random Forest
- Gradient Boosting
- Other classification models
- Voting Classifier (Ensemble Learning)

### Best Model Performance

The Voting Classifier achieved the following evaluation results:

| Metric | Score |
|---|---:|
| Accuracy | 75.65% |
| Precision | 52.82% |
| Recall | 77.53% |
| F1-Score | 62.82% |
| ROC-AUC | 84.11% |

The model was selected based on its overall performance, particularly its ability to identify customers who are likely to churn.

## Streamlit Application

The project includes an interactive web application that allows users to:

- Enter customer information.
- Submit customer details to the trained model.
- Predict whether a customer is likely to churn.
- View prediction results through a user-friendly interface.

## Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Model Serialization:** Joblib
- **Web Application:** Streamlit
- **Containerization:** Docker
- **Development Environment:** Google Colab, Jupyter Notebook

## Repository Structure

```text
Customer_Churn_End_to_End_Project-ML-/
│
├── Customer_Churn_End_to_End_Project(ML).ipynb
├── Customer_Churn_End_to_End_Project(ML).zip
│
├── app.py
├── churn_model.pkl
├── requirements.txt
├── Dockerfile
│
├── README.md
└── LICENSE
```

## Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/AlaaSoudy/Customer_Churn_End_to_End_Project-ML-.git
```

### 2. Navigate to the Project Directory

```bash
cd Customer_Churn_End_to_End_Project-ML-
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

## Run with Docker

Make sure Docker is installed and running.

### 1. Build the Docker Image

```bash
docker build -t customer-churn-app .
```

### 2. Run the Container

```bash
docker run -p 8501:8501 customer-churn-app
```

### 3. Access the Application

```text
http://localhost:8501
```

## Future Improvements

- Experiment with advanced ensemble learning techniques.
- Improve model performance through additional feature engineering.
- Apply model explainability techniques such as SHAP.
- Deploy the application to a cloud platform.
- Monitor model performance and data drift.

## Author

**Alaa Soudy Ibrahim Ibrahim**

Communication and Electronics Engineering Student | Machine Learning Enthusiast

GitHub: [@AlaaSoudy](https://github.com/AlaaSoudy)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

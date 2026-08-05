# 👥 Employee Attrition Prediction

This project focuses on analyzing employee attrition patterns and developing a classification model to predict whether an employee is likely to leave the company.

Employee turnover is a major challenge for organizations, as losing employees can increase recruitment costs and affect productivity. Understanding the factors associated with employee attrition can help identify potential risks and support better retention decisions.

The project includes data understanding, data cleaning, exploratory data analysis (EDA), feature engineering, model development, and evaluation.

A Logistic Regression model was selected as the main model due to its interpretability, allowing better understanding of how different employee characteristics are associated with attrition.


## 📂 Repository Structure

```text
Employee-Attrition-Prediction/
│
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── Employee_Attrition_Prediction.ipynb
└── README.md
```

## 📊 Dataset

The dataset used in this project is the **IBM HR Analytics Employee Attrition & Performance Dataset**.

It contains employee demographic, job-related, and workplace satisfaction information used to analyze factors associated with employee turnover.

### Features

Examples:
- Age
- Department
- Job Role
- Monthly Income
- OverTime
- Job Satisfaction
- Years At Company

### Target

- Attrition (Employee left or stayed)

Dataset Source:
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset


## 🔍 Exploratory Data Analysis

The analysis focused on understanding employee characteristics and identifying patterns related to attrition.

The notebook includes:

- Data distribution analysis
- Attrition rate analysis
- Correlation analysis
- Employee tenure analysis
- Salary-related analysis
- Attrition comparison across:
  - Gender
  - Department
  - Job Role
  - Overtime
  - Business Travel
  - Marital Status
  - Satisfaction levels


## 📌 Key Findings

The exploratory analysis highlighted several patterns associated with employee attrition:

- Employees with lower Job Satisfaction and Environment Satisfaction showed higher attrition rates.
- Overtime showed a noticeable relationship with employee turnover, with higher attrition among employees working overtime.
- Employees with shorter tenure and early career stages showed higher attrition patterns.
- Monthly Income showed a clearer difference between employees who left and those who stayed compared to other salary-related features.
- Frequent business travelers and single employees showed higher attrition rates.
- Higher job levels generally showed lower attrition rates.


## 🛠 Feature Engineering

Based on observations from the exploratory analysis, additional features were created to better represent employee career patterns:

### FirstYear

Identifies employees in their first or second year at the company, as early-tenure employees showed noticeable attrition patterns.


### AgeGroup

Groups employees into different career stages to better capture the relationship between age and attrition.


### FirstCareerYear

Identifies employees at the beginning of their careers, as early-career employees showed higher attrition patterns.


## 🤖 Model Development

### Logistic Regression

Logistic Regression was selected as the primary classification model because of its interpretability.

The goal was not only to predict employee attrition, but also to build a model that provides better understanding of the factors associated with employees leaving the company.


## 📈 Model Evaluation

The model was evaluated using classification metrics, with additional focus on the Attrition class due to the imbalance between employees who stayed and employees who left.


| Metric | Score |
|--------|-------|
| Accuracy | 87.30% |
| Precision (Attrition) | 0.73 |
| Recall (Attrition) | 0.34 |
| F1-score (Attrition) | 0.46 |


## 🔮 Future Improvements

This project can be further improved by:

- Comparing Logistic Regression with additional classification algorithms such as Random Forest and XGBoost.
- Applying hyperparameter tuning to optimize model performance.
- Exploring feature selection techniques.
- Applying methods to handle class imbalance and improve detection of employees likely to leave.


## 🛠 Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn


## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/Employee-Attrition-Prediction.git
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Open the Jupyter Notebook and run all cells.

---

## 👩‍💻 Author

**Areena Almeshaly**

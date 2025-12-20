# Customer Churn Analysis

## 📌 Project Overview
This project analyzes telecom customer churn to identify key factors influencing customer attrition using SQL and Python.

## 🛠 Tools & Technologies
- SQL (MySQL)
- Python (Pandas, Matplotlib)
- VS Code

## 📊 Key Analysis
- Overall churn rate analysis
- Churn by contract type
- Churn by payment method
- Churn by customer tenure

## 📈 Key Insights
- Overall churn rate is ~26.6%, indicating significant customer attrition.
- Month-to-month contracts show the highest churn (~43%).
- Customers using electronic check payment method have higher churn.
- New customers (0–12 months tenure) are more likely to churn.

## 📂 Project Structure
Customer-Churn-Analysis/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── python/
│   └── churn_analysis.py
│
├── sql/
│   └── churn_analysis.sql
│
├── plots/
│   ├── churn_distribution.png
│   ├── churn_by_contract.png
│   ├── churn_by_payment.png
│   └── churn_by_tenure.png
│
└── README.md

## 📊 Visual Insights

### Customer Churn Distribution
![Churn Distribution](plots/churn_by_distribution.png)

### Churn by Contract Type
![Churn by Contract](plots/churn_by_contract.png)

### Churn by Payment Method
![Churn by Payment](plots/churn_by_payment.png)

### Churn by Tenure
![Churn by Tenure](plots/churn_by_tenure.png)

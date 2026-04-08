# electricity-bill-prediction
ML project to predict electricity bills using regression.
## Overview
This project predicts electricity bills using machine learning based on household features.

## Features
- Number of rooms
- Number of people
- House area
- AC usage
- TV usage
- Flat type
- Income
- Number of children
- Urban area

## Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree
- Random Forest
- KNN
- SVR
- XGBoost

## Best Model
Decision Tree Regressor gave the best performance based on R² score and error metrics.

## GUI
Developed using Streamlit.

## Files
- app.py
- ebill_prediction_model.pkl
- scaler.pkl
- electricty_bill_data.csv
- Electricity_bill_prediction.ipynb

## Run
python -m streamlit run app.py

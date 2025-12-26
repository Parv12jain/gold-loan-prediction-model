Gold Loan / Gold Price Prediction

This project predicts the gold price (or gold loan value) using machine learning.
It uses financial indicators like stock market index, oil price, silver price, and currency exchange rate.

The trained model is saved as a .pkl file and deployed using Streamlit.

What this project does

Takes financial inputs such as:

S&P 500 index (SPX)

Oil price (USO)

Silver price (SLV)

EUR/USD exchange rate

Predicts the gold price

Shows the prediction on a simple web interface

Machine Learning Model

Algorithm used: Decision Tree Regressor

Type: Regression

Target column: Gold price (GLD)

Files in this project
gold-loan-prediction/
│
├── gold_loan.ipynb      # Jupyter notebook (training & analysis)
├── goldloan.pkl         # Trained model file
├── app.py               # Streamlit app
├── requirements.txt     # Required libraries
├── README.md            # Project description

How to run this project
Step 1: Install required libraries
pip install -r requirements.txt

Step 2: Run the Streamlit app
streamlit run app.py

Technologies used

Python

NumPy

Pandas

Scikit-learn

Streamlit

Pickle

Result

The model gives good predictions with:

High R² score

Low prediction error

Proper train-test split (no data leakage)

What I learned from this project

How to build a regression model

How to handle time-based data correctly

How to save and load ML models using pickle

How to deploy a model using Streamlit

Author

Parv Jain

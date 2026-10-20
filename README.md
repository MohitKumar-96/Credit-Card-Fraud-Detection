# 💳 Credit Card Fraud Detection Web App

A lightweight, interactive web application built with **Streamlit** and **Machine Learning** to evaluate and detect whether a credit card transaction is legitimate or fraudulent.

---

## 🚀 Features
- **Real-Time Analysis:** Input transaction parameters (`Time`, `Amount`, and PCA features `V1-V3`) to instantly evaluate fraud risk.
- **Interactive UI:** Clean web interface with adjustable numeric fields and streamlined inputs.
- **Optimized Model Loading:** Uses cached resources for fast performance.

---

## 📂 Project Structure
```text
creaditcard/
├── app.py                  # Main Streamlit application script
├── credit_card_model.pkl   # Trained machine learning model (Serialized)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🛠️ Installation & Setup

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/MohitKumar-96/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
Execute the following command in your terminal:
```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`.

---

## 📊 Dataset & Inputs
This model is built using transaction data structured around standard credit card attributes:
- **Time:** Seconds elapsed between the first transaction and the current transaction.
- **Transaction Amount ($):** The monetary value of the transaction.
- **PCA Features (V1 - V3):** Dimension-reduced components representing confidential transaction details (features V4–V28 default to `0.0` for quick analysis).

---

## 📝 Requirements (`requirements.txt`)
```text
streamlit
numpy
pandas
scikit-learn
joblib
```
*(Note: Ensure your `credit_card_model.pkl` file is properly trained and saved in the root folder before launching the app).*

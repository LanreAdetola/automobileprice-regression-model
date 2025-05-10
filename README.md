
---

# 🚗 Lanry's Car Price Prediction App

A simple and interactive Streamlit web application that predicts car prices using a machine learning model deployed on Azure. Users can enter detailed specifications about a car, and the app returns an estimated market price.

---

## 📌 Features

* User-friendly form for inputting car attributes
* Real-time price prediction using Azure Machine Learning
* Secure integration using Streamlit secrets for API management
* Handles missing data for normalized losses gracefully

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – For building the interactive UI
* **Azure Machine Learning** – Hosting the trained ML model
* **REST API** – Communication between the app and the ML model

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 2. Install dependencies

You can use pip to install the required packages:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```text
streamlit
requests
```

### 3. Set up Streamlit Secrets

Create a `.streamlit/secrets.toml` file with your Azure credentials:

```toml
[azure]
API_URL = "https://your-azure-api-endpoint"
API_KEY = "your-azure-api-key"
```

### 4. Run the app

```bash
streamlit run app.py
```

> Make sure to replace `app.py` with the actual filename if it's different.

---

## 📄 How It Works

1. The user inputs various car attributes.
2. The app prepares a JSON payload and sends it to the Azure ML API.
3. Azure ML returns a predicted price based on the trained model.
4. The app displays the predicted car price.

---

## 📸 Screenshot

*(Optional: Add a screenshot of your app here using Markdown or image upload)*

---

## 🔒 Security Note

API keys are stored using Streamlit's built-in secrets management to avoid exposing sensitive data in your codebase.

---

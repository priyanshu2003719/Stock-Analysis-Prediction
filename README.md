# 📊 Stock Analysis & Prediction Suite

> 🚀 A complete **Financial Data Science Platform** combining **CAPM, Technical Analysis, and Time-Series Forecasting** in an interactive **Streamlit Web App**.

---

## ✨ Overview

This project is a **multi-module stock intelligence system** that helps investors:

* 📈 Analyze stock performance
* ⚖️ Measure risk using **CAPM (Beta & Expected Return)**
* 🔍 Apply **technical indicators (RSI, MACD, SMA)**
* 🤖 Forecast future prices using **ARIMA models**

---

## 🧠 Core Technologies

* 🐍 Python
* 📊 **Streamlit** – Interactive UI
* 📉 **Plotly** – Advanced visualizations
* 💹 **yfinance** – Market data
* 🧮 **NumPy / Pandas** – Data processing
* 🤖 **Statsmodels (ARIMA)** – Forecasting
* 📚 **ta (Technical Analysis Library)**

---

## 🏗️ Project Architecture

```bash
Stock-Analysis-Prediction/
│
├── 📊 Trading_App.py          # Landing Dashboard
├── 📈 CAPM_Return.py         # CAPM Web App (Frontend)
├── 🧮 capm_functions.py      # CAPM Engine (Backend)
├── 📉 plotly_figure.py       # Visualization Engine
├── 🏢 Stock_Analysis.py      # Full Stock Dashboard
├── 🤖 model_train.py         # ML Model (ARIMA)
└── 🔮 Stock_Prediction.py    # Prediction Interface
```

---

# 📌 Modules Breakdown

---

## 📈 CAPM Web Application

### 🔹 What it Does

* Calculates **Expected Return using CAPM**
* Computes **Beta (β)** via regression
* Compares stocks with **S&P 500 benchmark**

### 📊 CAPM Formula

```math
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
```

### 🚀 Features

* 📌 Sector-based stock selection
* ⏳ Custom time horizon
* 🔄 Real-time data (yfinance + FRED)
* 📊 Interactive Plotly charts

---

## 🧮 CAPM Analytical Engine (`capm_functions.py`)

### ⚙️ Key Functions

* `normalize()` → Compare % growth
* `daily_return()` → Compute returns
* `calculate_beta()` → Linear regression

### 📌 Insights

* 🔺 β > 1 → Aggressive stock
* 🔻 β < 1 → Defensive stock

---

## 🏢 Trading App (`Trading_App.py`)

### 🎯 Purpose

Acts as the **central hub** for all tools.

### 🧩 Features

* Clean UI with **Streamlit**
* Navigation to:

  * Stock Info
  * CAPM Analysis
  * Prediction Engine
  * Beta Calculator

---

## 📊 Visualization Engine (`plotly_figure.py`)

### 📈 Indicators Included

* 📉 RSI (Overbought/Oversold)
* 🔀 MACD (Trend Signals)
* 📊 Moving Averages
* 🕯️ Candlestick Charts

### 🚀 Highlights

* Interactive zoom & sliders
* Forecast vs Historical separation
* Professional-grade tables

---

## 📊 Stock Analysis Dashboard (`Stock_Analysis.py`)

### 🔍 Capabilities

* Company fundamentals
* Financial ratios (P/E, ROE, etc.)
* Market metrics (Beta, Market Cap)
* Technical indicators

### 💼 Use Cases

* 📊 Fundamental Analysis
* ⚖️ Risk Profiling
* 📉 Trend Evaluation

---

## 🤖 ML Engine (`model_train.py`)

### ⚙️ Model Used

* **ARIMA (30, d, 30)**

### 🔄 Pipeline

1. Stationarity check (ADF Test)
2. Differencing
3. Model training
4. Forecast generation
5. RMSE evaluation

### 📊 RMSE Formula

```math
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
```

---

## 🔮 Stock Prediction App (`Stock_Prediction.py`)

### 🚀 Features

* 📌 Custom ticker input
* 📉 30-day forecast
* 📊 RMSE accuracy score
* 📈 Interactive forecast chart

### 🎨 Visualization Logic

* ⚫ Black → Historical data
* 🔴 Red → Predicted trend

---

# 📊 Key Capabilities

✔️ **Risk Analysis** → CAPM Beta
✔️ **Return Estimation** → Expected Return
✔️ **Technical Analysis** → RSI, MACD
✔️ **Forecasting** → ARIMA Predictions
✔️ **Visualization** → Interactive dashboards

---

# 💼 Business Value

* 📉 Reduce investment uncertainty
* ⚖️ Compare risk vs reward
* 📊 Make data-driven decisions
* 🤖 Remove emotional bias

---

# 🧪 Data Science Highlights

### ✔️ Predictive Modeling

* ARIMA for time-series forecasting
* Linear regression for Beta

### ✔️ Data Preprocessing

* Stationarity (ADF Test)
* Rolling averages
* Feature scaling

### ✔️ Model Evaluation

* RMSE for accuracy
* Visual validation with charts

---

# 🎯 Final Outcome

This project delivers a **full-stack financial analytics system** that:

* Combines **Machine Learning + Finance**
* Transforms raw data into **actionable insights**
* Provides a **professional-grade trading dashboard**

---

# ⭐ Future Improvements

* 📡 Live trading integration
* 🧠 Deep learning models (LSTM)
* 🌍 Multi-market support
* 📊 Portfolio optimization

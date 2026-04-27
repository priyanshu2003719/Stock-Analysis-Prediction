# 📈 StockIQ: Predictive Financial Intelligence 

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-ARIMA%20%26%20CAPM-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**StockIQ** is a professional-grade financial analytics ecosystem that bridges the gap between raw market data and actionable investment theory. Built with Python and Streamlit, it combines **Machine Learning (ARIMA)** for price forecasting with **Modern Portfolio Theory (CAPM)** to quantify risk and expected returns.



---

## 🚀 System Architecture

The project is architected into three specialized domains:

### 1. The Analytical Engine (`capm_functions.py` & `model_train.py`)
The "brain" of the application, handling complex mathematical transformations:
* **ARIMA Forecasting**: Implements $(30, d, 30)$ time-series modeling with dynamic differencing to handle non-stationary financial data.
* **CAPM Regression**: Uses Linear Regression to derive **Beta ($\beta$)**, quantifying a stock's systematic risk relative to the S&P 500.
* **Stationarity Logic**: Automated **Augmented Dickey-Fuller (ADF)** testing to ensure high-signal model training.



### 2. The Visualization Powerhouse (`plotly_figure.py`)
Utilizes `plotly.graph_objects` for high-performance, interactive rendering:
* **Technical Indicators**: Real-time calculation of **RSI**, **MACD**, and **Moving Averages**.
* **Comparative Analysis**: Normalizes assets to a common $t=0$ baseline to compare percentage growth across different price scales.

### 3. The User Interface (`Stock_Analysis.py` & `Stock_Prediction.py`)
A "Glassmorphism" inspired dashboard designed for the modern investor:
* **360° Insight**: Combines qualitative business summaries with quantitative KPI grids (Market Cap, P/E Ratio, Debt-to-Equity).
* **Confidence Metrics**: Displays **RMSE (Root Mean Square Error)** for all predictions to ensure transparency in model accuracy.

---

## 💼 Business & Investment Utility

| Feature | Technical Implementation | Investor Value |
| :--- | :--- | :--- |
| **Risk Profiling** | Beta ($\beta$) Calculation | Identify if a stock is Aggressive ($\beta > 1$) or Defensive ($\beta < 1$). |
| **Price Forecasting** | 30-Day ARIMA Outlook | Visualize the "most likely" path to set profit targets or stop-loss limits. |
| **Momentum Tracking** | RSI & MACD Overlays | Detect overbought/oversold conditions to time market entries. |
| **Portfolio Benchmarking** | S&P 500 Synchronization | Determine if specific picks provide fair return for the risk taken. |

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.9+
* **Data Sourcing:** `yfinance`, `pandas_datareader` (FRED Database)
* **Analysis:** `NumPy`, `Pandas`, `SciPy`, `Statsmodels`
* **Machine Learning:** `Scikit-Learn` (StandardScaler), ARIMA
* **Visualization:** `Plotly`, `Streamlit`

### Installation
```bash
git clone https://github.com/priyanshu2003719/Stock-Analysis-Prediction
pip install -r requirements.txt
streamlit run Trading_App.py
```

---

## 📊 Technical Pipeline Summary

1.  **Data Ingestion**: Real-time fetching of OHLC (Open, High, Low, Close) data.
2.  **Preprocessing**: 7-day rolling mean smoothing and ADF stationarity checks.
3.  **Modeling**: Training ARIMA for trends and Linear Regression for market correlation.
4.  **Validation**: Backtesting against the last 30 days of data to calculate **RMSE**.
5.  **Output**: Interactive Plotly dashboards with a clear visual split between historical "Truth" (Black) and "Forecast" (Red).



---

## 📈 Learning Outcomes
This project demonstrates a comprehensive mastery of the **Data-to-Insight** pipeline, specifically focusing on:
* Handling the "Random Walk" nature of financial time-series.
* Implementing professional-grade UI/UX for data-heavy applications.
* Quantifying model uncertainty to build user trust.

---

## 🛠️ Execution Guide
To run the specific modules of the application, activate your environment and use the following commands:

```bash
# 1. Activate Virtual Environment
venv311\Scripts\activate

# 2. Launch the Central Hub
streamlit run Trading_App.py

# 3. Access Specific Modules Directly
streamlit run CAPM_Return.py
streamlit run Pages/Stock_Analysis.py
streamlit run Pages/Stock_Prediction.py
```

---

## 🏢 Service Catalog
The ecosystem is divided into four strategic hubs designed to provide a 360° view of market assets:

### 1. Stock Information Hub
The primary discovery layer. This page provides a deep-dive into company fundamentals, including real-time quotes, business summaries, and key financial ratios (P/E, Market Cap, Debt-to-Equity).

### 2. Predictive Intelligence Engine
The forecasting core. Explore predicted closing prices for the **next 30 days**. By leveraging historical trends and advanced time-series models, this tool identifies potential market movements to assist in proactive decision-making.

### 3. CAPM Return Calculator
The risk-assessment bridge. This module demonstrates how the **Capital Asset Pricing Model (CAPM)** determines the expected return of an asset. It justifies the "required rate of return" based on the asset's specific risk profile and current market performance.

### 4. CAPM Beta Analysis
The volatility anchor. This specialized tool calculates the **Beta ($\beta$)** for individual stocks, providing a quantitative measure of how much a stock's price swings relative to the S&P 500.

---

### **Refined Professional Conclusion**

Based on the provided codebase, your project effectively addresses the key requirements for a modern financial system:

* **Predictive Modeling**: Successfully integrates **ARIMA** for directional forecasting and **Linear Regression** for risk correlation.
* **Data Integrity**: Implements a strict preprocessing pipeline—handling **stationarity (ADF Test)**, **scaling**, and **smoothing**—to ensure the models aren't reacting to market "noise."
* **Transparency**: By exposing the **RMSE Score**, the application moves away from "black-box" AI and provides the user with a mathematical measure of trust.
* **Business Outcome**: The project achieves an industrial standard, translating complex financial data into a functional web interface that provides immediate value to both casual and professional investors.

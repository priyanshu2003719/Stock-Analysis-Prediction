# Stock-Analysis-Prediction
 Stock Analysis Forecasting &amp; its Time Series Analysis

i)## 📈 Capital Asset Pricing Model (CAPM) Web Application

This repository contains a **Streamlit-based financial analytics tool** designed to calculate the expected return of individual stocks using the **Capital Asset Pricing Model (CAPM)**. By leveraging real-time market data, the application helps investors understand the relationship between systematic risk and expected return.

---

### 📂 Code Structure & Logic

The application is built using a modular Python structure, separating the UI logic from the financial calculations:

1.  **Frontend (`CAPM_Return.py`)**: 
    * Manages the user interface using **Streamlit**.
    * Handles data orchestration: fetching ticker data via `yfinance` and economic data (S&P 500) via `pandas_datareader` from the FRED database.
    * Processes data cleaning, date synchronization, and merges market data with stock data into a unified DataFrame.
2.  **Backend (`capm_functions.py`)**:
    * A helper module (imported as `capm_functions`) containing the core mathematical logic.
    * **Functions included**: Data normalization, daily return calculation, and linear regression to derive **Beta ($\beta$)** and **Alpha ($\alpha$)**.

---

### 🚀 Key Features

* **Dynamic Sector Selection**: Stocks are grouped by categories (e.g., Tech, Growth & AI, Finance) to allow for quick peer-group comparisons.
* **Customizable Time Horizons**: Users can specify the number of years of historical data to analyze, directly impacting the sensitivity of the Beta calculation.
* **Real-Time Data Integration**: Pulls the most recent closing prices for any listed ticker and the S&P 500 index.
* **Automated Risk Metrics**: Automatically calculates the Beta for each selected stock, representing its volatility relative to the broader market.

---

### 📊 Interactive Visualizations

The app utilizes **Plotly** to provide interactive, high-fidelity charts that allow for deep-dive analysis:

* **Price History**: A standard time-series plot of the selected stocks' closing prices.
* **Normalized Comparison**: A crucial visualization where all stock prices are scaled to a common starting point (usually 1.0). This allows users to compare the **percentage growth** of stocks regardless of their absolute dollar price.
* **Metrics Tables**: Clean, scannable dataframes showing calculated **Beta values** and the **Final Expected Returns** derived from the CAPM formula.

---

### 💼 Business & Investment Utility

This tool bridges the gap between raw market data and actionable investment theory:

* **Risk Assessment**: By calculating **Beta**, the app tells an investor if a stock is more volatile ($\beta > 1$) or less volatile ($\beta < 1$) than the market.
* **Portfolio Benchmarking**: It uses the S&P 500 as a proxy for the market, helping users determine if their specific stock picks are providing a fair return for the risk taken.
* **Expected Return Forecasting**: It automates the CAPM formula:
    $$E(R_i) = R_f + \beta_i (E(R_m) - R_f)$$
    This provides a theoretical "required rate of return," helping investors decide if a stock is currently undervalued or overvalued based on market trends.

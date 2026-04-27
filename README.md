# Stock-Analysis-Prediction
 Stock Analysis Forecasting &amp; its Time Series Analysis

## i) 📈 Capital Asset Pricing Model (CAPM) Web Application

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

## ii) CAPM Analytical Engine: `capm_functions.py`

This module serves as the **computational backend** for the Capital Asset Pricing Model (CAPM) application. It contains the mathematical logic and visualization wrappers required to transform raw financial data into actionable investment insights.

---

### 📂 Code Structure & Logic

The module is designed with a functional programming approach, where each function handles a specific stage of the data processing pipeline:

* **`interactive_plot(df)`**: A wrapper for `plotly.express` that iterates through dataframe columns to generate a multi-line time-series chart. It includes custom layout configurations for a clean, professional UI.
* **`normalize(df_2)`**: A data transformation function that scales all stock prices relative to their initial value at $t=0$. This is mathematically represented as:
    $$Price_{normalized} = \frac{Price_t}{Price_0}$$
* **`daily_return(df)`**: This function calculates the periodic percentage change in price, which is the standard input for financial volatility modeling. It uses a nested loop to compute:
    $$Return_t = \frac{P_t - P_{t-1}}{P_{t-1}} \times 100$$
* **`calculate_beta(stocks_daily_return, stock)`**: The core analytical function. It utilizes `numpy.polyfit` to perform a first-degree polynomial (linear) regression. The slope of this regression line represents the **Beta ($\beta$)**, indicating the stock's sensitivity to market movements.

---

### 💼 Business & Investment Utility

By isolating these functions, the application provides high-level business value:

1.  **Risk Quantification**: Through the `calculate_beta` function, investors can identify "Aggressive" stocks ($\beta > 1$) or "Defensive" stocks ($\beta < 1$).
2.  **Relative Performance Tracking**: The `normalize` function allows users to compare a low-priced stock (e.g., $\$20$) with a high-priced stock (e.g., $\$3000$) on an equal footing to see which has truly yielded better percentage returns.
3.  **Market Correlation**: It establishes how closely a stock's daily movements mirror the S&P 500, helping in the construction of diversified portfolios.

---

### 🚀 Key Features

* **Vectorized Computation**: Uses **NumPy** for high-performance mathematical operations, ensuring that even years of daily data are processed instantly.
* **Data Integrity**: Includes a `.copy()` mechanism within the transformation functions (`normalize` and `daily_return`) to prevent accidental modification of the original dataset (avoiding "SettingWithCopy" warnings).
* **Scalability**: The looping structures in the plotting and normalization functions allow the code to handle any number of stocks selected by the user without requiring manual code changes.

---

### 📊 Visualization Capabilities

The module leverages **Plotly** to move beyond static charts:

* **Comparative Analysis**: The `interactive_plot` function allows users to toggle individual stocks on and off via a horizontal legend, facilitating side-by-side comparisons of specific assets.
* **Dynamic Resizing**: The layout is set to `width=450` with tight margins, ensuring the charts fit perfectly within the Streamlit columns defined in the main application.
* **Zero-Baseline Normalization**: By forcing the first entry of the daily return to `0`, the charts provide a clean starting point for all assets, making the visual data more intuitive for end-users.

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

## iii ) 🏢 Landing Hub: `Trading_App.py`

This script serves as the **central gateway** for the Trading Guide ecosystem. It is designed as a high-level landing page that introduces users to the suite of financial tools available, emphasizing professional aesthetics and clear service navigation.

---

### 📂 Code Structure & Logic

The application follows a streamlined, top-down UI design using the **Streamlit** framework:

* **Page Configuration**: It initializes the web environment with a "wide" layout and financial iconography (`📉`) to establish immediate professional context.
* **HTML Integration**: The script uses `unsafe_allow_html=True` to inject custom CSS styles for headers, allowing for precise control over font weights and sizes that standard Markdown cannot achieve.
* **Visual Assets**: A primary hero image (`app.avif`) is utilized to create a modern, engaging interface for first-time visitors.
* **Service Routing Description**: The code outlines four distinct modules, providing the descriptive text that will guide users toward more technical tools like the CAPM calculators.

---

### 🚀 Key Features

* **High-Impact Branding**: Features a large, bold title ("Trading Guide App 📊") and a professional sub-header to build user trust.
* **Modular Service Index**: Clearly lists the platform's capabilities—Stock Information, CAPM Return, Stock Prediction, and CAPM Beta—in an organized, numbered format.
* **Responsive Layout**: By setting `layout="wide"`, the application ensures that the landing page content is optimized for various screen resolutions, from laptops to large desktop monitors.

---

### 💼 Business & Investment Utility

From a business perspective, this file acts as the **User Experience (UX) anchor**:

1.  **Value Proposition**: It immediately informs the investor that this is a comprehensive platform for collecting critical data "prior to investing in stocks".
2.  **Educational Pathing**: It simplifies complex financial concepts (like CAPM) by providing concise summaries of what each tool does before the user dives into the technical data.
3.  **Informed Decision Making**: By highlighting "predicted closing prices" and "market performance," the app positions itself as a tool for reducing investment uncertainty.

---

### 📊 Visual Layout Summary

The UI is architected into four logical sections to ensure a smooth user journey:

| Section | Content Type | Purpose |
| :--- | :--- | :--- |
| **Header** | Styled HTML Text | Establish the app's identity and primary mission. |
| **Hero** | Local Image Asset | Provide a modern, professional visual identity. |
| **Services** | Header & Markdown | Summarize the four key analytical tools available. |
| **Definitions** | Descriptive Text | Briefly explain how CAPM and Beta assist the user. |

## iv) 📊 Financial Visualization Engine: `plotly_figure.py`

This module is the **visualization powerhouse** of the application, utilizing `plotly.graph_objects` to create high-performance, interactive financial charts. It integrates the `ta` (Technical Analysis) library to calculate professional-grade indicators directly from raw price data.

---

### 📂 Code Structure & Logic

The module is organized into a suite of specialized functions designed for financial data manipulation and rendering:

* **Data Orchestration**: The `filter_data` function acts as a utility to slice DataFrames into specific time windows (e.g., 1 month, 1 year, Year-to-Date) using `dateutil` for precise relative time calculations.
* **Technical Indicator Integration**: Functions like `RSI`, `Moving_average`, and `MACD` leverage the `ta` library to append technical signals to the dataset before rendering them.
* **Forecast Mapping**: The `Moving_average_forecast` function distinguishes between historical and predicted data by plotting them as separate traces (Black for history, Red for future) on a unified timeline.
* **Tabular UI**: Beyond charts, `plotly_table` provides a customized, CSS-styled table component with alternating row colors for high readability of raw financial figures.

---

### 🚀 Key Features

* **Multi-Indicator Support**: Provides a comprehensive suite of technical tools including **Relative Strength Index (RSI)**, **Moving Average Convergence Divergence (MACD)**, and **Simple Moving Averages (SMA)**.
* **Interactive Time-Scaling**: Integrated range sliders in the `close_chart` and `Moving_average` functions allow users to zoom into specific price actions without losing context of the overall trend.
* **Advanced Chart Types**: Includes a `candlestick` function for traditional price action analysis, showing the Open, High, Low, and Close (OHLC) for every period.
* **Dynamic Styling**: Uses consistent color palettes (e.g., `#e1efff` for paper backgrounds) to ensure the visual identity remains professional and easy on the eyes during long research sessions.

---

### 💼 Business & Investment Utility

This module transforms abstract numbers into visual intelligence for traders:

1.  **Momentum Analysis**: The **RSI** tool identifies overbought ($>70$) and oversold ($<30$) conditions, helping investors spot potential price reversals.
2.  **Trend Confirmation**: By overlaying a **50-day SMA**, the module allows users to determine if a stock is in a long-term uptrend or downtrend relative to its daily noise.
3.  **Signal Detection**: The **MACD** function visualizes the relationship between two moving averages, providing "Signal" and "Histogram" traces used by pros to identify entry and exit points.
4.  **Forecasting Clarity**: The specialized forecast chart clearly separates "what happened" from "what is predicted," enabling a logical transition from historical review to future planning.

---

### 📊 Visualization Components

| Function | Visualization Type | Key Components |
| :--- | :--- | :--- |
| `candlestick` | OHLC Candlesticks | Traditional green/red bars showing price range. |
| `RSI` | Oscillator Chart | Includes a shaded area between 30 and 70 for volatility boundaries. |
| `MACD` | Dual-Line Plot | Compares the MACD line against its Signal line to find crossovers. |
| `plotly_table` | Data Grid | Professional-grade header and alternating row colors for financial reporting. |
| `close_chart` | Multi-Line Plot | Simultaneous tracking of Open, Close, High, and Low prices. |

## v) 📊 Industrial-Grade Stock Intelligence: `Stock_Analysis.py`

This module represents the most comprehensive analytical tool in the repository, designed to provide a 360-degree view of a company’s financial health and market performance. It serves as a professional-grade dashboard that combines qualitative business summaries with quantitative technical indicators.

---

### 📂 Code Structure & Logic

The script is built with a clear hierarchy that guides the user from high-level discovery to deep-dive technical analysis:

* **Dynamic Data Ingestion**: The application uses `yfinance` to fetch both real-time market quotes and static organizational data based on a user-provided ticker (e.g., "TSLA").
* **Modular Utility Integration**: It imports specialized visualization functions from the `Pages.utils.plotly_figure` module, ensuring that complex charts like RSI and MACD are rendered consistently.
* **Multi-Pane UI Layout**: Using Streamlit’s column system (`st.columns`), the code organizes data into logical clusters:
    * **Overview Pane**: Business summaries and company profiles.
    * **KPI Pane**: A grid of financial metrics (Price, Market Cap, Beta, P/E Ratio).
    * **Historical Pane**: A 15-day tabular lookback of recent price action.
* **State-Driven Visualization**: The `num_period` and `chart_type` variables capture user interactions (button clicks and dropdown selections) to dynamically update the rendering engine without refreshing the entire page.

---

### 🚀 Key Features

* **Smart Metric Formatting**: Custom helper functions like `format_market_cap` and `format_percent` automatically scale large numbers (e.g., converting billions to "B" or trillions to "T") to maintain a clean, readable interface.
* **Technical Indicator Toggle**: Users can switch between "Candle" and "Line" charts and overlay specific technical signals like **RSI**, **Moving Averages**, or **MACD** on the fly.
* **Flexible Time Horizons**: Integrated time-range buttons (5D, 1M, 1Y, YTD, MAX) allow for instant switching between short-term day trading views and long-term investment perspectives.
* **Live Price Delta**: The app calculates and displays the immediate daily change in both dollar value and percentage, providing instant market context.

---

### 💼 Business & Investment Utility

This module is designed for the modern investor who requires more than just a price chart:

1.  **Fundamental Analysis**: By displaying the "Business Summary" and "Key Financial Ratios" (Debt to Equity, Return on Equity), the app helps users evaluate the underlying strength of a company.
2.  **Valuation Benchmarking**: Metrics like the **P/E Ratio** and **Forward P/E** allow investors to assess if a stock is overvalued or undervalued relative to its earnings.
3.  **Risk Profiling**: The inclusion of **Beta** and **52-Week High/Low** ranges provides a clear picture of the asset's historical volatility and current price positioning.
4.  **Operational Insights**: Detailed data such as sector, industry, and full-time employee count gives investors a qualitative understanding of the company's operational scale.

---

### 📊 Visualization Components


The dashboard orchestrates several complex visual components to create a unified intelligence report:

| Component | Purpose | Logic |
| :--- | :--- | :--- |
| **Financial KPI Grid** | Rapid Health Check | Displays 9 critical metrics including Market Cap and Beta. |
| **Financial Tables** | Deep-Dive Data | Uses `plotly_table` to show Profit Margins and Debt ratios side-by-side. |
| **Main Price Chart** | Trend Analysis | Supports interactive Candlestick and Line formats. |
| **Indicator Sub-Charts** | Timing Entries/Exits | Dedicated areas for momentum (RSI) and trend strength (MACD). |

## vi) 🤖 Predictive Intelligence Engine: `model_train.py`

This module provides the **machine learning and statistical backend** for the "Stock Prediction" service mentioned in the main `Trading_App.py`. It focuses on time-series forecasting using the ARIMA (AutoRegressive Integrated Moving Average) model to predict future stock prices based on historical trends.

---

### 📂 Code Structure & Logic

The script follows a rigorous data science pipeline to ensure the accuracy and stability of its forecasts:

* **Data Acquisition**: The `get_data` function pulls historical closing prices from Yahoo Finance, specifically targeting data from the start of 2025.
* **Stationarity Processing**: For a time-series model like ARIMA to work, the data must be "stationary" (statistical properties don't change over time). The module uses the **Augmented Dickey-Fuller (ADF) test** to check for this and applies a "differencing loop" to transform the data until it meets the required criteria.
* **Model Architecture**: The system utilizes an `ARIMA(30, d, 30)` configuration. The "d" parameter is dynamically calculated by the differencing loop to ensure the model adapts to the specific volatility of the selected stock.
* **Validation Framework**: The `evaluate_model` function performs a "Train-Test Split," training the model on historical data while reserving the last 30 days to calculate the **Root Mean Square Error (RMSE)**, providing a quantitative measure of the model's reliability.

---

### 🚀 Key Features

* **Dynamic Differencing**: Automatically detects if a stock price is trending too aggressively and applies mathematical transformations to stabilize the data for better prediction.
* **30-Day Forecasting**: Generates a future-dated DataFrame containing predicted closing prices for the next full month.
* **Data Scaling**: Includes `StandardScaler` utilities to normalize price data, which helps in stabilizing the model's internal mathematical calculations.
* **Rolling Mean Analysis**: Provides a 7-day rolling average function to smooth out daily "noise" and identify the underlying price momentum.

---

### 💼 Business & Investment Utility

This module transforms historical "noise" into structured future insights:

1.  **Trend Anticipation**: By forecasting 30 days out, it helps traders visualize potential price directions rather than just reacting to past events.
2.  **Accuracy Transparency**: By calculating the RMSE, the app tells the user exactly how "wrong" the model was on recent data, allowing the investor to weigh the prediction's risk accordingly.
3.  **Algorithmic Consistency**: Standardizes the forecasting process across different stocks, removing emotional bias from price predictions.


---

### 📊 Technical Pipeline Summary

| Phase | Function | Outcome |
| :--- | :--- | :--- |
| **Check** | `stationary_check` | Determines if the data is stable enough for modeling. |
| **Clean** | `get_differencing_order` | Removes trends to make the data stationary. |
| **Train** | `fit_model` | Fits the ARIMA model to the processed price data. |
| **Predict** | `get_forecast` | Produces a 30-day price outlook with a proper date index. |
| **Validate** | `evaluate_model` | Scores the prediction's accuracy using RMSE. |

## vii) 🔮 Predictive Insights Engine: `Stock_Prediction.py`

This module serves as the **forecasting frontend** of the Trading App. It provides an intuitive interface for users to generate 30-day price predictions using sophisticated time-series modeling, making complex machine learning accessible to everyday investors.

---

### 📂 Code Structure & Logic

The script acts as a coordinator between the raw data processing logic and the visual presentation layer:

* **Integration Core**: It imports high-level functions from `model_train.py` (for the ARIMA logic) and `plotly_figure.py` (for the rendering logic), ensuring a clean separation between the "brains" and the "face" of the application.
* **Sequential Pipeline**:
    1.  **Data Fetching**: Retrieves historical data for the user-specified ticker.
    2.  **Smoothing**: Applies a 7-day rolling mean to reduce daily market "noise" before the model sees the data.
    3.  **Stationarity Logic**: Calculates the differencing order ($d$) needed to make the series predictable.
    4.  **Transformation**: Scales the data using standard normalization to improve model convergence.
    5.  **Evaluation**: Runs a backtest to generate an **RMSE (Root Mean Square Error)** score, telling the user how much the model's predictions deviated from actual history.
    6.  **Forecasting & Reversal**: Generates 30 days of future data and "inverse scales" it back into actual dollar values for the user.

---

### 🚀 Key Features

* **Custom Ticker Input**: Users can enter any valid stock symbol (e.g., AAPL, TSLA, BTC-USD) to generate instant localized forecasts.
* **Real-time Accuracy Scoring**: The **RMSE Score** provides transparency, allowing the user to judge the reliability of the current prediction based on the stock's recent volatility.
* **Rolling Average Base**: By training on the rolling mean rather than raw closing prices, the model focuses on the **underlying trend** rather than erratic daily spikes.
* **Dual Data Preview**: Combines a high-precision interactive chart with a detailed forecast table for users who need exact numerical values for their spreadsheets.

---

### 📊 Visualization Excellence

The module employs specialized visualization techniques to differentiate between "known" facts and "calculated" possibilities:

* **Forecast Table**: A professional-grade Plotly table displaying the next 30 days of predicted prices, sorted chronologically and rounded for readability.
* **Moving Average Forecast Chart**: This is the visual centerpiece. It uses color-coding to distinguish data:
    * **Black Line**: Represents the historical 7-day rolling price (The Truth).
    * **Red Line**: Represents the 30-day ARIMA prediction (The Forecast).
    * This visual separation helps users immediately identify where the history ends and the prediction begins.



---

### 💼 Business & Investment Utility

This tool provides significant strategic value for both casual and professional traders:

1.  **Risk Management**: The RMSE score acts as a "confidence meter." A high RMSE warns the user that the stock is currently too volatile for reliable short-term prediction.
2.  **Trend Anticipation**: Instead of looking purely at the past, investors can visualize a mathematically derived "most likely" path for the next month, helping them set realistic profit targets or stop-loss limits.
3.  **Algorithmic Consistency**: By relying on the ARIMA model, the tool removes emotional bias (fear or greed) from the forecasting process, providing a cold, mathematical perspective on price action.
4.  **Operational Planning**: For long-term investors, the 30-day outlook can assist in timing entries or exits to maximize capital efficiency.

Based on the provided codebase, here is the explanation of how your project addresses each of the specific requirements for building a predictive financial system, followed by a conclusion for each.

---

### **Predictive Modeling & Algorithms**
**Code Implementation:**
Your project utilizes two distinct mathematical approaches to forecast and analyze trends:
* **Time-Series Modeling (`model_train.py`)**: It implements an **ARIMA (AutoRegressive Integrated Moving Average)** model. The engine uses a $(30, d, 30)$ configuration where $d$ is dynamically calculated to ensure data stationarity.
* **Regression Analysis (`capm_functions.py`)**: It uses **Linear Regression** via `np.polyfit` to calculate the Beta ($\beta$) of a stock. This predicts how a stock will move relative to the market based on historical correlation.

**Conclusion:** The system successfully combines **statistical forecasting** (ARIMA) for price direction with **probabilistic modeling** (CAPM) for risk-adjusted returns, providing a multi-layered predictive framework.

---

### **Data Cleaning and Preprocessing**
**Code Implementation:**
Financial data is inherently "noisy." Your code manages this through several preprocessing layers:
* **Stationarity Logic**: In `model_train.py`, the `get_differencing_order` function uses the **Augmented Dickey-Fuller (ADF)** test. If the $p-value > 0.05$, the code iteratively applies differencing until the data is stationary.
* **Smoothing**: The `get_rolling_mean` function applies a 7-day window to eliminate daily outliers and reveal the underlying trend.
* **Feature Scaling**: The `scaling` function uses `StandardScaler` to transform prices into a distribution with a mean of $0$ and a standard deviation of $1$, which is critical for the stability of the ARIMA algorithm.
* **Date Synchronization**: In `CAPM_Return.py`, the code localizes timezones and performs an "inner join" between stock data and S&P 500 data to ensure perfectly aligned dates for regression.

**Conclusion:** The robust preprocessing pipeline ensures that the models are trained on **high-signal, stationary data**, which significantly reduces the risk of "spurious regressions" or biased forecasts.

---

### **Model Evaluation and Visualization**
**Code Implementation:**
The project doesn't just predict; it validates its own accuracy:
* **Accuracy Metrics**: The `evaluate_model` function in `model_train.py` performs a backtest using a **Train-Test Split**. It reserves the last 30 days of data and calculates the **Root Mean Square Error (RMSE)**:
    $$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$
* **Interactive Visuals**: `Stock_Prediction.py` uses Plotly to overlay the forecast. The `Moving_average_forecast` function creates a clear visual distinction between historical data (black) and the 30-day forecast (red).
* **Technical Overlays**: `Stock_Analysis.py` provides secondary validation using indicators like **RSI** and **MACD** to confirm if the predicted trend aligns with market momentum.

**Conclusion:** By exposing the **RMSE Score** to the user and providing interactive, color-coded charts, the application fosters **transparency and trust** in its data-driven predictions.

---

### **Learning Outcomes & Business Expected Outcome**
**Code Implementation:**
The integration of these scripts demonstrates a deep understanding of the "Data-to-Insight" pipeline:
* **Predictive Modeling**: You have learned to handle the complexity of ARIMA parameters and stationarity requirements.
* **Trend Analysis**: Through the `normalize` and `rolling_mean` functions, you’ve mastered the ability to compare assets of different scales and filter out market volatility.
* **Data-Driven Forecasting**: The transition from `Trading_App.py` (landing) to `Stock_Prediction.py` (outcome) shows a complete business application that translates raw CSV-style data into a strategic investment tool.

**Conclusion:** The project achieves a professional standard in **Financial Data Science**, moving beyond simple charting to create a system that can quantify risk ($\beta$), measure error ($RMSE$), and project future value within a modern web interface.

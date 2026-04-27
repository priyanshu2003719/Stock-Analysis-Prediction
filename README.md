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

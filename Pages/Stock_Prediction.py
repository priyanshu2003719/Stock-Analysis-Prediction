import streamlit as st
import pandas as pd
from Pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, scaling, evaluate_model
from Pages.utils.plotly_figure import plotly_table, Moving_average_forecast
from Pages.utils.model_train import (
    get_data,
    get_rolling_mean,
    get_differencing_order,
    scaling,
    evaluate_model,
    get_forecast,
    inverse_scaling
)

# ====================== PAGE CONFIG ======================
import streamlit as st

st.set_page_config(
    page_title="Stock Prediction",
    page_icon="📉",   # emoji works better than string name
    layout="wide"
)

# ====================== TITLE ======================
st.title("📊 Stock Prediction")

# ====================== INPUT SECTION ======================
col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input("Stock Ticker", "AAPL")

# ====================== MODEL SECTION ======================
rmse = 0

st.subheader(f"Predicting Next 30 Days Close Price for: {ticker}")

# ====================== DATA ======================
close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

# ====================== PREPROCESSING ======================
differencing_order = get_differencing_order(rolling_price)

scaled_data, scaler = scaling(rolling_price)


# ====================== MODEL EVALUATION ======================
rmse = evaluate_model(scaled_data, differencing_order)


st.write("**Model RMSE Score:**", rmse)


# ====================== FORECAST ======================
forecast = get_forecast(scaled_data, differencing_order)
forecast = inverse_scaling(scaler, forecast)

# ====================== FORECAST TABLE ======================

forecast["Close"] = inverse_scaling(
    scaler,
    forecast["Close"]
)

st.write("##### Forecast Data (Next 60 days)")

fig_tail = plotly_table(
    forecast
    .sort_index(ascending=True)
    .round(2)
)

fig_tail.update_layout(height=220)

st.plotly_chart(
    fig_tail,
    use_container_width=True
)

# ====================== MERGE DATA ======================
forecast = pd.concat(
    [rolling_price, forecast],
    axis=0
)

# ====================== PLOT ======================
st.plotly_chart(
    Moving_average_forecast(forecast.iloc[150]),
    use_container_width=True
)
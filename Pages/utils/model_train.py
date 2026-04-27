# ====================== IMPORTS ======================
import yfinance as yf
import numpy as np
import pandas as pd

from datetime import datetime, timedelta

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


# ====================== DATA FETCH ======================
def get_data(ticker):
    stock_data = yf.download(ticker, start="2025-01-01")
    return stock_data[["Close"]]


# ====================== STATIONARITY CHECK ======================
def stationary_check(close_price):
    adf_test = adfuller(close_price)
    p_value = round(adf_test[1], 3)
    return p_value


# ====================== ROLLING MEAN ======================
def get_rolling_mean(close_price):
    rolling_price = (
        close_price
        .rolling(window=7)
        .mean()
        .dropna()
    )
    return rolling_price

# ====================== DIFFERENCING ORDER ======================
def get_differencing_order(close_price):

    # ---------------- Initial Stationarity Check ----------------
    p_value = stationary_check(close_price)
    d = 0

    # ---------------- Differencing Loop ----------------
    while True:
        if p_value > 0.05:
            d += 1

            close_price = close_price.diff().dropna()
            p_value = stationary_check(close_price)
        else:
            break

    return d

# ====================== MODEL FITTING ======================
def fit_model(data, differencing_order):

    # ---------------- Model Training ----------------
    model = ARIMA(data, order=(30, differencing_order, 30))
    model_fit = model.fit()

    # ---------------- Forecasting ----------------
    forecast_steps = 30
    forecast = model_fit.get_forecast(steps=forecast_steps)

    # ---------------- Predictions ----------------
    predictions = forecast.predicted_mean

    return predictions


# ====================== MODEL EVALUATION ======================
def evaluate_model(original_price, differencing_order):

    # ---------------- Train-Test Split ----------------
    train_data = original_price[:-30]
    test_data = original_price[-30:]

    # ---------------- Model Prediction ----------------
    predictions = fit_model(train_data, differencing_order)

    # ---------------- RMSE Calculation ----------------
    rmse = np.sqrt(mean_squared_error(test_data, predictions))

    return round(rmse, 2)


# ====================== SCALING ======================
def scaling(close_price):

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(
        np.array(close_price).reshape(-1, 1)
    )

    return scaled_data, scaler

# ====================== FORECAST GENERATION ======================
def get_forecast(original_price, differencing_order):

    # ---------------- Model Prediction ----------------
    predictions = fit_model(original_price, differencing_order)

    # ---------------- Date Range ----------------
    start_date = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=29)).strftime("%Y-%m-%d")
 

    forecast_index = pd.date_range(
        start=start_date,
        end=end_date,
        freq="D"
    )

    # ---------------- DataFrame Creation ----------------
    forecast_df = pd.DataFrame(
        predictions,
        index=forecast_index,
        columns=["Close"]
    )

    return forecast_df


# ====================== INVERSE SCALING ======================
def inverse_scaling(scaler, scaled_data):

    close_price = scaler.inverse_transform(
        np.array(scaled_data).reshape(-1, 1)
    )

    return close_price
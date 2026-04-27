import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import datetime
import ta
from Pages.utils.plotly_figure import plotly_table
from Pages.utils.plotly_figure import (
    plotly_table,
    close_chart,
    candlestick,
    RSI,
    Moving_average,
    MACD
)


# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📊",
    layout="wide"
)

# ---------------- Helper Functions ----------------
def get_value(data, key, default="Not Available"):
    value = data.get(key, default)
    return default if value is None else value

def format_market_cap(value):
    if value is None or value == "Not Available":
        return "Not Available"
    if value >= 1_000_000_000_000:
        return f"${value / 1_000_000_000_000:.2f}T"
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    return f"${value:,.0f}"

def format_percent(value):
    if value is None or value == "Not Available":
        return "Not Available"
    return f"{value * 100:.2f}%"

# ---------------- Header ----------------
st.markdown(
    """
    <div>
       <h1><div class="title-text"><b>📊 Stock Analysis</b></div></h1>
        <div class="subtitle-text">
           <h2><b>Industrial-grade stock intelligence for company profile, valuation, risk, and market insights.</b></h2>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- Inputs ----------------
col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker", "TSLA").upper()

with col2:
    start_date = st.date_input(
        "Choose Start Date",
        datetime.date(today.year - 1, today.month, today.day)
    )

with col3:
    end_date = st.date_input(
        "Choose End Date",
        today
    )

# ---------------- Stock Info ----------------
stock = yf.Ticker(ticker)
info = stock.info

st.markdown(f"## {ticker} Overview")

# ---------------- Company Overview ----------------
left_col, right_col = st.columns([2, 1])

with left_col:
    st.markdown("### 📝 Business Summary")

    summary = get_value(info, "longBusinessSummary", "")

    if summary:
        for sentence in summary.split(". ")[:6]:
            if sentence.strip():
                st.markdown(f"- {sentence.strip().rstrip('.')}.")
    else:
        st.info("Business summary not available.")

with right_col:
    st.markdown("### 🏢 Company Profile")

    st.markdown(
        f"""
        <div class="company-card">
            <p><b>📊 Sector:</b> {get_value(info, "sector")}</p>
            <p><b>🏭 Industry:</b> {get_value(info, "industry")}</p>
            <p><b>🌍 Country:</b> {get_value(info, "country")}</p>
            <p><b>👥 Employees:</b> {get_value(info, "fullTimeEmployees")}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    website = get_value(info, "website", None)
    if website:
        st.markdown(f"**{ticker} Website**: [{website}]({website})")

st.markdown("---")

# ---------------- Financial KPI Section ----------------
st.markdown("### 📊 Key Financial Metrics")

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Current Price", get_value(info, "currentPrice"))

with col4:
    st.metric("Market Cap", format_market_cap(get_value(info, "marketCap", None)))

with col5:
    st.metric("Dividend Yield", format_percent(get_value(info, "dividendYield", None)))

col6, col7, col8 = st.columns(3)

with col6:
    st.metric("52W High", get_value(info, "fiftyTwoWeekHigh"))

with col7:
    st.metric("52W Low", get_value(info, "fiftyTwoWeekLow"))

with col8:
    st.metric("Beta", get_value(info, "beta"))

col9, col10, col11 = st.columns(3)

with col9:
    st.metric("P/E Ratio", get_value(info, "trailingPE"))

with col10:
    st.metric("Forward P/E", get_value(info, "forwardPE"))

with col11:
    st.metric("Price to Book", get_value(info, "priceToBook"))

st.markdown("---")

st.markdown("### 📊 Financial Overview")

col12, col13 = st.columns(2)

with col12:
    st.markdown("#### 💰 Key Financials")

    df = pd.DataFrame({
        "Metric": ['Market Cap', 'Beta', 'EPS', 'P/E Ratio'],
        "Value": [
            stock.info.get("marketCap"),
            stock.info.get("beta"),
            stock.info.get("trailingEps"),
            stock.info.get("trailingPE")
        ]
    })

    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)


with col13:
    st.markdown("#### 📈 Financial Ratios")

    df = pd.DataFrame({
        "Metric": [
            'Quick Ratio',
            'Revenue per Share',
            'Profit Margins',
            'Debt to Equity',
            'Return on Equity'
        ],
        "Value": [
            stock.info.get("quickRatio"),
            stock.info.get("revenuePerShare"),
            stock.info.get("profitMargins"),
            stock.info.get("debtToEquity"),
            stock.info.get("returnOnEquity")
        ]
    })

    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)

data = yf.download(ticker , start=start_date, end= end_date)



col14, col15, col16 = st.columns(3)

current = data['Close'][ticker].iloc[-1]
previous = data['Close'][ticker].iloc[-2]

daily_change = current - previous
percent_change = (daily_change / previous) * 100

with col14:
    st.metric(
        "📊 Daily Change",
        f"${current:.2f}",
        f"{daily_change:.2f} ({percent_change:.2f}%)"
    )
last_15_df = data.tail(15).sort_index(ascending = False).round(3)
fig_df = plotly_table(last_15_df)


st.write('##### Historical Data (Last 15 days)')
st.plotly_chart(fig_df, use_container_width=True)

# ---------------- TIME RANGE BUTTONS ----------------

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

num_period = ""

with col1:
    if st.button("5D"):
        num_period = "5d"

with col2:
    if st.button("1M"):
        num_period = "1mo"

with col3:
    if st.button("6M"):
        num_period = "6mo"

with col4:
    if st.button("YTD"):
        num_period = "ytd"

with col5:
    if st.button("1Y"):
        num_period = "1y"

with col6:
    if st.button("5Y"):
        num_period = "5y"

with col7:
    if st.button("MAX"):
        num_period = "max"


# ===================== CHART CONTROLS =====================

col1, col2, col3 = st.columns([1, 1, 4])


# -------- Chart Type Selection --------
with col1:
    chart_type = st.selectbox(
        label="",
        options=("Candle", "Line")
    )


# -------- Indicator Selection --------
with col2:

    if chart_type == "Candle":
        indicators = st.selectbox(
            label="",
            options=("RSI", "MACD")
        )

    else:
        indicators = st.selectbox(
            label="",
            options=("RSI", "Moving Average", "MACD")
        )

# ===================== DATA FETCH =====================

ticker_ = yf.Ticker(ticker)

new_df1 = ticker_.history(period="max")
data1   = ticker_.history(period="max")


# ===================== CHART RENDERING =====================

if num_period == "":

    # -------- Candle + RSI --------
    if chart_type == "Candle" and indicators == "RSI":
        st.plotly_chart(
            candlestick(data1, "1y"),
            use_container_width=True
        )
        st.plotly_chart(
            RSI(data1, "1y"),
            use_container_width=True
        )

    # -------- Candle + MACD --------
    if chart_type == "Candle" and indicators == "MACD":
        st.plotly_chart(
            candlestick(data1, "1y"),
            use_container_width=True
        )
        st.plotly_chart(
            MACD(data1, "1y"),
            use_container_width=True
        )

    # -------- Line + RSI --------
    if chart_type == "Line" and indicators == "RSI":
        st.plotly_chart(
            close_chart(data1, "1y"),
            use_container_width=True
        )
        st.plotly_chart(
            RSI(data1, "1y"),
            use_container_width=True
        )

    # -------- Line + Moving Average --------
    if chart_type == "Line" and indicators == "Moving Average":
        st.plotly_chart(
            Moving_average(data1, "1y"),
            use_container_width=True
        )
    
    # -------- Line + MACD --------
    if chart_type == 'Line' and indicators == 'MACD':
        st.plotly_chart(
            close_chart (data1, '1y'), 
            use_container_width=True
        )
        st.plotly_chart (
            MACD (data1, 'ly'), 
            use_container_width=True
        )

else:

    # -------- Candle + RSI --------
    if chart_type == "Candle" and indicators == "RSI":
        st.plotly_chart(
            candlestick(new_df1, num_period),
            use_container_width=True
        )
        st.plotly_chart(
            RSI(new_df1, num_period),
            use_container_width=True
        )

    # -------- Candle + MACD --------
    if chart_type == "Candle" and indicators == "MACD":
        st.plotly_chart(
            candlestick(new_df1, num_period),
            use_container_width=True
        )
        st.plotly_chart(
            MACD(new_df1, num_period),
            use_container_width=True
        )

    # -------- Line + RSI --------
    if chart_type == "Line" and indicators == "RSI":
        st.plotly_chart(
            close_chart(new_df1, num_period),
            use_container_width=True
        )
        st.plotly_chart(
            RSI(new_df1, num_period),
            use_container_width=True
        )

    # -------- Line + Moving Average --------
    if chart_type == "Line" and indicators == "Moving Average":
        st.plotly_chart(
            Moving_average(new_df1, num_period),
            use_container_width=True
        )

    # -------- Line + MACD --------
    if chart_type == "Line" and indicators == "MACD":
        st.plotly_chart(
            close_chart(new_df1, num_period),
            use_container_width=True
        )
        st.plotly_chart(
            MACD(new_df1, num_period),
            use_container_width=True
        )
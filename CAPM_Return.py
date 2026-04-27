# importing libraries

import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import  pandas_datareader.data as web
import capm_functions as capm_functions
import numpy as np


st.set_page_config(
    page_title = "CAPM",
    page_icon = "📈",
    layout = 'wide')
st.title("Capital Asset Pricing Model")


# ---------------- getting input from user ----------------
col1, col2, col3 = st.columns(3)

# Categories
stock_categories = {
    "💻 Tech": ['AAPL', 'MSFT', 'GOOGL', 'META', 'NVDA', 'ORCL', 'IBM'],
    "🚀 Growth & AI": ['TSLA', 'PLTR', 'RBLX', 'AI'],
    "🛒 E-Commerce": ['AMZN', 'SHOP', 'EBAY', 'ETSY', 'SPOT', 'NFLX'],
    "🏦 Finance": ['JPM', 'BAC', 'WFC', 'GS', 'MS', 'PYPL', 'SQ'],
    "⚡ Energy": ['XOM', 'CVX', 'COP'],
    "💊 Healthcare": ['PFE', 'JNJ', 'MRK', 'ABBV'],
    "🍔 Consumer": ['KO', 'PEP', 'MCD', 'SBUX', 'DIS'],
    "🚗 Auto": ['TSLA', 'F', 'GM'],
    "🌍 International": ['BABA', 'TSM', 'ASML']
}

# Column 1 → Category
with col1:
    category = st.selectbox("Select Category", list(stock_categories.keys()))

# Column 2 → Stocks based on category
with col2:
    stocks_list = st.multiselect(
        "Choose Stocks",
        stock_categories[category],
        default=stock_categories[category][:3]
    )

# Column 3 → Years
with col3:
    year = st.number_input("Number of years", 1, 100, value=5)

#downloding data for SP500
try:
    end= datetime.date.today()
    start = datetime.date(datetime.date.today().year-year, datetime.date.today().month, datetime.date.today().day)
    SP500 = web.DataReader (['sp500'], 'fred', start, end)
    print(SP500.head())
    print(SP500.tail())

    stocks_df = pd.DataFrame()

    for stock in stocks_list:
        data= yf.download(stock, period= f'{year}y')
        stocks_df[f'{stock}'] = data['Close']

    stocks_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)
    print(stocks_df.dtypes)
    print(SP500.dtypes)

    SP500.rename(columns={'DATE': 'Date'}, inplace=True)
    stocks_df['Date'] = stocks_df['Date'].dt.tz_localize(None)

    stocks_df[ 'Date'] = stocks_df['Date'].astype('datetime64[ns]')
    stocks_df['Date'] = stocks_df ['Date'].apply(lambda x:str(x)[:10])
    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    stocks_df = pd.merge(stocks_df, SP500, on = 'Date', how = 'inner')
    print(stocks_df)

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("### Dataframe head")
        st.dataframe(stocks_df.head(), use_container_width = True)
    with col2:
        st.markdown("### Dataframe tail")
        st.dataframe(stocks_df.tail(), use_container_width = True)

    col1 , col2 = st.columns([1,1])
    with col1:
        st.markdown("### Price of all the Stocks")
        st.plotly_chart(capm_functions.interactive_plot(stocks_df))
    with col2:
        st.markdown("### Price of all the Stocks (After Normalizing)")
        st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)))

    stocks_daily_return = capm_functions.daily_return(stocks_df)
    print(stocks_daily_return.head())


    beta  = {}
    alpha = {}

    for i in stocks_daily_return.columns:
        if i != 'Date' and i != 'sp500':
            b,a = capm_functions.calculate_beta(stocks_daily_return,i)
            
            beta[i] = b
            alpha[i] = a
    print(beta , alpha)

    beta_df = pd.DataFrame(columns=['Stock','Beta Value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta Value'] = [str(round(i,2)) for i in beta.values()]


    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown('### Calculated Beta Value')
        st.dataframe(beta_df, use_container_width=True)

    rf=0
    rm =stocks_daily_return['sp500'].mean()*252
    return_df = pd.DataFrame()
    return_value = []
    for stock , value in  beta.items():
        return_value.append(str(round(rf+(value*(rf-rm)),2)))
    return_df['Stock'] = stocks_list

    return_df['Return Value'] = return_value

    with col2:
        st.markdown('### Calculated Return using CAPM')
        st.dataframe(return_df, use_container_width=True)
except:
    st.write("Please Select Valid Inputs")
    

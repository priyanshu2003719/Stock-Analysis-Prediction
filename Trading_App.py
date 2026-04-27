import streamlit as st


st.set_page_config(
    page_title="Trading App",
    page_icon="📉",
    layout="wide"
)

# Title & Header
st.markdown(
    "<h1 style='font-weight:900; font-size:48px;'>Trading Guide App 📊</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h2 style='font-weight:700;'>We provide the Greatest platform for you to collect all information prior to investing in stocks.</h2>",
    unsafe_allow_html=True
)

# Image
st.image("app.avif", use_container_width=True)

# Services Section
st.markdown(
    "<h2 style='font-weight:900;'>✨ We Provide the Following Services</h2>",
    unsafe_allow_html=True
)

st.markdown("### 1️⃣ Stock Information")
st.write("Through this page, you can see all the information about stock.")

st.markdown("### 3️⃣ CAPM Return")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models. Use this tool to gain valuable insights into market trends and make informed investment decisions.")


st.markdown("### 2️⃣ Stock Prediction")
st.write("Discover how the Capital Asset Pricing Model (CAPM) calculates the expected return of different stocks asset based on its risk and market performance.")

st.markdown("### 4️⃣ CAPM Beta")
st.write("Calculates Beta and Expected Return for Individual Stocks.")


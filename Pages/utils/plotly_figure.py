import plotly.graph_objects as go
import dateutil
import datetime
import ta


def plotly_table(dataframe):
    headerColor = '#1f77d0'
    rowEvenColor = '#e6eef8'
    rowOddColor = '#ffffff'

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=[f"<b>{col}</b>" for col in dataframe.columns],
            fill_color=headerColor,
            line_color=headerColor,
            align='left',
            font=dict(color='white', size=15),
            height=35
        ),
        cells=dict(
            values=[dataframe[col] for col in dataframe.columns],
            fill_color=[[rowOddColor, rowEvenColor] * len(dataframe)],
            align='left',
            line_color='white',
            font=dict(color='black', size=14),
            height=32
        )
    )])

    fig.update_layout(
        height=40 + len(dataframe) * 32,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    return fig


def filter_data(dataframe, num_period):
    if num_period == "1mo":
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)

    elif num_period == "5d":
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)

    elif num_period == "6mo":
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)

    elif num_period == "1y":
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-1)

    elif num_period == "5y":
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-5)

    elif num_period == "ytd":
        date = datetime.datetime(dataframe.index[-1].year, 1, 1).strftime("%Y-%m-%d")

    else:
        date = dataframe.index[0]

    df_reset = dataframe.reset_index()

    return df_reset[df_reset["Date"] > date]


def close_chart(dataframe, num_period=False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["Open"], mode="lines", name="Open", line=dict(width=2, color="#5ab7ff")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["Close"], mode="lines", name="Close", line=dict(width=2, color="black")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["High"], mode="lines", name="High", line=dict(width=2, color="#0078ff")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["Low"], mode="lines", name="Low", line=dict(width=2, color="red")))

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        legend=dict(yanchor="top", xanchor="right")
    )

    return fig


def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=dataframe["Date"],
            open=dataframe["Open"],
            high=dataframe["High"],
            low=dataframe["Low"],
            close=dataframe["Close"]
        )
    )

    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff"
    )

    return fig


def RSI(dataframe, num_period):
    dataframe["RSI"] = ta.momentum.RSIIndicator(dataframe["Close"]).rsi()

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["RSI"], name="RSI", marker_color="orange", line=dict(width=2, color="orange")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=[70] * len(dataframe), name="Overbought", marker_color="red", line=dict(width=2, color="red", dash="dash")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=[30] * len(dataframe), fill="tonexty", name="Oversold", marker_color="#79da84", line=dict(width=2, color="#79da84", dash="dash")))

    fig.update_layout(
        yaxis_range=[0, 100],
        height=200,
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )

    return fig


def Moving_average(dataframe, num_period):
    dataframe["SMA_50"] = ta.trend.SMAIndicator(
        dataframe["Close"],
        window=50
    ).sma_indicator()

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["Open"], mode="lines", name="Open", line=dict(width=2, color="#5ab7ff")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["Close"], mode="lines", name="Close", line=dict(width=2, color="black")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["High"], mode="lines", name="High", line=dict(width=2, color="#0078ff")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["Low"], mode="lines", name="Low", line=dict(width=2, color="red")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["SMA_50"], mode="lines", name="SMA 50", line=dict(width=2, color="purple")))

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        legend=dict(yanchor="top", xanchor="right")
    )

    return fig


def MACD(dataframe, num_period):
    macd_indicator = ta.trend.MACD(dataframe["Close"])

    dataframe["MACD"] = macd_indicator.macd()
    dataframe["MACD Signal"] = macd_indicator.macd_signal()
    dataframe["MACD Hist"] = macd_indicator.macd_diff()

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["MACD"], name="MACD", marker_color="orange", line=dict(width=2, color="orange")))
    fig.add_trace(go.Scatter(x=dataframe["Date"], y=dataframe["MACD Signal"], name="Signal", marker_color="red", line=dict(width=2, color="red", dash="dash")))

    colors = ["red" if cl < 0 else "green" for cl in dataframe["MACD Hist"].fillna(0)]

    fig.update_layout(
        height=200,
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )

    return fig

def Moving_average_forecast(forecast):

    # ====================== FIGURE ======================
    fig = go.Figure()

    # ====================== HISTORICAL CLOSE PRICE ======================
    fig.add_trace(
        go.Scatter(
            x=forecast.index[:-30],
            y=forecast["Close"].iloc[:-30],
            mode="lines",
            name="Close Price",
            line=dict(width=2, color="black")
        )
    )

    # ====================== FUTURE CLOSE PRICE ======================
    fig.add_trace(
        go.Scatter(
            x=forecast.index[-31:],
            y=forecast["Close"].iloc[-31:],
            mode="lines",
            name="Future Close Price",
            line=dict(width=2, color="red")
        )
    )

    # ====================== LAYOUT ======================
    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        legend=dict(
            yanchor="top",
            xanchor="right"
        )
    )

    return fig
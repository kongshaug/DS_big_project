# imports ----
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import talib as ta
import yfinance as yf
import seaborn as sns
yf.pdr_override()


# for testing

# tesla_close = np.array(data["Close"])
# tesla_high = np.array(data["High"])
# tesla_open = np.array(data["Open"])
# tesla_low = np.array(data["Low"])

# ADX kan bruges til at se om den opad eller nedadgående trend er stærk


def signal_RSI(close):


def signal_RSI_and_SMA(close):
    in_position = False
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30

    # for testing
    close = numpy.array(tesla_close)

    rsi = talib.RSI(close, RSI_PERIOD)

    sma = talib.SMA(close)

    buy = []
    sell = []
    for r, c, s in zip(rsi, close, sma):
        if r < RSI_OVERSOLD and s < c and in_position == False:
            buy.append(c)
            in_position = True

        else:
            buy.append(0)

        if r > RSI_OVERBOUGHT and in_position == True:
            sell.append(c)
            in_position = False
        else:
            sell.append(0)


def signal_SMA(close):
    in_position = False
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30

    # for testing
    close = numpy.array(tesla_close)

    sma = talib.SMA(close, 300)

    buy = []
    sell = []
    for c, s in zip(close, sma):
        if s < c and in_position == False:
            buy.append(c)
            in_position = True
        else:
            buy.append(0)

        if s > c and in_position == True:
            sell.append(c)
            in_position = False
        else:
            sell.append(0)


def signal_macd(close):
    in_position = False
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30

    # for testing
    close = numpy.array(tesla_close)

    sma = talib.SMA(close, 100)
    macd, signal, hist = ta.MACD(
        tesla_close, fastperiod=12, slowperiod=26, signalperiod=9)
    buy = []
    sell = []
    for c, s in zip(close, sma):
        if s < c and in_position == False:
            buy.append(c)
            in_position = True
        else:
            buy.append(0)

        if s > c and in_position == True:
            sell.append(c)
            in_position = False
        else:
            sell.append(0)


def signal_RSI_and_CMO(close):
    in_position = False
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30

    # for testing
    close = numpy.array(tesla_close)

    rsi = talib.RSI(close, RSI_PERIOD)

    cmo = talib.CMO(close)

    buy = []
    sell = []
    cmo_said_no = []
    for r, c, cm in zip(rsi, close, cmo):
        if r < RSI_OVERSOLD and in_position == False:

            buy.append(c)
            in_position = True

        else:
            buy.append(0)

        if r > RSI_OVERBOUGHT and cm < -50 and in_position == True:
            sell.append(c)
            in_position = False
        else:
            sell.append(0)


# %%
def signal_CMO(data):

    close = np.array(data["Close"])
    high = np.array(data["High"])
    open = np.array(data["Open"])
    low = np.array(data["Low"])

    in_position = False
    RSI_PERIOD = 14

    # for testing
    close = np.array(close)

    rsi = ta.RSI(close, RSI_PERIOD)

    cmo = ta.CMO(close,  timeperiod=4)

    buy = []
    sell = []
    cmo_said_no = []
    for r, c, cm in zip(rsi, close, cmo):
        if cm > 20 and in_position == False:

            buy.append(c)
            in_position = True

        else:
            buy.append(0)

        if cm < -55 and in_position == True:
            sell.append(c)
            in_position = False
        else:
            sell.append(0)

    df = pd.DataFrame()
    df["data"] = close

    sns.set(rc={'figure.figsize': (20, 5)})
    sns.scatterplot(data=sell, color="red", marker='X', s=30)
    sns.scatterplot(data=buy, color="green", marker='X', s=30)
    # sns.scatterplot(data=cmo_said_no, color="darkgreen", marker='v', s=140)
    sns.lineplot(data=df)
    sns.lineplot(data=cmo, color="purple")
    # sns.lineplot(data=slowd, color="orange")
    plt.show()

    gain = 0
    entire_price_change = df["data"].iloc[-1] - df["data"].iloc[0]

    buy_prices = [price for price in buy if price != 0]
    sell_prices = [price for price in sell if price != 0]

    if len(buy_prices) > len(sell_prices):
        buy_prices = buy_prices[:-1]

    for buy_price, sell_price in zip(buy_prices, sell_prices):
        gain += sell_price - buy_price

    print("den totale udvikling var: " + str(entire_price_change))
    print("modellens gevinst var: " + str(gain))


# data1 = pdr.get_data_yahoo("TSLA.MX", start="2012-01-01", end="2017-11-28")
# data2 = pdr.get_data_yahoo("PFE.MX", start="2012-01-01", end="2017-11-28")
data3 = pdr.get_data_yahoo("TLXTQ", start="2012-01-01", end="2017-11-28")
data4 = pdr.get_data_yahoo("BAFS-R.BK", start="2012-01-01", end="2017-11-28")
data5 = pdr.get_data_yahoo("6222.TWO", start="2012-01-01", end="2017-11-28")
data6 = pdr.get_data_yahoo("STGG", start="2012-01-01", end="2017-11-28")

signal_CMO(data1)
signal_CMO(data2)
signal_CMO(data3)
signal_CMO(data4)
signal_CMO(data5)
signal_CMO(data6)
# %%

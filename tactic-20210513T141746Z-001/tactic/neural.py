from identify_candlestick import recognize_candlestick
import sys
from keras.layers import Dropout
from keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import talib
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
from datetime import datetime
from os import listdir
import random
random.seed(42)

sys.path.append(
    r'C:\Users\benja\OneDrive\Skrivebord\CRYPTO\binance-master')
os.chdir(r"C:\Users\benja\OneDrive\Skrivebord\CRYPTO\binance-master")

# dataset = pd.read_csv(r"./data/BTC-USD.csv")
# dataset = pd.read_csv(r"./data/RELIANCE.NS.csv")
# dataset = dataset[['Open', 'High', 'Low', 'Close']]

files = listdir(r"./data/archive (1)many/")
for indx, file in enumerate(files):
    dataset = pd.DataFrame()
    dataset = pd.concat(
        [dataset, pd.read_csv(r"./data/archive (1)many/" + file)])
    dataset = dataset.reset_index()
    # dataset = pd.read_csv(r"./data/archive (1)many/coin_Bitcoin.csv")
    dataset = dataset[['Open', 'High', 'Low', 'Close']]

    # plt.plot(trade_dataset['Cumulative Strategy Returns'],
    #          color='g', label='Strategy Returns')

    # dataset.rename(columns={'open': 'Open', 'high': 'High',
    #                         'low': 'Low', 'close': 'Close', }, inplace=True)
    # dataset = dataset[:200]

    dataset = dataset.dropna()
    dataset['H-L'] = dataset['High'] - dataset['Low']
    dataset['O-C'] = dataset['Close'] - dataset['Open']
    dataset['3day MA'] = dataset['Close'].shift(1).rolling(window=3).mean()
    dataset['10day MA'] = dataset['Close'].shift(1).rolling(window=10).mean()
    dataset['30day MA'] = dataset['Close'].shift(1).rolling(window=30).mean()
    dataset['Std_dev'] = dataset['Close'].rolling(5).std()
    dataset['RSI'] = talib.RSI(dataset['Close'].values, timeperiod=9)
    dataset['Williams %R'] = talib.WILLR(
        dataset['High'].values, dataset['Low'].values, dataset['Close'].values, 7)

    # Ekstra
    dataset['Cmo'] = talib.CMO(dataset['Close'].values,  timeperiod=4)
    dataset["ADX"] = talib.ADX(dataset['High'].values,
                               dataset['Low'].values, dataset['Close'].values)
    dataset["ADXR"] = talib.ADXR(
        dataset['High'].values, dataset['Low'].values, dataset['Close'].values)
    dataset["APO"] = talib.APO(dataset['Close'].values)
    # dataset["AROON"] = talib.AROON(dataset['Close'].values)
    # dataset["AROONOSC"] = talib.AROONOSC(dataset['High'].values, dataset['Low'].values, dataset['Close'].values)
    dataset["BOP"] = talib.BOP(dataset['Open'].values, dataset['High'].values,
                               dataset['Low'].values, dataset['Close'].values)
    dataset["CCI"] = talib.CCI(dataset['High'].values,
                               dataset['Low'].values, dataset['Close'].values)
    dataset["CMO"] = talib.CMO(dataset['Close'].values)
    dataset["DX"] = talib.DX(dataset['High'].values,
                             dataset['Low'].values, dataset['Close'].values)
    # dataset["MACDFIX"] = talib.MACDFIX(dataset['High'].values, dataset['Low'].values, dataset['Close'].values)
    dataset["MFI"] = talib.MFI(dataset['Open'].values, dataset['High'].values,
                               dataset['Low'].values, dataset['Close'].values)
    dataset["MINUS_DI"] = talib.MINUS_DI(
        dataset['High'].values, dataset['Low'].values, dataset['Close'].values)
    dataset["MOM"] = talib.MOM(dataset['Close'].values)
    dataset["PLUS_DI"] = talib.PLUS_DI(
        dataset['High'].values, dataset['Low'].values, dataset['Close'].values)
    # dataset["PLUS_DM"] = talib.PLUS_DM(dataset['Close'].values)
    dataset["PPO"] = talib.PPO(dataset['Close'].values)
    dataset["ROCP"] = talib.ROCP(dataset['Close'].values)
    dataset["ROCR"] = talib.ROCR(dataset['Close'].values)
    # dataset["STOCH"] = talib.STOCH(dataset['High'].values, dataset['Low'].values, dataset['Close'].values)
    dataset["TRIX"] = talib.TRIX(dataset['Close'].values)
    dataset["ULTOSC"] = talib.ULTOSC(
        dataset['High'].values, dataset['Low'].values, dataset['Close'].values)

    dataset = recognize_candlestick(dataset)
    dataset = dataset.drop(columns=["candlestick_match_count"])
    dataset = dataset.drop(columns=["candlestick_pattern"])
    # dataset = dataset.drop(columns=["candlestick_match_sum"])

    # dataset['candlestick_pattern'] = dataset['candlestick_pattern'].apply(
    #     lambda x: x[-4:])

    # def pattern_reg(dirction, matches):
    #     if dirction == "Bear":
    #         return -matches
    #     return matches

    # dataset["candlestick_pattern"] = dataset.apply(lambda x: pattern_reg(
    #     x["candlestick_pattern"], x["candlestick_match_count"]), axis=1)

    # y
    dataset['Price_Rise'] = np.where(
        dataset['Close'].shift(-1) > dataset['Close'], 1, 0)

    dataset['Price_Rise_labe'] = np.where(
        dataset['Close'].shift(-1) > dataset['Close'], [1, 0], [0, 1])
    # dataset['Price_Rise'] = dataset['Close'].shift(-1) - dataset['Close']

    # dataset = dataset.drop(columns=["Open", "High", "Low", "Close"])
    dataset = dataset.dropna()

    X = dataset.iloc[:, :-2]
    y = dataset.iloc[:, -1]

    split = int(len(dataset)*0.7)
    X_train, X_test, y_train, y_test = X[:
                                         split], X[split:], y[:split], y[split:]

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    # print(X_test, type(X_test[1][1]))
    if indx == 0:
        classifier = Sequential()
        classifier.add(Dense(units=128, kernel_initializer='uniform',
                             activation='relu', input_dim=X.shape[1]))
        classifier.add(
            Dense(units=128, kernel_initializer='uniform', activation='relu'))

        classifier.add(
            Dense(units=2, kernel_initializer='uniform', activation='sigmoid'))
        classifier.compile(
            optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    classifier.fit(X_train, y_train, batch_size=20, epochs=70)

    y_pred = classifier.predict(X_test)
    pred = []
    for x in y_pred:
        pred.append(x[0] > x[1])

    y_pred = np.array(pred)

    # print("y_pred: ",y_pred)

    dataset['y_pred'] = np.NaN
    dataset.iloc[(len(dataset) - len(y_pred)):, -1:] = y_pred
    trade_dataset = dataset.dropna()

    trade_dataset['Tomorrows Returns'] = 0.
    trade_dataset['Tomorrows Returns'] = trade_dataset['Close'] - \
        trade_dataset['Close'].shift(1)
    trade_dataset['Tomorrows Returns'] = trade_dataset['Tomorrows Returns'].shift(
        -1)

    trade_dataset['Strategy Returns'] = 0.
    trade_dataset['Strategy Returns'] = np.where(
        trade_dataset['y_pred'] == True, trade_dataset['Tomorrows Returns'], 0)

    trade_dataset['Cumulative Market Returns'] = np.cumsum(
        trade_dataset['Tomorrows Returns'])
    trade_dataset['Cumulative Strategy Returns'] = np.cumsum(
        trade_dataset['Strategy Returns'])
    trade_dataset["buy"] = np.where((trade_dataset['y_pred'] == True) &
                                    (trade_dataset['y_pred'].shift(1) == False), 1, 0)

    trade_dataset["buy_spot"] = np.where(
        (trade_dataset["buy"] == 1), trade_dataset["Cumulative Market Returns"], 0)

    trade_dataset["sell"] = np.where((trade_dataset['y_pred'] == False) &
                                     (trade_dataset['y_pred'].shift(1) == True), 1, 0)

    trade_dataset["sell_spot"] = np.where(
        (trade_dataset["sell"] == 1), trade_dataset["Cumulative Market Returns"], 0)

    plt.figure(figsize=(10, 5))
    plt.plot(trade_dataset['Cumulative Market Returns'],
             color='b', label='Market Returns')
    plt.plot(trade_dataset['Cumulative Strategy Returns'],
             color='g', label='Strategy Returns')

    # plt.plot(trade_dataset["buy_spot"], color='g')
    # plt.plot(trade_dataset["sell_spot"], color='r')
    plt.legend()
    plt.show()

    print("total market return: " +
          str(trade_dataset['Cumulative Market Returns'].iloc[-2]))
    print("total strategy return: " +
          str(trade_dataset['Cumulative Strategy Returns'].iloc[-2]))
    print("total antal køb: "+str(sum(trade_dataset["buy"])))
    print("total antal valgte dage: "+str(sum(trade_dataset["y_pred"])))
    print("total rigtige køb: " +
          str(len(trade_dataset[(trade_dataset["buy"] == 1) & (trade_dataset["Price_Rise"] == 1)])))
    print("total antal dage: "+str(len(trade_dataset)))

from app.backtest.IFR2Backtest import IFR2Backtest
from app.backtest.CrossAverageBacktest import CrossAverageBacktest
from app.database.Schemas import IFR2Schema, CrossAverageSchema, BackTestSchema
import pandas as pd
from backtesting import Backtest
from binance.spot import Spot as Client
import numpy as np
from datetime import date
import json


def getBacktest(robot):
    if isinstance(robot, IFR2Schema):
        df = getCandles(robot.symbol, robot.timeframe)
        bt = Backtest(df, IFR2Backtest, cash=100000,
                      commission=0, exclusive_orders=False)
        return bt.run().to_json()

    elif isinstance(robot, CrossAverageSchema):
        df = getCandles(robot.symbol, robot.timeframe)
        bt = Backtest(df, CrossAverageBacktest, cash=100000,
                      commission=0, exclusive_orders=False)
        return bt.run().to_json()


def generateStats():
    symbols = ['BTCUSDT']
    timeframes = ['1m']
    robots = [IFR2Backtest]
    backtests = []
    for timeframe in timeframes:
        for symbol in symbols:
            df = getCandles(symbol, timeframe)
            for robot in robots:
                bt = Backtest(df, robot, cash=100000,
                              commission=0, exclusive_orders=False)
                result = json.loads(bt.run().to_json())
                result.pop("_strategy")
                for key in result.keys():
                    key.remove(".")
                backtests.append(result)
    return backtests


def getCandles(symbol, timeframe):
    df = pd.DataFrame(columns=['Date', 'Open', 'High',
                      'Low', 'Close', 'Volume', 'Close_time'])
    spot_client = Client(base_url="https://testnet.binance.vision")
    candles = spot_client.klines(symbol, timeframe, limit=1000)
    opentime, lopen, lhigh, llow, lclose, lvol, closetime = [], [], [], [], [], [], []

    for candle in candles:
        opentime.append(candle[0])
        lopen.append(candle[1])
        lhigh.append(candle[2])
        llow.append(candle[3])
        lclose.append(candle[4])
        lvol.append(candle[5])
        closetime.append(candle[6])

    df['Date'] = opentime
    df['Open'] = np.array(lopen).astype(np.float)
    df['High'] = np.array(lhigh).astype(np.float)
    df['Low'] = np.array(llow).astype(np.float)
    df['Close'] = np.array(lclose).astype(np.float)
    df['Volume'] = np.array(lvol).astype(np.float)
    df['Close_time'] = closetime
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df.set_index('Date', inplace=True)
    return df

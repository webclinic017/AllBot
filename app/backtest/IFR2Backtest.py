from backtesting import Strategy
import ta


class IFR2Backtest(Strategy):
    periodRSI = 2
    periodMean = 5
    lower = 10
    upper = 90

    def init(self):
        self.RSI = self.I(ta.momentum.rsi, self.data.Close.s, self.periodRSI)
        self.SMA = self.I(ta.trend.sma_indicator, self.data.Close.s, self.periodMean)

    def next(self):
        price = self.data.Close[-2]
        rsi = self.RSI[-2]
        sma = self.SMA[-2]
        if not self.position:
            if rsi < self.lower:
                self.buy()
            # elif rsi > self.upper:
            #     self.sell()
        else:
            if self.position.is_long and (price > sma):
                self.position.close()
            # elif self.position.is_short and (price < sma):
            #     self.position.close()

from backtesting import Strategy


class IFRBacktest(Strategy):
    def init(self):
        pass

    def next(self):
        price = self.data.Close[-2]
        rsi = self.data.RSI[-2]
        sma = self.data.SMA[-2]
        if not self.position:
            if rsi < 10:
                self.buy()
            elif rsi > 90:
                self.sell()
        else:
            if self.position.is_long and (price > sma):
                self.position.close()
            elif self.position.is_short and (price < sma):
                self.position.close()

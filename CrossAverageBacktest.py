from backtesting import Strategy
import ta


class CrossAverageBacktest(Strategy):
    fastPeriod = 5
    slowPeriod = 21
    name = 'CrossAverage'

    def init(self):
        self.mFast = self.I(ta.trend.sma_indicator, self.data.Close.s, self.fastPeriod)
        self.mSlow = self.I(ta.trend.sma_indicator, self.data.Close.s, self.slowPeriod)

    def next(self):
        mFastShift1 = self.mFast[-1]
        mSlowShift1 = self.mSlow[-1]

        mFastShift2 = self.mFast[-2]
        mSlowShift2 = self.mSlow[-2]

        if mFastShift1 > mSlowShift1 and (mFastShift2 < mSlowShift2):
            self.buy()
            # if self.position:
            #     self.position.close()
            # else:
            #     self.buy()
        elif mFastShift1 < mSlowShift1 and (mFastShift2 > mSlowShift2):
            if self.position:
                self.position.close()
            # else:
            #     self.sell()
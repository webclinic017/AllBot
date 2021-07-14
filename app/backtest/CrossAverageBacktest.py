from backtesting import Strategy


class CrossAverageBacktest(Strategy):
    def init(self):
        pass

    def next(self):
        mFastShift1 = self.data.mFast[-1]
        mSlowShift1 = self.data.mSlow[-1]

        mFastShift2 = self.data.mFast[-2]
        mSlowShift2 = self.data.mSlow[-2]

        if mFastShift1 > mSlowShift1 and (mFastShift2 < mSlowShift2):
            if self.position:
                self.position.close()
            self.buy()
        elif mFastShift1 < mSlowShift1 and (mFastShift2 > mSlowShift2):
            if self.position:
                self.position.close()
            self.sell()
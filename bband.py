import talib as ta
from n225 import N225

#BBand(ボリンジャーバンド) -> 売られすぎ買われ過ぎを判断
#判断基準は枠内に入っているか(正常)どうか(過度)
class BBAND:
    def __init__(self, start, end, price, period):
        self.start = start
        self.end = end
        self.price = price
        self.period = period
        n225 = N225(self.start, self.end)
        self.df = n225.getN225()
        self.df['upper'], self.df['middle'], self.df['lower'] = ta.BBANDS(self.price, timeperiod=self.period, nbdevup=2, nbdevdn=2, matype=0)

    def getBband(self):
        return self.df

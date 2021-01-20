import talib as ta
from n225 import N225

#MACD>0 -> 上昇トレンド
#MACD<0 -> 下降トレンド
class MACD:
    def __init__(self, start, end,  price):
        self.start = start
        self.end = end
        self.price = price
        n225 = N225(self.start, self.end)
        self.df = n225.getN225()
        self.df['macd'], self.df['macdsignal'], self.df['macdhist'] = ta.MACD(self.price, fastperiod=12, slowperiod=26, signalperiod=9)

    def getMacd(self):
        return self.df

    def getMacdHist(self):
        fill = self.df['macdhist'].fillna(0)
        return fill
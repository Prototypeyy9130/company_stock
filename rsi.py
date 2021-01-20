import talib as ta
from n225 import N225

#RSI < 20~30% -> 売られすぎ(逆張りの買い判断)
#RSI > 70~80% -> 買われすぎ(逆張りの売り判断)
class RSI:
    def __init__(self, start, end, price, period):
        self.start = start
        self.end = end
        self.price = price
        self.period = period
        n225 = N225(self.start, self.end)
        self.df = n225.getN225()
        self.df['RSI'] = ta.RSI(self.price, timeperiod=self.period)

    def getRsi(self):
        return self.df['RSI']
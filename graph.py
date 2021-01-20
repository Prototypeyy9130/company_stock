import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')
from datetime import datetime as dt
from macd import MACD
from rsi import RSI
from bband import BBAND

#単純SMAのグラフ
class Graph:
    def __init__(self, date, price):
        self.date = date
        self.price = price

    #グラフの雛形
    def base(self):
        plt.plot(self.date, self.price, label='Nikkei225', color='#99b898')

    #グラフの表示
    def show(self):
        plt.title('N225', color='blue', backgroundcolor='white', size=40, loc='center')
        plt.xlabel('date', color='black', size=30)
        plt.ylabel('price', color='black', size=30)
        plt.legend()

#5,25,50SMAを追加したグラフ
class Span(Graph):
    def __init__(self, date, price, sma01, sma02, sma03):
        super().__init__(date, price)
        self.sma01 = sma01
        self.sma02 = sma02
        self.sma03 = sma03

    #5,25,50SMAを追加
    def base(self):
        super().base()
        plt.plot(self.date, self.sma01, label='5SMA', color='#e84a5f')
        plt.plot(self.date, self.sma02, label='25SMA', color='#ff847c')
        plt.plot(self.date, self.sma03, label='50SMA', color='#feceab')

#個別銘柄ver.(ラベル変更)
class GraphB(Graph):
    def __init__(self, date, price, label):
        super().__init__(date, price)
        self.label = label

    #ラベル変更
    def changeLabel(self):    
        plt.plot(self.date, self.price, label=self.label, color='#99b898')
    
    def show(self):
        super().show()

class SpanB(GraphB):
    def __init__(self, date, price, label, sma01, sma02, sma03):
        super().__init__(date, price, label)
        self.sma01 = sma01
        self.sma02 = sma02
        self.sma03 = sma03

    def changeLabel(self):
        super().changeLabel()
        plt.plot(self.date, self.sma01, label='5SMA', color='#e84a5f')
        plt.plot(self.date, self.sma02, label='25SMA', color='#ff847c')
        plt.plot(self.date, self.sma03, label='50SMA', color='#feceab')


#出来高のグラフ
class Volume:
    def __init__(self, date, volume):
        self.date = date
        self.volume = volume

    #グラフの雛形
    def show(self):
        plt.bar(self.date, self.volume, label='Volume', color='grey')
        plt.legend()

#MACDの折れ線塗りつぶしグラフ
class GraphM:
    def __init__(self, start, end, date, price):
        self.start = start
        self.end = end
        self.date = date
        self.price = price
        df = MACD(self.start, self.end, self.price)
        self.df = df.getMacdHist()

    def getHist(self):
        dt_start = dt.strptime(self.start, '%Y-%m-%d')
        dt_end = dt.strptime(self.end, '%Y-%m-%d')
        plt.fill_between(self.date, self.df, color='grey', alpha=0.5, label='MACD_hist')
        plt.hlines(0, dt_start, dt_end, 'grey', linestyles='dashed')
        plt.legend()

#RSIの折れ線グラフ
class GraphR:
    def __init__(self, start, end, date, price, period):
        self.start = start
        self.end = end
        self.date = date
        self.price = price
        self.period = period
        df = RSI(self.start, self.end, self.price, self.period)
        self.df = df.getRsi()

    def show(self):
        dt_start = dt.strptime(self.start, '%Y-%m-%d')
        dt_end = dt.strptime(self.end, '%Y-%m-%d')
        plt.plot(self.date, self.df, label='RSI', color='grey')
        plt.ylim(0, 100)
        plt.hlines([30, 50, 70], dt_start, dt_end, 'grey', linestyles='dashed')
        plt.legend()

#ボリンジャーバンドの表示
class BAND(Graph):
    def __init__(self, date, price, start, end, period):
        super().__init__(date, price)
        self.start = start
        self.end = end
        self.period = period
        df = BBAND(self.start, self.end, self.price, self.period)
        self.df = df.getBband()

    def base(self):
        super().base()
        plt.fill_between(self.date, self.df['upper'], self.df['lower'], color='grey', alpha=0.3)
        plt.legend()

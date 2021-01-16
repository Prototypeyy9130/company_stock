import matplotlib.pyplot as plt

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
        plt.title('N225', color='red', backgroundcolor='white', size=40, loc='center')
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



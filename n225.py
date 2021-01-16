from pandas_datareader import data

class N225:
    #コンストラクタ
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.df = data.DataReader('^N225', 'yahoo', self.start, self.end)

    #N225の取得
    def getN225(self):
        return self.df

    #indexの取得
    def getDate(self):
        return self.df.index

    #Adj Closeの取得  
    def getPrice(self):  
        return self.df['Adj Close']

    #Volumeの取得
    def getVolume(self):
        return self.df['Volume']


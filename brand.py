from pandas_datareader import data

class Brand:
    def __init__(self,start, end, company_code):
        self.start = start
        self.end = end
        self.company_code = company_code+'.JP'
        self.df = data.DataReader(self.company_code, 'stooq', self.start, self.end)

    #個別銘柄のコード
    def code(self):
        return self.company_code

    #個別銘柄のデータ取得
    def getPrice(self):
        return self.df

    #株価の表示
    def showPrice(self):    
        print("指定された個別銘柄の株価を表示します。\n")
        print(self.df)


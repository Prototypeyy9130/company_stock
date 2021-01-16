from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import n225
import graph
import brand
#行の省略を解除
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

start = input('いつからのデータを取得しますか？(YY-MM-DD):')
if start == "sample":
    start = '2021-01-07'
    end = '2021-01-14'
elif start == "sample2":
    start = '2020-01-14'
    end = '2021-01-14' 
else:
    end = input('いつまでのデータを取得しますか？(YY-MM-DD):')

select = n225.N225(start, end)
date = select.getDate()
price = select.getPrice()
volume = select.getVolume()
print('index:\n{0}'.format(date))

print("\nテーマとキーワード\n")
list = dict({'N225の折れ線グラフ':1,
             '折れ線グラフのオプション':2,
             '移動平均の作成':3,
             '出来高の棒グラフ':4,
             '出来高＋移動平均':5,
             '個別銘柄の株価':6,
             '出来高＋移動平均(個別銘柄ver.)':7
             })
for k,v in list.items():
    print("{0}:{1}".format(k, v))
    print()

while True:
    kw = int(input("確認する動作のキーワードを入力してください。："))

    if kw == 1:
        plt.plot(date, price)
        plt.show()
        break

    elif kw == 2:
        graph = graph.Graph(date, price)
        plt.figure(figsize=(30, 10))
        graph.base()
        graph.show()
        plt.show()
        break

    elif kw == 3:
        span01 = 5
        span02 = 25
        span03 = 50

        add_span = select.getN225()
        add_span['sma01'] = price.rolling(window=span01).mean()
        sma01 = add_span['sma01']
        add_span['sma02'] = price.rolling(window=span02).mean()
        sma02 = add_span['sma02']
        add_span['sma03'] = price.rolling(window=span03).mean()
        sma03 = add_span['sma03']

        print(add_span.head(100))

        graph = graph.Span(date, price, sma01, sma02, sma03)
        plt.figure(figsize=(30, 10))
        graph.base()
        graph.show()
        plt.show()
        break

    elif kw ==4:
        graph = graph.Volume(date, volume)
        plt.figure(figsize=(30, 15))
        graph.show()
        plt.show()
        break

    elif kw == 5:
        plt.figure(figsize=(30, 15))

        plt.subplot(2, 1, 1)
        span01 = 5
        span02 = 25
        span03 = 50
        add_span = select.getN225()
        add_span['sma01'] = price.rolling(window=span01).mean()
        sma01 = add_span['sma01']
        add_span['sma02'] = price.rolling(window=span02).mean()
        sma02 = add_span['sma02']
        add_span['sma03'] = price.rolling(window=span03).mean()
        sma03 = add_span['sma03']
        graph1 = graph.Span(date, price, sma01, sma02, sma03)
        graph1.base()
        plt.legend()

        plt.subplot(2, 1, 2)
        graph2 = graph.Volume(date, volume)
        graph2.show()

        plt.show()
        break

    elif kw == 6:
        while True:
            code = input("株価を取得したい銘柄のコードを入力してください。(ipxで東京証券取引所のHPを開けます。):")
            if code == "ipx":
                webbrowser.open('https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/stock_search')
            else:
                brand = brand.Brand(start, end, code)
                brand.showPrice()
                break
        break

    elif kw == 7:
        while True:
            code = input("株価を取得したい銘柄のコードを入力してください。(ipxで東京証券取引所のHPを開けます。):")
            if code == "ipx":
                webbrowser.open('https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/stock_search')
            else:
                brand = brand.Brand(start, end, code)
                label = brand.code()

                plt.figure(figsize=(30, 15))

                plt.subplot(2, 1, 1)
                span01 = 5
                span02 = 25
                span03 = 50
                add_span = brand.getPrice()
                add_span['sma01'] = price.rolling(window=span01).mean()
                sma01 = add_span['sma01']
                add_span['sma02'] = price.rolling(window=span02).mean()
                sma02 = add_span['sma02']
                add_span['sma03'] = price.rolling(window=span03).mean()
                sma03 = add_span['sma03']
                graph1 = graph.SpanB(date, price, label, sma01, sma02, sma03)
                graph1.changeLabel()
                plt.legend()

                plt.subplot(2, 1, 2)
                graph2 = graph.Volume(date, volume)
                graph2.show()

                plt.show()
                break
        break
        
    else:
        print('\nキーワードが正しく入力されませんでした。もう一度入力してください。\n')

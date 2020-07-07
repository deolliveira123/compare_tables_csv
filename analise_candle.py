import yfinance as yf
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick2_ohlc
import matplotlib.dates as mdt
import datetime as dt

start = '2020-05-13'
end = '2020-07-07'

acao = yf.download('SHOW3.SA', start, end)
acao.reset_index(inplace=True)


fig, ax = plt.subplots()
plt.title('SHOW3')
plt.xlabel('')
plt.ylabel('')

candlestick2_ohlc(ax, acao.Open, acao.High, acao.Low, acao.Close, width=1, colorup='g')
plt.savefig('meugrafico.png')
plt.show()


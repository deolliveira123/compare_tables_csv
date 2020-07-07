import pandas_datareader as pdr
import pandas as pd
import datetime as dt

Acao_1 = 'PETR4.SA'
Acao_2 = 'COGN3.SA'
Acao_3 = 'CIEL3.SA'
Acao_4 = 'SHOW3.SA'

start = '2019-01-01'
end = dt.datetime.today()

price = pd.DataFrame()

Tickers = [Acao_1, Acao_2, Acao_3, Acao_4]

for i in Tickers:
    price[i] = pdr.DataReader(i, 'yahoo', start, end)['Adj Close']

log_returns = price
print('############## PREÇO MÉDIO #########################')
print(log_returns.mean())
print('############### DESVIO PADRÃO ######################')
print(log_returns.std())
print('################ CORRELAÇÃO #########################')
print(log_returns.corr())
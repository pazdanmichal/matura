import numpy
import requests
import pandas as pd
import matplotlib.pyplot as plt
def get_crypto_price(symbol, exchange, start_date = None):
    api_key = 'YOUR API KEY'
    api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={exchange}&apikey={api_key}'
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
    df = df.rename(columns = {'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low', '4a. close (USD)': 'close', '5. volume': 'volume'})
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis = 1)
    if start_date:
        df = df[df.index >= start_date]
    return df

btc = get_crypto_price(symbol = 'BTC', exchange = 'USD', start_date = '2020-01-01')
wartosci = (btc["open"])
x = []
y = []
for i in range (0, len(btc)):
    x.append(i)
    y.append(wartosci[i])
plt.style.use('dark_background')

plt.plot(x, y)



num = 100
ret = numpy.polyfit(x,y,num)

listY = []
for i in range (0, len(wartosci)):
    valNow = 0
    for j in range (0, num+1):
        valNow += ret[j]*i**(num-j)
    listY.append(valNow)
plt.plot(x, listY)
plt.show()
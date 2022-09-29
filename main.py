from kucoin.client import Market, User
import pandas as pd
import matplotlib.pyplot as plt
import time

from dotenv import load_dotenv
import os

load_dotenv('.env')

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
api_passphrase = os.environ.get("API_PASSPHRASE")
account_id = os.environ.get("ACCOUNT_ID")

client = Market(url='https://api.kucoin.com')

user = User(api_key, api_secret, api_passphrase)
# print(user.get_account_list('USDT'))

def getminutedata(symbol, interval, lookback):
    currenttime = time.time()
    starttime = currenttime - (float(lookback) * 60)
    frame = pd.DataFrame(client.get_kline(symbol, interval, startAt=int(starttime)))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'Close', 'High', 'Low', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

# print(getminutedata('BTC-USDT','1min', '30'))

# test = getminutedata('BTC-USDT','1min', '30')

# plt.plot(test.Open)
# plt.show()

#buy if asset fell by more then 0.2% within the last 30 min
#sell of asset rises by more then 0.15% or falls futher by 0.15%

def strategytest(symbol, qty, entered=False):
    df = getminutedata(symbol, '1min', '30')
    cumulret = (df.Open.pct_change() +1).cumprod() - 1
    if not entered:
        if cumulret[-1] < -0.002:
            order = df.Time
            print(order)
            entered = True
        else:
            print('No trade has been executed')
    if entered:
        while True:
            df = getminutedata(symbol, '1min', '30')
            sincebuy = df.loc[df.index > pd.to_datetime(order, unit='ms')]
            if len(sincebuy) > 0:
                sincebuyret = (sincebuy.Open.pct_change() +1).cumprod() - 1
                if sincebuyret[-1] > 0.0015 or sincebuyret[-1] < -0.0015:
                    order = df.Time
                    print(order)
                    break

# strategytest('BTC-USDT', 0.001)

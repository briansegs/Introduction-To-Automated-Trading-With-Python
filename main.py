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

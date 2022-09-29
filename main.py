from kucoin.client import Market
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv('.env')

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
api_passphrase = os.environ.get("API_PASSPHRASE")
account_id = os.environ.get("ACCOUNT_ID")

client = Market(url='https://api.kucoin.com')

klines = client.get_kline('BTC-USDT','1min')

print(klines)
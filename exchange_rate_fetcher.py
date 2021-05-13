import requests
import os

KEY = os.environ.get("KEY")
URL = "https://rest.coinapi.io"
headers = {
    "X-CoinAPI-Key": KEY
}


def get_exchange_rate(ticker, currency, time=""):
    endpoint = f"/v1/exchangerate/{ticker}/{currency}?time={time}"
    response = requests.get(url=URL+endpoint, headers=headers)
    rate = response.json()["rate"]
    return rate

import ccxt
import os

BIN_KEY = os.environ.get("BIN_KEY")
BIN_SECRET = os.environ.get("BIN_SECRET")


exchange_auth = {
        "apiKey": BIN_KEY,
        "secret": BIN_SECRET
    }

exchange = ccxt.binance(exchange_auth)

balance = exchange.fetch_balance()["total"]

wallet = {key: value for key, value in balance.items() if value != 0.0}


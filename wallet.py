import ccxt
import time
yesterday = round(time.time() - 86400)*1000


class Wallet:
    def __init__(self, bin_key, bin_secret, currency):
        self.exchange_auth = {
            "apiKey": bin_key,
            "secret": bin_secret
          }
        self.timeframe = ""
        self.exchange = ccxt.binance(self.exchange_auth)
        # Which coins are in the wallet, and data to be processed later
        self.balance = self.exchange.fetch_balance()["total"]
        self.coins = {key: value for key, value in self.balance.items() if value != 0.0}
        self.wallet_data = {coin: self.fetch_data(coin, "USDT") for (coin, value) in self.coins.items()}
        # Last close and previous close for each coin
        self.close_amounts = [(self.calculate_value(coin, "now"))*self.coins[coin] for coin in self.coins]
        self.previous_close_amounts = [(self.calculate_value(coin, "yesterday"))*self.coins[coin] for coin in self.coins]
        # Exchange rate for the chosen currency and total amounts for last close and previous close in that currency
        self.currency_exchange_data = self.fetch_data(currency, "USDT")
        self.total_close = sum(self.close_amounts)*(1/self.currency_exchange_data["now"])
        self.total_previous_close = sum(self.previous_close_amounts)*(1/self.currency_exchange_data["yesterday"])
        # Difference and Difference% between last close and previous close
        self.diff = self.total_close - self.total_previous_close
        self.diff_percent = round((self.diff / float(self.total_close)) * 100)

    def fetch_data(self, ticker, base):
        """fetch data on a coin/base pair. Returns current value and the value 24 hours prior"""
        data = self.exchange.fetch_ohlcv(f"{ticker}/{base}", timeframe="1d", since=yesterday)
        coin_data = {"now": data[0][4], "yesterday": data[0][1]}
        return coin_data

    def calculate_value(self, coin, date):
        """get the value at last close (use "close") or previous close (use "previousClose") for a coin"""
        value = self.wallet_data[coin][date]
        return value


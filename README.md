# WalletUpdates

This python program will take a wallet of cryptocurrencies in assets.py and send an email update on its performance to a specified recipient.

You will need your own API key from https://www.coinapi.io/ (it's free) and declare it in exchange_rate_fetcher.py.

You will also need to declare an smpt server, sender email and password, and recipient email in mail_server.py.

You can also change your preferred currency in main.py

In the future I would like to fetch a wallet directly from Binance rather than having to hardcode it here, have not looked at their API yet.
# WalletUpdates

This python program will take a wallet of cryptocurrencies in assets.py and send an email update on its performance to a specified recipient.

Things you will need to set up, either as environmental variables or to replace the os.envorin... part in the relevant file

your own API key from https://www.coinapi.io/ (it's free) to declare in exhange_rate_fetcher.py

Your own API key and secret from Binance in assets.py. Note that you should be able to also edit the exchange and use another, however you may need to check the ccxt manual (https://github.com/ccxt/ccxt/wiki/Manual) to see whether the authentication process is different

Your own details for smtp server, sender email (and password) and receiver email in mail_server.py

You can also change the currency variable in main.py in case you want the daily update in EUR, USD or whatever else you normally use


# WalletUpdates

This python program will take a wallet of cryptocurrencies in assets.py and send an email update on its performance to a specified recipient.

Things you will need to set up to make this work:

your own API key from https://www.coinapi.io/ (it's free)

Your own API key and secret from Binance 

Your own details for smtp server, sender email (and password) and receiver email

[optional] the fiat currency you want to get your results into (default is GBP)

All of these variables are in main.py declared as environmental variables, except for the currency that is just a string. You can either declare your own environmental variables or declare them all as strings, as you prefer.

# WalletUpdates

This python program will connect to your Binance wallet and send an email update on its recent performance to a specified recipient.

Things you will need to set up to make this work:

Your own API key and secret from Binance 

Your own details for smtp server, sender email (and password) and receiver email

[optional] the fiat currency you want to get your results into (default is GBP)

All of these variables are in main.py declared as environmental variables, except for the currency that is just a string. You can either declare your own environmental variables or declare them all as strings, as you prefer.

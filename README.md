# WalletUpdates

This python program will connect to your Binance wallet and send an email update on its recent performance to a specified recipient.

Note: I wrote this script as a challenge to myself to work with a public API and only put a few pounds on a few shitcoins for fun (I since retrieved that amount). Whether you should invest in crypto or not is up to you, I won't endorse it.

Things you will need to set up to make this work:

Your own API key and secret from Binance 

Your own details for smtp server, sender email (and password) and receiver email

Note that if you wish to use a gmail to send the email you need to enable less secure apps access for that Google profile. More info here: https://support.google.com/accounts/answer/6010255 (You may want to create a dummy gmail for this purpose)

[optional] the fiat currency you want to get your results into (default is GBP)

All of these variables are in main.py declared as environmental variables, except for the currency that is just a string. You can either declare your own environmental variables or declare them all as strings, as you prefer.


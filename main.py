from wallet import Wallet
from mail_server import MailServer
import os


# currency for calculating the total value of the wallet, also displayed in the update email
CURRENCY = "GBP"

# Binance API details, either add yours as environmental variables or declare them as strings
BIN_KEY = os.environ.get("BIN_KEY")
BIN_SECRET = os.environ.get("BIN_SECRET")

# details of the email you are sending from, its password, its smtp server and the email you are sending to. Either
# add yours as environmental variables or declare them as strings
SENDER = os.environ.get("SENDER")
RECIPIENT = os.environ.get("RECIPIENT")
PASSWORD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")

# Initialise classes
wallet = Wallet(bin_key=BIN_KEY, bin_secret=BIN_SECRET, currency=CURRENCY)
mail_server = MailServer(sender=SENDER, recipient=RECIPIENT, password=PASSWORD, server=SERVER)

# switch between emoticons as appropriate and add a + to a positive percentage
emoticon = ":("
if wallet.diff_percent > 0.0:
    emoticon = ":)"
    wallet.diff_percent = f"+{wallet.diff_percent}"

# Send the email with the values taken from the wallet
mail_server.send_mail(value_today=round(wallet.total_close, 2), value_yesterday=round(wallet.total_previous_close, 2),
                      diff=wallet.diff_percent, currency=CURRENCY, emoticon=emoticon)

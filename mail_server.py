import smtplib
import os

SENDER = os.environ.get("SENDER")
RECIPIENT = os.environ.get("RECIPIENT")
PASSWORD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")



def send_mail(today_amount, yesterday_amount, diff, currency):
    with smtplib.SMTP(SERVER) as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECIPIENT,
            msg=f"Subject:Daily Portfolio update: {diff}%\n\nYour portfolio is worth {today_amount} {currency} today! "
                f"It was {yesterday_amount} {currency} yesterday"
        )

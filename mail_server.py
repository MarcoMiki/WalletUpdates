import smtplib


class MailServer:
    def __init__(self, sender, recipient, password, server):
        self.sender = sender
        self.recipient = recipient
        self.password = password
        self.server = server

    def send_mail(self, value_today, value_yesterday, diff, currency, emoticon):
        with smtplib.SMTP(self.server) as connection:
            connection.starttls()
            connection.login(self.sender, self.password)
            connection.sendmail(
                from_addr=self.sender,
                to_addrs=self.recipient,
                msg=f"Subject:Daily Portfolio update: {diff}%\n\nYour portfolio is worth {value_today} {currency} "
                    f"today {emoticon} it was {value_yesterday} {currency} yesterday. "
            )

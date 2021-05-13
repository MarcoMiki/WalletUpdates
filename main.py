from exchange_rate_fetcher import get_exchange_rate
from assets import wallet
from mail_server import send_mail
from datetime import datetime, timedelta

CURRENCY = "GBP"

yesterday = datetime.strftime((datetime.now() - timedelta(1)), '%Y-%m-%d')
today_values = []
yesterday_values = []

for asset in wallet:
    today_rate = get_exchange_rate(ticker=asset, currency=CURRENCY)
    yesterday_rate = get_exchange_rate(ticker=asset, currency=CURRENCY, time=yesterday)
    today_value = float(wallet[asset]) * float(today_rate)
    yesterday_value = float(wallet[asset]) * float(yesterday_rate)
    yesterday_values.append(yesterday_value)
    today_values.append(today_value)

today_total = sum(today_values)
yesterday_total = sum(yesterday_values)
diff = today_total - yesterday_total
diff_percent = round((diff / float(today_total)) * 100)
if diff_percent > 0:
    diff_percent = f"+{diff_percent}"

send_mail(today_amount=round(today_total, 2), yesterday_amount=round(yesterday_total, 2), diff=diff_percent,
          currency=CURRENCY)

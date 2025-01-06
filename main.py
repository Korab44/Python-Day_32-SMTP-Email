import smtplib
import datetime as dt
import random

my_email = "korabmtest@gmail.com"
password = "htjgwqutatyiknog"

now = dt.datetime.now()
current_day_week = now.weekday()
if current_day_week == 0:
    with open("quotes.txt") as data:
        text = data.readlines()
        quote = random.choice(text)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs="korab.morina444@gmail.com",
                msg=f"Subject:Motivation quote\n\n{quote}")





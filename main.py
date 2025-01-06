import smtplib

my_email = "korabmtest@gmail.com"
password = "htjgwqutatyiknog"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="korab.morina444@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email.")

import smtplib
import datetime as dt
import random

my_email = "bijay765@gmail.com"
password = "rbzhbtpoqldsjcuh"
target_email = "765crimson@gmail.com"

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 3:

    with open("quotes.txt") as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #ENCRYPTS CONNECTION
        connection.login(user=my_email, password= password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=f"Subject:Monday Motivator\n\n{quote}"
        )

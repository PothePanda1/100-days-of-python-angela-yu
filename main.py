import smtplib

my_email = "bijay765@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()


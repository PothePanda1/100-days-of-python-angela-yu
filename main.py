import smtplib

my_email = "bijay765@gmail.com"
password = "placeholder"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #ENCRYPTS CONNECTION
connection.login(user=my_email, password= password)
connection.sendmail(from_addr=my_email, to_addrs="765crimson@gmail.com", msg="Hello")
connection.close()
ss
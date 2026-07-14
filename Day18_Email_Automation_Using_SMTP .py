'''
SMTP module
Email Message
Password: busw phda ffbe szgc

import smtplib
import ssl
from email.message import EmailMessage
sender_email = "meenav1143@gmail.com"
password = "buswphdaffbeszgc"

receiver_email = "viyyapumeenakshi2004@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Welcome Mail"
message.set_content("Welcome to the Codegnan")

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context = context)
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message)


import smtplib
import ssl
from email.message import EmailMessage
sender_email = "meenav1143@gmail.com"
password = "buswphdaffbeszgc"

receiver_email = "viyyapumeenakshi2004@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Welcome Mail"
message.set_content("Welcome to the Codegnan")

#context = ssl.create_default_context()
try:
    smtp = smtplib.SMTP("smtp.gmail.com", port = 587) #as smtp:
    #smtp.ehlo()
    smtp.starttls()
    #smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message)
    print("Email sent successfully")
except Exception as e:
    print("Error: ", e)
finally:
    smtp.quit()


import smtplib
import ssl
from email.message import EmailMessage
sender_email = "meenav1143@gmail.com"
password = "buswphdaffbeszgc"

receiver_email = "viyyapumeenakshi2004@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Welcome Mail"
message.set_content("Good Morning Meenakshi Viyyapu \nI hope you are doing well.\nJust wanted to wish you a fantastic day ahead.\nMay your day be filled with positivity, productivity, and happiness.\nKeep believing in yourself and continue working towards your goals. Have a wonderful day.\nBest Wishes,\nMeenakshi Yadav")

#context = ssl.create_default_context()
try:
    smtp = smtplib.SMTP("smtp.gmail.com", port = 587) #as smtp:
    #smtp.ehlo()
    smtp.starttls()
    #smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message)
    print("Email sent successfully")
except Exception as e:
    print("Error: ", e)
finally:
    smtp.quit()
'''




import smtplib
import ssl
from email.message import EmailMessage
sender_email = "meenav1143@gmail.com"
password = "buswphdaffbeszgc"

receiver_email = "viyyapumeenakshi2004@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Welcome Mail"
message.set_content(f"""
Hello Meenakshi!

Wecome to our Python Class

Regards,
Python Team
""")

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context = context)
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message)

    

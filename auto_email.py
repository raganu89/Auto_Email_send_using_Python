import os
import random
import smtplib


def email_send():
    user = input("Enter your name")
    email = input("Enter Email ID")
    message = (f"Dear {user}, Welcome to Python Programming")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("**********@gmail.com","**********")
    s.sendmail("recievermailid",email,message)
    print("Email Sent!")
    s.send
    
email_send()
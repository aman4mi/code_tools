import getpass
import smtplib
from email.message import EmailMessage

def get_email_info(sender_mail, passwd):
    receiver = "aman4.mi@gmail.com"
    subject = "Test Test Test"
    message = "Hello there, I am trying Please Favour me.."
    send_email(receiver, subject, message, sender_mail, passwd)
    

def send_email(receiver, subject, message, sender_mail, passwd):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login(sender_mail, passwd)
    email = EmailMessage()
    email['From'] = sender_mail
    email['To'] = receiver
    email['Subject'] = subject
    #print('pass ', passwd)
    email.set_content(message)
    server.send_message(email)
    print('Mail Sent ............')
    

try:
    sender_mail = input("Enter sender email: ")
    p = getpass.getpass("Password Dao: ")
    agree = input('Type y if agree: ')
    if agree == 'y' or agree == 'Y' :
         get_email_info(sender_mail, p)
except Exception as error:
	print('ERROR', error)         

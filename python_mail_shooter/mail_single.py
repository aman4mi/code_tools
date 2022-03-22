# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:07:11 2021

@author: Aman
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import smtplib

e=pd.read_excel("mail_add.xlsx")
emails=e['Emails'].values

from_addr = '171devteam@gmail.com'
to_addr = 'aman4.mi@gmail.com'
text = 'Hi Friend!!!'

username = '171devteam@gmail.com'
password = '171devteam_171'

msg = MIMEMultipart()

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Test Mail'
msg.attach(MIMEText(text))


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
print("All Email Sent Successfully.")   
import pandas as pd
import smtplib

username="171devteam@gmail.com"
passw=input("Enter your mail pass: ")

e=pd.read_excel("mail_add.xlsx")
emails=e['Emails'].values

print(emails)
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, passw)
subject = "Test Subject"

msg = pd.read_csv('mail_body.txt', delimiter = "\t")
#msg = "Hello World...i Am Mail Shooter...Bye."


body="subject: {}\n\n{}".format(subject, msg)
print(body)

for email in emails:
    server.sendmail(username, email, body)
server.quit()
    
print("All Email Sent Successfully.")   
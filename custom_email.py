import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass
import os


email_user = input("what is your gmail address? \n ")
email_password = getpass("what is the password for that email address? \n  ")
email_send = os.environ.get('EMAIL_SEND')
subject = 'Python daily CSV-Data'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, this csv file contains the updated/daily scraped python repos from github that are trending the most, containing the name, description, and code link, my website: http://167.71.157.4/'
msg.attach(MIMEText(body,'plain'))

filename='python_github.csv'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()

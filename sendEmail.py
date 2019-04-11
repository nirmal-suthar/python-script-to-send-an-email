import sys
import smtplib
from getpass import getpass
from email.mime.text import MIMEText


content="""\
Hi Kushagra!
"""
subject="Sent from my Python"

text_subtype = 'plain'
msg = MIMEText(content, text_subtype)
msg['Subject'] = subject
msg['From'] = sender

# input_string = input("Enter email address(es) seperated by comma: ")
# to_email_list = input_string.split(",")
# kushgpt99@gmail.com
to_email = "kushgpt99@gmail.com"
# to_email_list.append(to_email)

# from_email = "nirmalps@iitk.ac.in"



server = smtplib.SMTP("mmtp.iitk.ac.in",25)
server.ehlo()
server.starttls()


username = input("Enter your iitk username: ")
from_email = username+"@iitk.ac.in"
print("Sending email from "+from_email)
try:
    server.login(username,getpass("Please enter your iitk password: "))

    try:
        print('Sending email...')
        server.sendmail(from_email,to_email,msg)
        print('Email sent')
    finally:
        server.quit()
except:
    sys.exit( "username and passwork does not match ; %s" % "Autentication Failed" )

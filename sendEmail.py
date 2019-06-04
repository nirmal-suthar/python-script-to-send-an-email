import sys
import smtplib
from getpass import getpass
from email.mime.text import MIMEText

# sender mail details
username = input("Enter your iitk username: ")
from_email = username+"@iitk.ac.in"
sender = from_email

# content for the email
content="""\
Hello World
"""
subject="Sent from my Python"

text_subtype = 'plain'
msg = MIMEText(content, text_subtype)
msg['Subject'] = subject
msg['From'] = sender
msg = msg.as_string()

input_string = input("Enter email address(es) seperated by comma: ")
to_email_list = input_string.split(",")
# to_email_list.append(to_email)

# from_email = "nirmalps@iitk.ac.in"


#establishing connection
server = smtplib.SMTP("mmtp.iitk.ac.in",25)
server.ehlo()
server.starttls()
print("Sending email from "+from_email)

#attempting sendmail
try:
    server.login(username,getpass("Please enter your iitk password: "))

    try:
        print('Sending email...')
        server.sendmail(from_email,to_email_list,msg)
        print('Email sent')
    finally:
        server.quit()
except:
    sys.exit( "username and passwork does not match ; %s" % "Autentication Failed" )

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:35:32 2018

@author: james
"""
#it is better to run code line by line 
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("rahulsingh60verma@gmail.com", "yourpass") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("rahulsingh60verma@gmail.com", "mukulkirtiverma@gmail.com", message) 
  
# terminating the session 
s.quit() 




# Python code to illustrate Sending mail  
# to multiple users  
# from your Gmail account   
import smtplib 
  
# list of email_id to send the mail 
li = ["rahulsingh60verma@gmail.com", "mukulkirtiverma@gmail.com"] 
  
for i in range(len(li)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("rahulsingh60verma@gmail.com", "yourpass") 
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", li[i], message) 
    s.quit() 
    
    
    
    
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you"
 
# setup the parameters of the message
password = "yourpass"
msg['From'] = "rahulsingh60verma@gmail.com"
msg['To'] = "mukulkirtiverma@gmail.com" 
msg['Subject'] = "Subscription"
 
# add in the message body
msg.attach(MIMEText("hello", 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
 






#Create and Send an Email With an Attachment


import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase  
from email import encoders 
fromaddr = "rahulsingh60verma@gmail.com"
toaddr = "mukulkirtiverma@gmail.com"
# instance of MIMEMultipart 
msg = MIMEMultipart() 
 # storing the senders email address   
msg['From'] = fromaddr 
# storing the receivers email address  
msg['To'] = toaddr 
# storing the subject  
msg['Subject'] = "Subject of the Mail"
# string to store the body of the mail 
body = "Body_of_the_mail"
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
# open the file to be sent  
filename = "abcd.txt"
attachment = open("abcd.txt", "w+") 
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
# encode into base64 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment" ,filename="abcd.txt") 
"""Extended header setting.

        name is the header field to add.  keyword arguments can be used to set
        additional parameters for the header field, with underscores converted
        to dashes.  Normally the parameter will be added as key="value" unless
        value is None, in which case only the key will be added.  If a
        parameter value contains non-ASCII characters it can be specified as a
        three-tuple of (charset, language, value), in which case it will be
        encoded according to RFC2231 rules.  Otherwise it will be encoded using
        the utf-8 charset and a language of ''.

        Examples:

        msg.add_header('content-disposition', 'attachment', filename='bud.gif')
        msg.add_header('content-disposition', 'attachment',
                       filename=('utf-8', '', Fußballer.ppt'))
        msg.add_header('content-disposition', 'attachment',
                       filename='Fußballer.ppt'))
        """
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
 # start TLS for security 
s.starttls() 
# Authentication 
s.login(fromaddr, "yourpass") 
# Converts the Multipart msg into a string 
text = msg.as_string() 
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
# terminating the session 
s.quit()





import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "rahulsingh60verma@gmail.com"
receiver_email = "mukulkirtiverma@gmail.com"
password = ''

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p><h1>Hi,</h1><br>
       How are you?<br>
       <a href="http://www.inoneticx.com">inoneticx</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
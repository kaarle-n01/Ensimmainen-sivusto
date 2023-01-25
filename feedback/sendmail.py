#!/usr/bin/python
# coding=utf-8
import smtplib
import cgi, os
import cgitb
cgitb.enable()
#we use school smtp-server for sending the email (therefore it only accepts school emails!)
server = smtplib.SMTP('mail.puv.fi', 25)
print ("Content-type: text/html\r\n\r\n")
#this is the text that is shown in browser after Submit-button is clicked
print ("<html>Thank you for your feedback!</html>")
form = cgi.FieldStorage()
#In case you need more information how to send email via Python, see:
#https://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email
#This is the email message field 
# form["subject"].value ottaa arvon lomakkeen kentästä jolla name="subject"
# \n tekee rivinvaihdon mailissa
msg = "Text from first field: " + form["subject"].value + "\nText from another field: " + form["comment"].value  
#Send the mail (NOTE! Use your school email-address)
server.sendmail("YOUREMAIL@vamk.fi", "e2001972@vamk.fi", msg)

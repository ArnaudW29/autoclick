import pyautogui
import time
import threading
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="s")
clicking = False

cps = input("number between 1 and 5")


def test(input_chk):
    global cps
    if input_chk.strip().isdigit() and int(input_chk) <= 5:
        print("launching in 3 sec")
    else:
        cps = input("not a number ! or too big")
        test(cps)


test(cps)
cps = int(cps)
time.sleep(1), print("launching in 2 sec"), time.sleep(1), print("launching in 1 sec"), time.sleep(1), print("launched")


def click():
    while True:
        if clicking:
            pyautogui.click(clicks=cps)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=click)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

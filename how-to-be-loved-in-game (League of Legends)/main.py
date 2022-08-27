from random import randint

import pyautogui
import cv2
import pytesseract
import numpy as np
import time
from pynput.keyboard import Key, Controller

screenWidth, screenHeight = pyautogui.size()
i_killed = ["Thank you for the golds", "haha I'm better than you", "I love you", "how do you feel after I just destroyed you?"]
i_died = ["report my team", "your charachter is for noobs.", "get a life", "ff15"]
kills = 0
deaths = 0


def send_message(message):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.type(message)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def surrender():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.type("/ff")
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3)


def show_mastery():
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    time.sleep(0.3)


while 1:
    myScreenshot = pyautogui.screenshot(region=(screenWidth - 258, 0, 60, 30))
    myScreenshot.save(r'C:\Users\gab-a\OneDrive\Bureau\screenLoL\score.png')
    keyboard = Controller()

    img = cv2.imread(r'C:\Users\gab-a\OneDrive\Bureau\screenLoL\score.png')

    kernel = np.ones((2, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    pytesseract.pytesseract.tesseract_cmd = r'D:\Users\gab-a\AppData\Local\Tesseract-OCR\tesseract.exe'
    out_below = pytesseract.image_to_string(img)
    test = out_below.split('/')

    new_kills = int(test[0])
    new_deaths = int(test[1])
    if new_kills > kills:
        kills = new_kills
        show_mastery()
        send_message(i_killed[randint(0, len(i_killed) - 1)])

    if new_deaths > deaths:
        deaths = new_deaths
        surrender()
        send_message(i_died[randint(0, len(i_died) - 1)])
    time.sleep(0.5)

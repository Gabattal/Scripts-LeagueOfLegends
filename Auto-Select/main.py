import time
from pynput.keyboard import Key, Controller
import cv2
import pytesseract
import pyautogui
import webbrowser

pytesseract.pytesseract.tesseract_cmd = r'./utils/Tesseract-OCR/tesseract.exe'
screenWidth, screenHeight = pyautogui.size()
keyboard = Controller()
picks = []
bans = []
has_banned = False
has_picked = False

picks_file = open("picks.txt", "r").read().splitlines()
for line in picks_file:
    picks.append(line)

bans_file = open("bans.txt", "r").read().splitlines()
for line in bans_file:
    bans.append(line)

music_url = open("music.txt", "r").readline()


class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)


class MovieMP4(Video):
    type = "MP4"


def in_lobby():
    screen_lobby = pyautogui.screenshot(region=(580, 190, 70, 30))
    screen_lobby.save(r'./screen.png')
    img_screen_lobby = cv2.imread(r'./screen.png')
    screen_lobby_text = pytesseract.image_to_string(img_screen_lobby)
    if 'HOME' in screen_lobby_text:
        return False
    else:
        return True


def in_game():
    screen_score = pyautogui.screenshot(region=(1662, 0, 60, 30))
    screen_score.save(r'./screen.png')
    img_screen_score = cv2.imread(r'./screen.png')
    screen_score_text = pytesseract.image_to_string(img_screen_score)
    if '0/0/0' in screen_score_text:
        return True
    else:
        return False


def accept_match():
    while not in_lobby() and not in_game():
        print('accept match')
        screen_accept = pyautogui.screenshot(region=(900, 710, 130, 30))
        screen_accept.save(r'./screen.png')
        img_screen_accept = cv2.imread(r'./screen.png')
        screen_accept_text = pytesseract.image_to_string(img_screen_accept)
        global has_banned, has_picked
        has_banned = False
        has_picked = False
        if 'ACCEPT!' in screen_accept_text:
            pyautogui.click(950, 720)
        time.sleep(1)


def prepick():
    has_prepicked = False
    while not has_prepicked and in_lobby() and not in_game():
        print("prepick")
        time.sleep(10)
        pyautogui.click(1100, 265)
        keyboard.type(picks[0])
        has_prepicked = True
        time.sleep(1)
        pyautogui.click(700, 330)


def ban_champion():
    ban_number = 0
    global has_banned
    while not has_banned and in_lobby() and not in_game():
        print('ban match')
        screen_search = pyautogui.screenshot(region=(730, 160, 460, 50))
        screen_search.save(r'./screen.png')
        img_screen_search = cv2.imread(r'./screen.png')
        screen_search_text = pytesseract.image_to_string(img_screen_search)
        if 'BAN A CHAMPION!' in screen_search_text and not has_banned:
            pyautogui.click(1100, 265)
            pyautogui.click(1100, 265)
            keyboard.press(Key.delete)
            keyboard.type(bans[ban_number])
            time.sleep(1)
            pyautogui.click(700, 330)
            time.sleep(1)
            pyautogui.click(950, 770)
            time.sleep(2)

            screen_ban = pyautogui.screenshot(region=(730, 160, 460, 50))
            screen_ban.save(r'./screen.png')
            img_screen_ban = cv2.imread(r'./screen.png')
            screen_ban_text = pytesseract.image_to_string(img_screen_ban)
            ban_number += 1
            if 'BAN A CHAMPION!' not in screen_ban_text:
                has_banned = True
                print('yo')
            else:
                pyautogui.click(1000, 570)
            time.sleep(1)


def pick_champion():
    pick_number = 0
    global has_picked
    while not has_picked and in_lobby() and not in_game() and has_banned:
        print('pick champ')
        screen_search = pyautogui.screenshot(region=(730, 160, 460, 50))
        screen_search.save(r'./screen.png')
        img_screen_search = cv2.imread(r'./screen.png')
        screen_search_text = pytesseract.image_to_string(img_screen_search)
        if 'CHOOSE YOUR CHAMPION!' in screen_search_text and not has_picked:
            pyautogui.click(1100, 265)
            keyboard.type(picks[pick_number])
            time.sleep(1)
            pyautogui.click(700, 330)
            time.sleep(1)
            pyautogui.click(950, 770)

            screen_pick = pyautogui.screenshot(region=(730, 160, 460, 60))
            screen_pick.save(r'./screen.png')
            img_screen_pick = cv2.imread(r'./screen.png')
            screen_pick_text = pytesseract.image_to_string(img_screen_pick)
            pick_number += 1
            if 'CHOOSE YOUR CHAMPION!' not in screen_pick_text:
                has_picked = True
            else:
                pyautogui.click(1100, 265)
                pyautogui.click(1100, 265)
                keyboard.press(Key.delete)
            time.sleep(1)


def execute():
    while not in_game():
        accept_match()
        prepick()
        ban_champion()
        pick_champion()
    webbrowser.open(music_url, new=0, autoraise=True)


execute()

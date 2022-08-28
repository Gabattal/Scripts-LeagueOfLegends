from random import randint
import time
from pynput.keyboard import Key, Controller
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

<<<<<<< HEAD
=======
screenWidth, screenHeight = pyautogui.size()
>>>>>>> 1a1bd9f9b907da0c72fbada4238030f16a92171f
i_killed = ["/all Thank you for the golds", "/all haha I'm better than you",
            "/all how do you feel after I just destroyed you?", "/all sit", "/all get rekt", "/all I feel your pain",
            "/all EZ clapped", "/all I'm not arrogant, I'm good",
            "/all Do you mind leaving the game? I would rather play with the AI.",
            "/all Don't be coming up in my kitchen with your weaksauce.",
            "/all Where's your homework? Cause you guys just got schooled.",
            "/all Are you Neymar? Because I see you more often on the floor lying down than playing"]
i_died = ["/all report my team",
          "/all your champ is designed for people who have a social life, basically people who don't know how to play.",
          "/all I'm done with this game", "/all jungler diff",
          "/all I don't want to play this game, I just want to raise sheeps in the mountains",
          "/all If I wanted to end with my life, I'd jump from your ego to your elo",
          "/all If I wanted to support 4 talentless douchebags I could have just bought a Nickelback album",
          "/all Its okay that you're all trash. It's called garbage can, not garbage cannot. Lets do this",
          "/all You guys are garbanzo beans", "/all Your grandma makes cookies really really bad"]
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
    time.sleep(0.1)


def show_mastery():
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)
    time.sleep(0.1)


while 1:
    keyboard = Controller()
    try:
        response_API = requests.get('https://127.0.0.1:2999/liveclientdata/playerscores?summonerName=YOUR_PSEUDO_HERE',
                                     verify=False)
        statistics = response_API.json()
        new_kills = statistics['kills']
        new_deaths = statistics['deaths']

<<<<<<< HEAD
=======
    img = cv2.imread(r'C:\Users\gab-a\OneDrive\Bureau\Jokes-script\scripts\how-to-be-loved-in-game (League of Legends)\screenshot')

    kernel = np.ones((2, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    pytesseract.pytesseract.tesseract_cmd = r'D:\Users\gab-a\AppData\Local\Tesseract-OCR\tesseract.exe'
    out_below = pytesseract.image_to_string(img)
    test = out_below.split('/')

    if score[0].isdigit() and score[1].isdigit():
        new_kills = int(score[0])
        new_deaths = int(score[1])
>>>>>>> 1a1bd9f9b907da0c72fbada4238030f16a92171f
        if new_kills > kills:
            kills = new_kills
            show_mastery()
            send_message(i_killed[randint(0, len(i_killed) - 1)])
<<<<<<< HEAD
=======

>>>>>>> 1a1bd9f9b907da0c72fbada4238030f16a92171f
        if new_deaths > deaths:
            deaths = new_deaths
            surrender()
            send_message(i_died[randint(0, len(i_died) - 1)])
<<<<<<< HEAD
        time.sleep(1)
    except:
        print("An exception occurred")
=======
    time.sleep(0.5)
>>>>>>> 1a1bd9f9b907da0c72fbada4238030f16a92171f

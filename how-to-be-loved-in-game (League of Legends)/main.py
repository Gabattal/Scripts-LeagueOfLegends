from random import randint
import time
from pynput.keyboard import Key, Controller
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
        if new_kills > kills:
            kills = new_kills
            show_mastery()
            send_message(i_killed[randint(0, len(i_killed) - 1)])
        if new_deaths > deaths:
            deaths = new_deaths
            surrender()
            send_message(i_died[randint(0, len(i_died) - 1)])
        time.sleep(1)
    except:
        print("An exception occurred")

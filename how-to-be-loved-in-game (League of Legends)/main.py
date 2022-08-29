from random import randint
import time
from pynput.keyboard import Key, Controller
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

i_killed = ["/all How did this guy get passed the login screen ? ", "/all haha I'm better than you",
            "/all how do you feel after I just destroyed you?", "/all sit", "/all get rekt",
            "/all EZ clapped", "/all I'm not arrogant, I'm good",
            "/all Do you mind leaving the game? I would rather play with the AI.",
            "/all Don't be coming up in my kitchen with your weaksauce.",
            "/all Where's your homework? Cause you guys just got schooled.",
            "/all Are you Neymar? Because I see you more often on the floor lying down than playing",
            "/all I can't even call you an animal, these have a survival instinct at least",
            "/all  I would call you a walking ward, but even wards live longer.",
            "/all cry me a river and put a ward in it",
            "/all *knock knock* -Who's there ? -Uni -Uni who? -Uninstall",
            "/all  anyone has a good tutorial on how to change bots difficulty?",
            "/all You are the single reason why Shurima is more dead than pre-rework Yorick",
            "/all if you were a sandwich, you would be an idiot sandwich",
            "/all if you cooked like you are playing, you would have a visit from Gordon Ramsay very soon..."
            ]
i_died = ["/all report my team",
          "The scuttle crab applies more jungle pressure than you.  .",
          "/all I'm done with this game", "/all jungler diff",
          "/all I don't want to play this game, I just want to raise sheeps in the mountains",
          "/all If I wanted to end with my life, I'd jump from your ego to your elo",
          "/all If I wanted to support 4 talentless douchebags I could have just bought a Nickelback album",
          "Its okay that you're all trash. It's called garbage can, not garbage cannot. Lets do this",
          "/all You guys are garbanzo beans", "/all Your grandma makes cookies really really bad",
          "/all My team is so bad they can't even win a surrender vote",
          "/all It's not my fault bot lane started with a Doran's Spoon and fed the shit out of Draven",
          "/all Not even Noah can carry these animals",
          "/all You would need a gank when laning against a minion",
          "My push-up bra supports better than you"]

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

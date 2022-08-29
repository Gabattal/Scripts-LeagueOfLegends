from random import randint
import time
from pynput.keyboard import Key, Controller
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Which mode would you like ?\n"
      "Press 1 if you want to pick your sentences randomly\n"
      "Press 2 if you want to pick your sentences in the order \n"
      "(it goes back to the first sentence when you typed them all)"
      )
mode = input()

you_killed = []
you_died = []

you_killed_sentence_number = 0
you_died_sentence_number = 0

deaths = 0
kills = 0

in_game = True

f1 = open("you_killed.txt", "r").read().splitlines()
for line in f1:
    you_killed.append(line)

f2 = open("you_died.txt", "r").read().splitlines()
for line in f2:
    you_died.append(line)


def send_message(message):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.02)
    keyboard.type(message)
    time.sleep(0.02)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.02)


while 1:
    keyboard = Controller()
    try:
        request_pseudo = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayername', verify=False)
        your_pseudo = request_pseudo.json()
        response_API = requests.get(f'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={your_pseudo}',
                                    verify=False)
        statistics = response_API.json()
        if request_pseudo and response_API and not in_game:
            print("Game found!")
            in_game = True
        new_kills = statistics['kills']
        new_deaths = statistics['deaths']
        if new_kills > kills:
            kills = new_kills
            if mode == 1:
                send_message(you_killed[randint(0, len(you_killed) - 1)])
            else:
                if you_killed_sentence_number == len(you_killed) - 1:
                    you_killed_sentence_number = 0
                send_message(you_killed[you_killed_sentence_number])
                you_killed_sentence_number += 1
        if new_deaths > deaths:
            deaths = new_deaths
            if mode == 1:
                send_message(you_died[randint(0, len(you_died) - 1)])
            else:
                if you_died_sentence_number == len(you_died) - 1:
                    you_died_sentence_number = 0
                send_message(you_died[you_died_sentence_number])
                you_died_sentence_number += 1
        time.sleep(1)
    except:
        if in_game:
            print("Searching for game...")
        in_game = False

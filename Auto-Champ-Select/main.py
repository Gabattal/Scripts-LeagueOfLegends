import time
import requests
import urllib3
from lcu_driver import Connector
import webbrowser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

in_game = False

connector = Connector()


@connector.ready
async def connect(connection):
    global summoner_id, champions_map
    temp_champions_map = {}
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    summoner_to_json = await summoner.json()
    summoner_id = summoner_to_json['summonerId']
    champion_list = await connection.request('get', f'/lol-champions/v1/inventories/{summoner_id}/champions-minimal')

    champion_list_to_json = await champion_list.json()
    for i in range(len(champion_list_to_json)):
        temp_champions_map.update({champion_list_to_json[i]['name']: champion_list_to_json[i]['id']})
    champions_map = temp_champions_map


@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def ready_check_changed(connection, event):
    if event.data['state'] == 'InProgress' and event.data['playerResponse'] == 'None':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept', data={})


@connector.ws.register('/lol-champ-select/v1/session', event_types=('CREATE', 'UPDATE',))
async def champ_select_changed(connection, event):
    picks = []
    bans = []
    pick_number = 0
    ban_number = 0
    global in_game

    picks_file = open("picks.txt", "r").read().splitlines()
    for line in picks_file:
        picks.append(line)

    bans_file = open("bans.txt", "r").read().splitlines()
    for line in bans_file:
        bans.append(line)

    phase = event.data['actions'][-1][0]['type']
    action_id = event.data['actions'][-1][0]['id']
    is_in_progress = event.data['actions'][-1][0]['isInProgress']

    while phase == 'ban':
        try:
            await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                     data={"championId": champions_map[bans[ban_number]], "completed": False})
            break
        except (Exception,):
            ban_number += 1
    while phase == 'pick':
        try:
            await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                     data={"championId": champions_map[picks[pick_number]], "completed": True})
            break
        except (Exception,):
            pick_number += 1

    if not is_in_progress:
        while not in_game:
            try:
                request_pseudo = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayername', verify=False)
                your_pseudo = request_pseudo.json()
                response_API = requests.get(
                    f'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={your_pseudo}',
                    verify=False)
                if request_pseudo and response_API and not in_game:
                    print("Game found!")
                    in_game = True
                    music_url = open("music.txt", "r").readline()
                    webbrowser.open(music_url, new=0, autoraise=True)
                time.sleep(1)
            except (Exception,):
                print('Waiting for game to start...')
                time.sleep(1)


@connector.close
async def disconnect(_):
    print('The client have been closed!')
    await connector.stop()


connector.start()

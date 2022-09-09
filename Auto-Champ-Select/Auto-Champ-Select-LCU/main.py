import time
import requests
import urllib3
from lcu_driver import Connector
import webbrowser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

connector = Connector()
global am_i_assigned, am_i_picking, am_i_banning, ban_number, phase, picks, bans, in_game
am_i_assigned = False
am_i_banning = False
am_i_picking = False
in_game = False
phase = ''
picks = []
bans = []
pick_number = 0
ban_number = 0

picks_file = open("picks.txt", "r").read().splitlines()
for line in picks_file:
    picks.append(line)

bans_file = open("bans.txt", "r").read().splitlines()
for line in bans_file:
    bans.append(line)


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
    global am_i_assigned, pick_number, ban_number, am_i_banning, am_i_picking, phase, bans, picks, have_i_prepicked, in_game, action_id
    have_i_prepicked = False
    lobby_phase = event.data['timer']['phase']

    local_player_cell_id = event.data['localPlayerCellId']
    for teammate in event.data['myTeam']:
        if teammate['cellId'] == local_player_cell_id:
            assigned_position = teammate['assignedPosition']
            am_i_assigned = True

    for action in event.data['actions']:
        for actionArr in action:
            if actionArr['actorCellId'] == local_player_cell_id and actionArr['isInProgress'] == True:
                phase = actionArr['type']
                action_id = actionArr['id']
                if phase == 'ban':
                    am_i_banning = actionArr['isInProgress']
                if phase == 'pick':
                    am_i_picking = actionArr['isInProgress']

    if phase == 'ban' and lobby_phase == 'BAN_PICK' and am_i_banning:
        while am_i_banning:
            try:
                await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                         data={"championId": champions_map[bans[ban_number]], "completed": True})
                ban_number += 1
                am_i_banning = False
            except (Exception,):
                ban_number += 1
                if ban_number > len(
                        bans):  # Due to some lcu bugs I have to do this to correct a bug that may happen in draft custom
                    ban_number = 0
    if phase == 'pick' and lobby_phase == 'BAN_PICK' and am_i_picking:
        while am_i_picking:
            try:
                await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                         data={"championId": champions_map[picks[pick_number]], "completed": True})
                pick_number += 1
                am_i_picking = False
            except (Exception,):
                pick_number += 1
                if pick_number > len(
                        picks):  # Due to some lcu bugs I have to do this to correct a bug that may happen in draft custom
                    pick_number = 0
    if lobby_phase == 'PLANNING' and not have_i_prepicked:
        try:
            await connection.request('patch', '/lol-champ-select/v1/session/actions/%d' % action_id,
                                     data={"championId": champions_map['Teemo'], "completed": False})
            have_i_prepicked = True
        except (Exception,):
            print(Exception)
    if lobby_phase == 'FINALIZATION':
        while not in_game:
            try:
                request_game_data = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify=False)
                game_data = request_game_data.json()['gameData']['gameTime']
                if game_data > 0 and not in_game:
                    print("Game found!")
                    in_game = True
                    music_url = open("music.txt", "r").readline()
                    webbrowser.open(music_url, new=0, autoraise=True)
                time.sleep(2)
            except (Exception,):
                print('Waiting for game to start...')
                time.sleep(2)


@connector.close
async def disconnect(_):
    print('The client has been closed!')
    await connector.stop()


connector.start()

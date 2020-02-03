import os
import json
import pytz
from datetime import datetime

CHAMPION_FILE = 'res/champion.json'
ID_TO_CHAMPION_FILE = 'res/idToChampion.json'

def getGameTime(timestamp):
    est = pytz.timezone('US/Eastern')
    dt = datetime.utcfromtimestamp(timestamp / 1000)
    return dt.astimezone(est).strftime('%B %d, %Y  %H:%M EST')


def getGameResult(game, summonerName):
    participantIdentities = game['participantIdentities']
    playerId = -1
    for p in participantIdentities:
        if p['player']['summonerName'] == summonerName:
            playerId = p['participantId']
            break

    participants = game['participants']
    teamId = -1
    for p in participants:
        if p['participantId'] == playerId:
            teamId = p['teamId']
            break

    teams = game['teams']
    for t in teams:
        if t['teamId'] == teamId:
            if t['win'] == 'Win':
                return 'WIN'
            else:
                return 'LOSS'


def getChampionName(champId):
    if os.path.exists(ID_TO_CHAMPION_FILE):
        with open(ID_TO_CHAMPION_FILE) as jsonFile:
            try:
                data = json.load(jsonFile)
                return data[str(champId)]
            except:
                print('Error reading file: ' + ID_TO_CHAMPION_FILE + '.')
    else:
        print('File ' + ID_TO_CHAMPION_FILE + ' could not be found.')


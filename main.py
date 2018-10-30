import json

from sambot import Sambot

if __name__ == '__main__':
    with open('auth.json') as jsonFile:
        data = json.load(jsonFile)
        token = data['token']

    sambot = Sambot(token)
    sambot.run()


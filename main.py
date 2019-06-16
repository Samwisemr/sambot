import json
import os

from sambot import Sambot

AUTH_FILE = 'auth.json'

if __name__ == '__main__':
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE) as jsonFile:
            try:
                data = json.load(jsonFile)
                token = data['token']
            except:
                print('Error reading file: ' + AUTH_FILE + '. Exiting.')
    else:
        print('File ' + AUTH_FILE + ' could not be found. Exiting.')

    sambot = Sambot(token)
    sambot.run()

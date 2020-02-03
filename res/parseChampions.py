import json
import os
import sys

def parseChampions(champions):
    newDict = {}
    for name, data in champions.items():
        newDict[data['key']] = name

    with open('idToChampion.json', 'w') as outfile:
        json.dump(newDict, outfile)

    print('Data writen to idToChampion.json')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Invalid number of arguments. Exiting.')
    elif os.path.exists(sys.argv[1]):
        with open(sys.argv[1]) as jsonFile:
            try:
                data = json.load(jsonFile)
                parseChampions(data['data'])
            except:
                print('Error parsing file: ' + sys.argv[1] + '. Exiting.')
    else:
        print('File ' + sys.argv[1] + ' could not be found. Exiting.')



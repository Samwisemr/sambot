import discord
import asyncio
import aiohttp
import random
import requests
import re
from datetime import datetime
from time import strftime

import lolUtils
from warbandTimes import getTimeTillNextWarband

class Sambot:
    def __init__(self, discord_token, lotr_token, riot_token):
        self.discord_token = discord_token
        self.lotr_token = lotr_token
        self.riot_token = riot_token
        self.client = discord.Client()

        self.setup()

    def setup(self):

        @self.client.event
        async def on_message(message):
            # ignore all bots
            if message.author.bot:
                return
            elif message.content.startswith('!sambot ') or message.content.startswith('/sambot '):
                args = message.content[8:]

                if args == 'help':
                    await self.help(message.channel)
                elif args == 'hi' or args == 'hello' or args == 'yo' or args == 'hey':
                    await self.greeting(message.channel)
                elif args == 'merch':
                    await self.merch(message.channel)
                elif args.startswith('spam '):
                    await self.spam(message.channel, message)
                elif args == 'teleport':
                    await self.teleport(message.channel)
                elif args == 'tell me a story':
                    await self.storytime(message)
                elif args == 'warbands' or args == 'warband' or args == 'how long until the next warband?':
                    await self.wildernessWarbands(message.channel)
                elif args == 'quote':
                    await self.quote(message.channel)
                elif args.startswith('lol '):
                    await self.leagueOfLegends(message.channel, args[4:])
                elif args == 'I\'m tilted' or args == 'tilt':
                    await self.tilt(message.channel, message)
                else:
                    await self.say(message.channel, 'That\'s not a command. You obviously have no clue what you\'re doing you idiot\nUse `!sambot help` if you\'re lost')
            elif message.content.lower() == 'omae wa mou shindeiru':
                await self.say(message.channel, 'NANI??')

                # if args == 'love me' or msg == 'show me love' or msg == 'show me some love':
                #     async for pastMessage in bot.logs_from(message.channel):
                #         if pastMessage.author == message.author:
                #             await bot.add_reaction(pastMessage, ':heart:')
                #             return

        @self.client.event
        async def on_member_join(member):
            for channel in member.guild.channels:
                if channel.permissions_for(member.guild.me).send_messages and channel.type is discord.ChannelType.text:
                    await self.say(channel, 'Welcome to this little crew of sambot worshipers ' + member.mention + '! You idiot')
                    break

        @self.client.event
        async def on_guild_join(guild):
            for channel in guild.channels:
                if channel.permissions_for(guild.me).send_messages and channel.type is discord.ChannelType.text:
                    await self.say(channel, 'Welcome to ME bitchezzz')
                    break

        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

            # for guild in self.client.guild:
            #     for channel in guild.channels:
            #         if channel.permissions_for(guild.me).send_messages and channel.type is discord.ChannelType.text:
            #             await self.say(channel, 'I\'m heeerrreeee')
            #             await self.say(channel, 'you idiots')
            #             break


    async def say(self, chan, msg):
        async with chan.typing():
            await asyncio.sleep(0.5)
            await chan.send(msg)

    async def help(self, chan):
        msg = '''
        sambot usage:

        ----

        PREFIX COMMAND [command arguments]
        or
        omae wa mou shindeiru

        ----

        PREFIX options:
            !sambot
            /sambot

        COMMANDs:
            help
                show this help message

            hi | hello | yo | hey
                say hi to sambot

            merch
                do the merch dance

            spam MENTION [ADDITIONAL-MENTIONS...]
                spams whoever is included in MENTIONS

            teleport
                teleports everyone active in a voice channel to a very special place temporarily

            tell me a story
                story time with sambot

            warband[s]
                get time till next wilderness warband

            quote
                shares some inspirational quotes

            lol mh SUMMONER_NAME
                displays a summary of the summoner's last five games

            tilt | I'm tilted
                puts things into perspective
        '''
        await self.say(chan, msg)

    async def greeting(self, chan):
        greeting = random.choice(['aaayo', 'Hello there!', 'Ça va?', 'yo', 'Oi mate', 'ciao bud', 'what it do?', 'sup'])
        await self.say(chan, greeting)

    async def merch(self, chan):
        await self.say(chan, 'merch')

        for i in range(3):
            async with chan.typing():
                await asyncio.sleep(0.75)
                await chan.send('merch')

    async def spam(self, chan, msg):
        if not msg.mentions:
            await self.say(chan, 'You didn\'t mention anyone to spam you idiot')
            return
        for member in msg.mentions:
            for i in range(4):
                await self.say(chan, 'Hey' + member.mention)

    async def teleport(self, chan):
        newChan = await chan.guild.create_voice_channel('Ben\'s Asshole')
        membersChannels = []
        nonVoiceMembers = []

        for member in chan.guild.members:
            if member.status == discord.Status.online:
                if member.voice.voice_channel is not None:
                    membersChannels.append((member, member.voice.voice_channel))
                    await member.move_to(newChan)
                else:
                    if not member.bot:
                        nonVoiceMembers.append(member)

        mentions = nonVoiceMembers[0].mention
        for member in nonVoiceMembers[1:]:
            mentions += ', ' + member.mention
        await self.say(chan, 'Hey' + member.mention + ', get in a voice channel so I can teleport you, you idiot')

        await asyncio.sleep(10)
        await self.say(chan, 'Ok teleporting ya\'ll back now')
        for pair in membersChannels:
            await pair[0].move_to(pair[1])

        await newChan.delete()

    async def storytime(self, message):
        string1 = 'Did you ever hear the tragedy of Darth Plagueis "the wise"?'
        string2 = ('I thought not. It\'s not a story the Jedi would tell you. It\'s a Sith legend. '
                'Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the '
                'Force to influence the midichlorians to create life... He had such a knowledge of the '
                'dark side that he could even keep the ones he cared about from dying.')
        string3 = 'The dark side of the Force is a pathway to many abilities some consider to be unnatural.'
        string4 = ('He became so powerful... the only thing he was afraid of was losing his power, which eventually, '
                'of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice '
                'killed him in his sleep. It\'s ironic he could save others from death, but not himself.')

        await self.say(message.channel, string1)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and (msg.content.startswith('No') or msg.content.startswith('no'))

        response = await self.client.wait_for('message', check=check, timeout=10.0)

        await self.say(message.channel, string2)
        await self.say(message.channel, string3)
        await self.say(message.channel, string4)

    async def wildernessWarbands(self, chan):
        hours, minutes = getTimeTillNextWarband()
        hoursWord = 'hours'
        minutesWord = 'minutes'
        if hours == 1:
            hoursWord = 'hour'
        if minutes == 1:
            minutesWord = 'minute'

        if hours == 0 and minutes == 0:
            await self.say(chan, 'A warband just started!')
        elif hours == 0:
            await self.say(chan, f'The next warband is in {minutes} {minutesWord}')
        elif minutes == 0:
            await self.say(chan, f'The next warband is in {hours} {hoursWord}')
        else:
            await self.say(chan, f'The next warband is in {hours} {hoursWord} and {minutes} {minutesWord}')

    async def quote(self, chan):
        LOTR_API_URL = 'https://the-one-api.dev/v2'
        headers = {'Authorization': 'Bearer ' + self.lotr_token}

        try:
            async with chan.typing():
                r = requests.get(LOTR_API_URL + '/quote', headers=headers)
                json = r.json()
                data = json['docs']
                quote = random.choice(data)
                characterId = quote['character']
                quoteDialog = quote['dialog']

                r = requests.get(LOTR_API_URL + '/character/' + characterId, headers=headers)
                json = r.json()
                data = json['docs'][0]
                characterName = data['name']

                quoteDialog = re.sub('\s+', ' ', quoteDialog).strip()

                msg = '```' + quoteDialog + '\n\t- ' + characterName + '```'

                await self.say(chan, msg)
        except Exception as e:
            print(e)
            await self.say(chan, 'Hmm I\'m drawing a blank on quotes right now. It\'s not my fault, I promise')

    async def leagueOfLegends(self, chan, args):
        if args.startswith('mh '):
            await self.matchHistory(chan, args[3:])
        else:
            await self.say(chan, 'That\'s not a command. You obviously have no clue what you\'re doing you idiot\nUse `!sambot help` if you\'re lost')

    async def matchHistory(self, chan, summonerName):
        SUMMONER_API_URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
        MATCHLIST_API_URL = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'
        headers = {'X-Riot-Token': self.riot_token}

        try:
            async with chan.typing():
                r = requests.get(SUMMONER_API_URL + summonerName, headers=headers)
                json = r.json()
                accountId = json['accountId']

                payload = {'endIndex': '5'}
                r = requests.get(MATCHLIST_API_URL + accountId, params=payload, headers=headers)
                json = r.json()

                matchHistory = []
                for i, game in enumerate(json['matches']):
                    MATCH_API_URL = 'https://na1.api.riotgames.com/lol/match/v4/matches/'
                    matchId = game['gameId']

                    r = requests.get(MATCH_API_URL + str(matchId), headers=headers)
                    gameData = r.json()

                    gameTime = lolUtils.getGameTime(game['timestamp'])
                    gameResult = lolUtils.getGameResult(gameData, summonerName)
                    champion = lolUtils.getChampionName(game['champion'])

                    gameOutput = (gameTime, champion, gameResult)

                    matchHistory.append(gameOutput)

                historyOutput = '```'
                for game in matchHistory:
                    historyOutput = historyOutput + '\n' + game[0] + ' -- ' + game[1] + ' -- ' + game[2] + '\n'

                historyOutput = historyOutput + '```'

                await self.say(chan, historyOutput)
        except:
            await self.say(chan, 'I can\'t seem to find a match history for that summoner at the moment. It\'s not my problem so don\'t blame me.')


    async def tilt(self, chan, message):
        CONRAD_ID = 265584372021723136
        if message.author.id == CONRAD_ID:
            msg = 'You don\'t fear the tilt, you welcome it. Your punishment must be more severe.'
        else:
            msg = 'Ah you think the tilt is your ally? You merely adopted the tilt. Conrad was born in it, molded by it. He didn\'t see a win until he was already a man, by then it was nothing to him but blinding!'
        await self.say(chan, msg)


    def run(self):
        self.client.run(self.discord_token)


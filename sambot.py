import discord
import asyncio
import aiohttp


class Sambot:
    def __init__(self, token):
        self.token = token
        self.client = discord.Client()

        self.setup()

    def setup(self):

        @self.client.event
        async def on_message(message):
            # ignore all bots
            if message.author.bot:
                return
            elif message.content.startswith('!sambot '):
                args = message.content[8:]

                if args == 'help':
                    await self.say(message.channel, 'Don\'t ask me')
                elif args == 'merch':
                    await self.merch(message.channel)
                elif args.startswith('spam '):
                    await self.spam(message.channel, message)
                elif args == 'teleport':
                    await self.teleport(message.channel)
                elif args == 'tell me a story':
                    await self.storytime(message)
                else:
                    await self.say(message.channel, 'That\'s not a command. You obviously have no clue what you\'re doing you idiot')
            elif message.content.lower() == 'omae wa mou shindeiru':
                await self.say(message.channel, 'NANI??')

                # if args == 'love me' or msg == 'show me love' or msg == 'show me some love':
                #     async for pastMessage in bot.logs_from(message.channel):
                #         if pastMessage.author == message.author:
                #             await bot.add_reaction(pastMessage, ':heart:')
                #             return

        @self.client.event
        async def on_member_join(member):
            await self.say(member.server.default_channel, 'Welcome to this little crew of sambot worshipers ' + member.mention + '! You idiot')

        @self.client.event
        async def on_server_join(server):
            await self.say(server.default_channel, 'Welcome to ME bitchezzz')

        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')


    async def say(self, chan, msg):
        await self.client.send_typing(chan)
        await asyncio.sleep(0.5)
        await self.client.send_message(chan, msg)

    # async def mention(bot, chan,

    async def merch(self, chan):
        await self.say(self.client, chan, 'merch')

        for i in range(3):
            await self.client.send_typing(chan)
            await asyncio.sleep(0.75)
            await self.client.send_message(chan, 'merch')

    async def spam(self, chan, msg):
        if not msg.mentions:
            await self.say(self.client, chan, 'You didn\'t mention anyone to spam you idiot')
            return
        for member in msg.mentions:
            for i in range(4):
                await self.say(chan, 'Hey' + member.mention)

    async def teleport(self, chan):
        newChan = await self.client.create_channel(chan.server, 'Ben\'s Asshole', type=discord.ChannelType.voice)
        membersChannels = []
        nonVoiceMembers = []

        for member in chan.server.members:
            if member.status == discord.Status.online:
                if member.voice.voice_channel is not None:
                    membersChannels.append((member, member.voice.voice_channel))
                    await self.client.move_member(member, newChan)
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
            await self.client.move_member(pair[0], pair[1])

        await self.client.delete_channel(newChan)

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
            return msg.content.startswith('No') or msg.content.startswith('no')

        response = await self.client.wait_for_message(timeout=10.0, author=message.author, channel=message.channel, check=check)

        await self.say(message.channel, string2)
        await self.say(message.channel, string3)
        await self.say(message.channel, string4)

    def run(self):
        self.client.run(self.token)


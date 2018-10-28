import discord
import asyncio
import aiohttp
import json

from discord.utils import get


async def say(bot, chan, msg):
    await bot.send_typing(chan)
    await asyncio.sleep(0.5)
    await bot.send_message(chan, msg)


async def merch(bot, chan):
    await say(bot, chan, 'merch')

    for i in range(3):
        await bot.send_typing(chan)
        await asyncio.sleep(0.75)
        await bot.send_message(chan, 'merch')

async def spam(bot, chan, msg):
    if not msg.mentions:
        await say(bot, chan, 'You didn\'t mention anyone to spam you idiot')
        return
    for member in msg.mentions:
        for i in range(4):
            await say(bot, chan, 'Hey' + member.mention)

async def teleport(bot, chan):
    newChan = await bot.create_channel(chan.server, 'Ben\'s Asshole', type=discord.ChannelType.voice)

    for member in chan.server.members:
        if member.status == discord.Status.online:
            if member.voice.voice_channel is not None:
                await bot.move_member(member, newChan)
            else:
                if not member.bot:
                    await say(bot, chan, 'Hey' + member.mention + ', get in a voice channel so I can teleport you, you idiot')

    await asyncio.sleep(10)
    await say(bot, chan, 'Ok teleporting ya\'ll back now')
    await bot.delete_channel(newChan)





if __name__ == '__main__':
    with open('auth.json') as jsonFile:
        data = json.load(jsonFile)
        TOKEN = data['token']

    bot = discord.Client();

    @bot.event
    async def on_message(message):
        # ignore all bots
        if message.author.bot: return

        if message.content.lower() == 'omae wa mou shindeiru':
            await say(bot, message.channel, 'NANI??')

        elif message.content.startswith('sambot '):
            args = message.content[7:]

            if args == 'help':
                await say(bot, message.channel, 'Fuck you')
            elif args == 'merch':
                await merch(bot, message.channel)
            elif args.startswith('spam '):
                await spam(bot, message.channel, message)
            elif args == 'teleport':
                await teleport(bot, message.channel)
            else:
                await say(bot, message.channel, 'That\'s not a command. You obviously have no clue what you\'re doing you idiot')




            # if args == 'love me' or msg == 'show me love' or msg == 'show me some love':
            #     async for pastMessage in bot.logs_from(message.channel):
            #         if pastMessage.author == message.author:
            #             await bot.add_reaction(pastMessage, ':heart:')
            #             return



    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')


    bot.run(TOKEN)

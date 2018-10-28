import discord
import asyncio
import aiohttp
import json

from discord.utils import get


async def say(bot, chan, msg):
    await bot.send_typing(chan)
    await asyncio.sleep(0.5)
    await bot.send_message(chan, msg)


async def merchCommand(bot, chan):
    await say(bot, chan, 'merch')

    for i in range(3):
        await bot.send_typing(chan)
        await asyncio.sleep(0.75)
        await bot.send_message(chan, 'merch')



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
                await merchCommand(bot, message.channel)




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

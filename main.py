import discord
import asyncio
import aiohttp
import json

from discord.utils import get


async def merchCommand(bot, channel):
    await bot.send_typing(channel)
    await bot.send_message(channel, 'merch')

    for i in range(3):
        await bot.send_typing(channel)
        await asyncio.sleep(0.75)
        await bot.send_message(channel, 'merch')


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
            newMessage = 'NANI??'

            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, newMessage)


        elif message.content.startswith('sambot '):
            args = message.content[7:]

            if args == 'merch':
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

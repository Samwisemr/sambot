import discord
import asyncio
import aiohttp
import json


if __name__ == '__main__':
    with open('auth.json') as jsonFile:
        data = json.load(jsonFile)
        TOKEN = data['token']

    client = discord.Client();


    @client.event
    async def onMessage(message):
        # ignore all bots
        if message.author.bot: return





    client.run(TOKEN)



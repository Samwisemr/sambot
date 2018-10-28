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
    async def on_message(message):
        # ignore all bots
        if message.author.bot: return
        if message.content.startswith('sambot ') or message.content.startswith('sambot, '): return

        if message.content.lower() == 'omae wa mou shindeiru':
            newMessage = 'NANI??'
            await client.send_message(message.channel, newMessage)



    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')


    client.run(TOKEN)


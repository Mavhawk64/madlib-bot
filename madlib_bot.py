import discord
import os
from dotenv import load_dotenv
import requests

command_key = '&'


load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=command_key+"help"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(command_key+'hello'):
        await message.channel.send('hello jello!')
    if message.content.startswith(command_key+'help'):
        await message.channel.send('much help! very wow!')
client.run(os.getenv('TOKEN'))
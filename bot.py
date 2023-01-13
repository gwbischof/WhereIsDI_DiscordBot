import discord
import os
import requests
import time
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_location(server=4):
    """
    Get the DI location from the whereisdi api.
    Server 4 is Bahamut.
    """

    query = f"https://api.whereisdi.com/items/di_location?fields=*.*&sort=-date_created&limit=1&filter[server][_eq]={server}"
    try:
        response = requests.get(query)
        location = response.json()['data'][0]['location']['en_us']
    except Exception:
        location = "Failed to get DI location"
    return location

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):

    mention = message.author.mention

    if message.author == client.user:
        return

    if message.content.startswith('!di'):

        channel = client.get_channel(1063500585351004160)

        # await message.channel.send('`Use`**`!where`**`to display current Domain Invasion location!`')
        await channel.send(f'{mention}, Please use **!where** to display current Domain Invasion location!')

    if message.content.startswith('!where'):
        await message.channel.send(f'{mention} **DI is currently at:** \n {get_location()}')

client.run(DISCORD_TOKEN)

























# client = commands.Bot(command_prefix='!', intents=intents)



# @client.event
# async def on_ready():
#     print('Bot is online!')

# @client.event
# async def on_message(message):
#     print(message.author, message.content, message.channel.id)

# @client.command
# async def hello(ctx):
#     channel = (1063456560715681825)
#     await channel.send(f'hello there {ctx.author.mention}')




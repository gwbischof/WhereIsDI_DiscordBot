import os
from dotenv import load_dotenv
from pathlib import Path
import time
import discord
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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

        filepath = Path("E:\\WhereIsDI\\whereisdi\\DI.txt")
        filepath.stat().st_size == 0 # If 0 file is empty
        
        if filepath.stat().st_size == 0:
            await message.channel.send(f'{mention} Please stand by. Fetching Data!')
            time.sleep(3)
            f = open("E:\\WhereIsDI\\whereisdi\\DI.txt", "r")
            await message.channel.send(f'{mention} **DI is currently at:** \n' + f.readline())

        else:
            f = open("E:\\WhereIsDI\\whereisdi\\DI.txt", "r")
            await message.channel.send(f'{mention} **DI is currently at:** \n' + f.readline())
        
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




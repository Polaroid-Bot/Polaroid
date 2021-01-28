import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from asyncio import sleep
from discord.utils import get


load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents.all()
client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('p!'), help_command=None, intents=intents, case_insensitive=True)


@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'dsc.gg/polaroid! | p!help'))



extensions = ['Cogs.supportserver', 'Cogs.filters']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.run(token)
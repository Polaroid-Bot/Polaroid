import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from asyncio import sleep
from discord.utils import get
import aiohttp

load_dotenv()

colors = [0xe3a2fc, 0x0da2ff]
token = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.members = True

client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('p! '), help_command=None, intents=intents, case_insensitive=True)
client.aiohttp_session = aiohttp.ClientSession()


@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'dsc.gg/plrd | p! help'))


extensions = ['Cogs.search', 'Cogs.emojis','Cogs.extrautils', 'Cogs.manipulation', 'Cogs.help', 'Cogs.supportserver', 'Cogs.filters']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.run(token)

from discord.ext import commands
import discord
from asyncio import sleep 
from discord.utils import get
import tracemalloc
client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('tsu!'), help_comamnd = None)

@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    

@client.command()
async def info(ctx):
    mbed  = discord.Embed(
        color = discord.Color(0xe3a2fc),
        title = 'TSUKI',
        description = '***tsu!loop <channel> (partnership reminder), tsu!announce <channel> <message>***',
    )
    if ctx.author.guild_permissions.administrator:
        await ctx.send(embed = mbed)

@client.command()
async def loop(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(
        title = 'Success.',
        color = discord.Color(0xe3a2fc),
        description = f"{channel.mention} has been set to partnership channel."
    )
    roleSelect = get(ctx.guild.channels, name = 'role-select')
    mbed2 = discord.Embed(
        title = 'Hello there!',
        color = discord.Color(0xe3a2fc),
        description = f'Hello, if youre tired of getting notifications from this channel, go to {roleSelect.mention} and get the No Partnership Ping Role.'
    )
    if ctx.author.guild_permissions.administrator:
        await ctx.send(embed=mbed)
        while True:
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)


@client.command()
async def announce(ctx, channel:discord.TextChannel, *, message):
    mbed = discord.Embed(
        description = f"{message}",
        color = discord.Color(0xe3a2fc)
    )
    if ctx.author.guild_permissions.administrator:
        await channel.send(embed=mbed)

@client.event
async def on_member_join(member):
    channel = get(member.guild.channels, name = 'welcome') 
    mbed = discord.Embed(
        title = 'Welcome',
        description = f'Hello {member.mention}, welcome to TSUKI!',
        color = discord.Color(0xe3a2fc)
    )
    await channel.send(embed = mbed)


client.run('NzMyNjU0NTgyMDg5NTE1MDA5.Xw3vwA.1csUvA74TVIT9bxvigUUXsQ5ET4')
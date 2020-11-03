from discord.ext import commands
import discord
from asyncio import sleep 
from discord.utils import get
import tracemalloc
intents = discord.Intents.all()
client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('p!'), help_comamnd = None, intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'{len(client.users)} users in discord.gg/HWNKQkw!'))

@client.command()
async def info(ctx):
    mbed  = discord.Embed(
        color = discord.Color(0xe3a2fc),
        title = 'Polaroid',
        description = '***p!loop <channel> (partnership reminder), p!announce <channel> <message>***',
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
            await sleep(60*600)


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
    channel2 = get(member.guild.channels, name = 'rules')
    mbed = discord.Embed(
        title = 'Welcome',
        description = f'Hello {member.mention}, welcome to Polaroid! Please head over to {channel2.mention} to verify yourself.',
        color = discord.Color(0xe3a2fc)
    )
    mbed.set_image(url = 'https://cdn.discordapp.com/avatars/732654582089515009/8506972331cc82af0b5ef4d6f2dff59b.webp?size=1024')
    await channel.send(embed = mbed)


client.run('NzMyNjU0NTgyMDg5NTE1MDA5.Xw3vwA.1csUvA74TVIT9bxvigUUXsQ5ET4')

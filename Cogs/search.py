import discord
import os
import aiohttp
from discord.ext import commands

class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pixabay = os.getenv("PIXABAY")



def setup(bot):
    bot.add_cog(search(bot))
import discord
from discord.ext import commands
from PIL import ImageFilters

class supportserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(supportserver(bot))

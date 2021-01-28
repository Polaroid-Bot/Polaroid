import discord
from discord.ext import commands
from PIL import ImageFilter

class filters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(filters(bot))

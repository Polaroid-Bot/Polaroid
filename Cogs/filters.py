import discord
from discord.ext import commands
from PIL import ImageFilter
from PIL import Image
from discord.ext.commands import BucketType
from io import BytesIO
import requests

class filters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=2, type=BucketType.user)
    async def blur(self, ctx, url: str):
        


def setup(bot):
    bot.add_cog(filters(bot))

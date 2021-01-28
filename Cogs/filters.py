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
        response = requests.get(url)
        img = Image.open(BytesIO(response.content), mode='r')
        im = img.filter(ImageFilter.BLUR)
        b = BytesIO()
        im.save(b, format='PNG')
        byte_im = b.getvalue()
        with open('blur.png','wb')as img:
            img.write(byte_im)
            await ctx.send(file=discord.File("blur.png"))
        os.remove("blur.png")



def setup(bot):
    bot.add_cog(filters(bot))

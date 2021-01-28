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
        img1 = Image.open(BytesIO(response.content), mode='r')
        im = img1.filter(ImageFilter.BLUR)
        b = BytesIO()
        b_im = im.save(b, format='PNG')
        b_val = b.getvalue()
        blurred_image = BytesIO(b_im)
        img2 = Image.open(blurred_image)
        draw = ImageDraw.Draw(img2)
        await ctx.send(blur)


def setup(bot):
    bot.add_cog(filters(bot))

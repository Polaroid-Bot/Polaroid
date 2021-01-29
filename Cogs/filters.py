import os
import discord
from discord.ext import commands
from PIL import ImageFilter
from PIL import Image
from discord.ext.commands import BucketType
from io import BytesIO
import requests
import random

err_color = discord.Color.red()
colors = [0xe3a2fc, 0x0da2ff]

class filters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def blur(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            response = requests.get(url)
            img = Image.open(BytesIO(response.content), mode='r')
            try:
                img.seek(1)
            except EOFError:
                isanimated = False
            else:
                isanimated = True

            if isanimated == True:
                await ctx.send(embed=discord.Embed(description='Animated Pictures are currently not supported for the blur filter!', color=random.choice(colors)))

            elif isanimated == False:
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

    @commands.command(aliases=['rb'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def rainbow(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={url}")
            await ctx.send(embed=mbed)

    @commands.command(aliases=['in'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def invert(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/invert?avatar={url}")
            await ctx.send(embed=mbed)

    @invert.error
    async def rb_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/invert?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text='Orthodoxed Syntax: p!in <image link>')
            await ctx.send(embed=mbed)

    @rainbow.error
    async def rb_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text='Orthodoxed Syntax: p!rb <image link>')
            await ctx.send(embed=mbed)

    @blur.error
    async def blur_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            response = requests.get(ctx.author.avatar_url)
            img = Image.open(BytesIO(response.content), mode='r')
            try:
                img.seek(1)
            except EOFError:
                isanimated = False
            else:
                isanimated = True

            if isanimated == True:
                await ctx.send(embed=discord.Embed(color=err_color, description='Your pfp may be a gif! You may also use p!blur <image link>'))

            elif isanimated == False:
                response = requests.get(ctx.author.avatar_url)
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

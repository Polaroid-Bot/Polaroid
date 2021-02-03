import os
import discord
from discord.ext import commands
from PIL import ImageFilter
from PIL import Image
from PIL import ImageOps
from discord.ext.commands import BucketType
from io import BytesIO
import aiohttp
import random


err_color = discord.Color.red()
colors = [0xe3a2fc, 0x0da2ff]

class filters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['blurpify', 'blurple'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def blurp(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            async with aiohttp.ClientSession as ses:
                endpoint = f'https://nekobot.xyz/api/imagegen?type=blurpify&image={url}'
                async with ses.get(endpoint) as r:
                    data = await r.json()
                    mbed = discord.Embed(
                        title='Snap!',
                        color=random.choice(colors)
                    )
                    mbed.set_image(url=data['message'])
                    mbed.set_footer(text=f'Blurple Filter | Requested by {ctx.author}')
                    await ctx.send(embed=mbed)
                    await ses.close()

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
            mbed.set_footer(text=f'Rainbow Filter | Requested by {ctx.author}')
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
            mbed.set_footer(text=f'Invert Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @commands.command(aliases=['gryscl'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def greyscale(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/greyscale?avatar={url}")
            mbed.set_footer(text=f'Greyscale Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @commands.command(aliases=['sep'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def sepia(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/sepia?avatar={url}")
            mbed.set_footer(text=f'Sepia Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def glass(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/glass?avatar={url}")
            mbed.set_footer(text=f'Glass Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @glass.error
    async def glass_error(self, ctx, error):
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
            mbed.set_image(url=f"https://some-random-api.ml/canvas/glass?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Orthodoxed Syntax: p!glass <image link> | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @sepia.error
    async def sep_error(self, ctx, error):
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
            mbed.set_image(url=f"https://some-random-api.ml/canvas/sepia?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Syntax: p!sepia <image link> | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @greyscale.error
    async def gryscl_error(self, ctx, error):
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
            mbed.set_image(url=f"https://some-random-api.ml/canvas/greyscale?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Syntax: p!gryscl <image link> | Requested by {ctx.author}')
            await ctx.send(embed=mbed)

    @invert.error
    async def in_error(self, ctx, error):
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
            mbed.set_footer(text=f'Syntax: p!in <image link> | Requested by {ctx.author}')
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
            mbed.set_footer(text=f'Syntax: p!rb <image link> | Requested By {ctx.author}')
            await ctx.send(embed=mbed)

    @blurp.error
    async def blurp_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with aiohttp.ClientSession as ses:
                async with ses.get(f'https://nekobot.xyz/api/imagegen?type=blurpify&image={ctx.author.avatar_url}') as r:
                    data = await r.json()
                    mbed = discord.Embed(
                        title='Snap!',
                        color=random.choice(colors)
                    )
                    mbed.set_image(url=data['message'])
                    mbed.set_footer(text=f'Blurple Filter | Requested by {ctx.author}')
                    await ctx.send(embed=mbed)
                    await ses.close()


def setup(bot):
    bot.add_cog(filters(bot))

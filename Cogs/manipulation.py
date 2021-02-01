from discord.ext import commands
import discord
import random
from discord.ext.commands import BucketType

err_color = discord.Color.red()
colors = [0xe3a2fc, 0x0da2ff]

class manipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def wasted(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={url}")
            mbed.set_footer(text='Wasted | Requested By {ctx.author}')
            await ctx.send(embed=mbed)

    @commands.command(aliases=['bright'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def brighten(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/brightness?avatar={url}")
            mbed.set_footer(text=f'70% Brightened | Requested By {ctx.author}')
            await ctx.send(embed=mbed)
            
    @commands.command(aliases=['bright'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def brighten(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=random.choice(colors)
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/brightness?avatar={url}")
            mbed.set_footer(text=f'100% Brightened | Requested By {ctx.author}')
            await ctx.send(embed=mbed)

    @brighten.error
    async def bright_error(self, ctx, error):
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
            mbed.set_image(url=f"https://some-random-api.ml/canvas/brightness?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Syntax: p!brighten <image link> | Requested By {ctx.author}')
            await ctx.send(embed=mbed)

    @wasted.error
    async def w_error(self, ctx, error):
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
            mbed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Syntax: p!wasted <image link> | Requested By {ctx.author}')
            await ctx.send(embed=mbed)


def setup(bot):
    bot.add_cog(manipulation(bot))

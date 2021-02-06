from discord.ext import commands
import discord
import random
from discord.ext.commands import BucketType
import aiohttp
import aiofile
from io import BytesIO
from PIL import Image
import os
import asyncio

err_color = discord.Color.red()
color = 0x0da2ff

class manipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ses = bot.aiohttp_session

    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def wasted(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={url}")
            mbed.set_footer(text=f'Wasted Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

    @commands.command(aliases=['rtt'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def rotate(self, ctx, url: str, degrees: int):
        async with self.ses.get(url) as r:
            if r.status in range(200, 299):
                im = Image.open(BytesIO(await r.read()), mode='r')
                im_rtt = im.rotate(angle=degrees)
                b = BytesIO()
                im_rtt.save(b, 'PNG')
                b_im = b.getvalue()
                file = discord.File(filename='rotated.png', fp=BytesIO(b_im))
                mbed = discord.Embed(
                    title = f'Snap! | Rotated the image by {degrees}° counter clockwise.',
                    color=color
                )
                mbed.set_image(url='attachment://rotated.png')
                await ctx.send(embed=mbed, file=file)
            else:
                await ctx.send(embed=discord.Embed(description=f'<:error:806619029044723722> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))

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
                color=0xfffac4
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/sepia?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Wasted Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

        @rotate.error
        async def rtt_error(self, ctx, error):
            if isinstance(error, commands.CommandOnCooldown):
                errembed = discord.Embed(
                    title='Hold on there, buddy',
                    color=err_color,
                    description='Wait 3 more seconds before you can get another snap!'
                )
                await ctx.send(embed=errembed)

            elif isinstance(error, commands.MissingRequiredArgument):
                async with self.ses.get(ctx.author.avatar_url) as r:
                    if r.status in range(200, 299):
                        im = Image.open(BytesIO(await r.read()), mode='r')
                        im_rtt = im.rotate(angle=180)
                        b = BytesIO()
                        im_rtt.save(b, 'PNG')
                        b_im = b.getvalue()
                        file = discord.File(filename='rotated.png', fp=BytesIO(b_im))
                        mbed = discord.Embed(
                            title = f'Snap! | Rotated the image by {degrees}° counter clockwise.',
                            color=color
                        )
                        mbed.set_image(url='attachment://rotated.png')
                        await ctx.send(embed=mbed, file=file)
                    else:
                        await ctx.send(embed=discord.Embed(description=f'<:error:806619029044723722> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))


def setup(bot):
    bot.add_cog(manipulation(bot))

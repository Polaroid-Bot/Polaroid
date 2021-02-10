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
from asyncdagpi import Client, ImageFeatures
from dotenv import load_dotenv

err_color = discord.Color.red()
color = 0x0da2ff

class manipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ses = bot.aiohttp_session
        token = os.getenv("DAGPI")
        self.dagpi = Client(token)
    
    ## FUN COMMANDS

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


    ## IMAGE EDITING AND PROCESSING

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
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))

    @commands.group(aliases=['rs'])
    async def resize(self, ctx, url: str, width: int, height: int):
        async with self.ses.get(url) as r:
            if r.status in range(200, 299):
                im = Image.open(BytesIO(await r.read()), mode='r')
                im_res = im.resize((width, height))
                b = BytesIO()
                im_res.save(b, 'PNG')
                b_im = b.getvalue()
                file = discord.File(filename='resized.png', fp=BytesIO(b_im))
                mbed = discord.Embed(
                    title = f'Snap! | Image resized to {width}x{height}',
                    color=color
                )
                mbed.set_image(url='attachment://resized.png')
                await ctx.send(embed=mbed, file=file)
            else:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))



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
            author = ctx.author
            img = await self.dagpi.image_process(ImageFeatures.wasted(), str(author.avatar_url))
            file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://wasted.{img.format}")
            mbed.set_footer(text='Syntax: p! wasted <image link>')
            await ctx.send(embed=mbed, file=file)

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
            await ctx.send(embed=discord.Embed(description='Syntax: p! rtt <image url> <degrees>'))

def setup(bot):
    bot.add_cog(manipulation(bot))

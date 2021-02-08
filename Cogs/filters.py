import os
import discord
from discord.ext import commands
from PIL import ImageFilter
from PIL import Image, ImageFilter
from PIL import ImageOps
from discord.ext.commands import BucketType
from io import BytesIO
import aiohttp
import random
import requests
import asyncio
import PIL

err_color = discord.Color.red()
color = 0x0da2ff

class filters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ses = bot.aiohttp_session


    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def blur(self, ctx, url: str):
        async with self.ses.get(url) as r:
            try:
                if r.status in range(200, 299):
                    im = Image.open(BytesIO(await r.read()), mode='r')
                    im_blur = im.filter(filter=ImageFilter.BLUR)
                    b = BytesIO()
                    im_blur.save(b, 'PNG')
                    b_im = b.getvalue()
                    file = discord.File(filename='blurred.png', fp=BytesIO(b_im))
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url='attachment://blurred.png')
                    mbed.set_footer(text=f'Blur Filter | Requested by {ctx.author}')
                    await ctx.send(embed=mbed, file=file)
                else:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))
            except:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> File size may be too big/pfp is a Gif.', color=color))

    @commands.command(aliases=['blurpify', 'blurple'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def blurp(self, ctx, url: str):
        async with self.ses.get(f'https://nekobot.xyz/api/imagegen?type=blurpify&image={url}') as r:
            if r.status in range(200, 299):
                data = await r.json()
                url = data['message']
                mbed = discord.Embed(
                    title='Snap',
                    color=color
                )
                mbed.set_image(url=url)
                mbed.set_footer(text=f'Blurple | Requested By {ctx.author}')
                await ctx.send(embed=mbed)
            else:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))

    @commands.command(aliases=['rb'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def rainbow(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=0xffcba4
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/gay?avatar={url}")
            mbed.set_footer(text=f'Rainbow Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description=(description='<:error:806618798768652318> Please pass in a proper url.', color=color))


    @commands.command(aliases=['in'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def invert(self, ctx, url: str):
        async with self.ses.get(url) as r:
            try:
                if r.status in range(200, 299):
                    im = Image.open(BytesIO(await r.read()), mode='r')
                    im_inv = ImageOps.invert(im)
                    b = BytesIO()
                    im_inv.save(b, 'PNG')
                    b_im = b.getvalue()
                    file = discord.File(filename='inverted.png', fp=BytesIO(b_im))
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url='attachment://inverted.png')
                    mbed.set_footer(text=f'Inverted Filter | Requested by {ctx.author}')
                    await ctx.send(embed=mbed, file=file)
                else:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))
            except:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> File size may be too big/pfp is a Gif.', color=color))

    @commands.command(aliases=['gryscl'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def greyscale(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=0x616161
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/greyscale?avatar={url}")
            mbed.set_footer(text=f'Greyscale Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

    @commands.command(aliases=['sep'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def sepia(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=0xfffac4
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/sepia?avatar={url}")
            mbed.set_footer(text=f'Sepia Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def glass(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/glass?avatar={url}")
            mbed.set_footer(text=f'Glass Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

    @commands.command(aliases=['bright'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def brighten(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=0xffff
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/brightness?avatar={url}")
            mbed.set_footer(text=f'70% Brightened | Requested By {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

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
                color=0xffff
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/brightness?avatar={ctx.author.avatar_url}")
            mbed.set_footer(text=f'Syntax: p!brighten <image link> | Requested By {ctx.author}')
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
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                try:
                    if r.status in range(200, 299):
                        im = Image.open(BytesIO(await r.read()), mode='r')
                        im_blur = im.filter(filter=ImageFilter.BLUR)
                        b = BytesIO()
                        im_blur.save(b, 'PNG')
                        b_im = b.getvalue()
                        file = discord.File(filename='blurred.png', fp=BytesIO(b_im))
                        mbed = discord.Embed(
                            title='Snap!',
                            color=color
                        )
                        mbed.set_image(url='attachment://blurred.png')
                        mbed.set_footer(text=f'Blur Filter | Requested by {ctx.author}')
                        await ctx.send(embed=mbed, file=file)
                    else:
                        await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))
                except:
                    await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> File size may be too big/pfp is a Gif.', color=color))

    @invert.error
    async def invert_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                try:
                    if r.status in range(200, 299):
                        im = Image.open(BytesIO(await r.read()), mode='r')
                        im_blur = ImageOps.invert(im)
                        b = BytesIO()
                        im_blur.save(b, 'PNG')
                        b_im = b.getvalue()
                        file = discord.File(filename='inverted.png', fp=BytesIO(b_im))
                        mbed = discord.Embed(
                            title='Snap!',
                            color=color
                        )
                        mbed.set_image(url='attachment://inverted.png')
                        mbed.set_footer(text=f'Invert Filter | Requested by {ctx.author}')
                        await ctx.send(embed=mbed, file=file)
                    else:
                        await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))
                except:
                    await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> File size may be too big/pfp is a Gif.', color=color))

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
                color=color
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
                color=0xfffac4
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
                color=0x616161
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
            async with self.ses.get(ctx.author.avatar_url) as r:
                if r.status in range(200, 299):
                    im = Image.open(BytesIO(await r.read()), mode='r')
                    im_inv = ImageOps.invert(im)
                    b = BytesIO()
                    im_inv.save(b, 'PNG')
                    b_im = b.getvalue()
                    file = discord.File(filename='inverted.png', fp=BytesIO(b_im))
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url='attachment://inverted.png')
                    mbed.set_footer(text=f'Inverted Filter | Requested by {ctx.author}')
                    await ctx.send(embed=mbed, file=file)
                else:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))


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
                color=0xffcba4
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
            async with self.ses.get(f'https://nekobot.xyz/api/imagegen?type=blurpify&image={ctx.author.avatar_url}') as r:
                if r.status in range(200, 299):
                    data = await r.json()
                    url = data['message']
                    mbed = discord.Embed(
                        title='Snap',
                        color=color
                    )
                    mbed.set_image(url=url)
                    mbed.set_footer(text=f'Blurple | Requested By {ctx.author}')
                    await ctx.send(embed=mbed)
                else:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Your pfp may be a gif. | {r.status} response.', color=color))



def setup(bot):
    bot.add_cog(filters(bot))

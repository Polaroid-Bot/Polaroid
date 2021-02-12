import os
import discord
from discord.ext import commands
from PIL import Image, ImageFilter
from discord.ext.commands import BucketType
from io import BytesIO
from asyncdagpi import Client, ImageFeatures

from dotenv import load_dotenv
err_color = discord.Color.red()
color = 0x0da2ff


class filters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ses = bot.aiohttp_session
        token = os.getenv("DAGPI")
        self.dagpi = Client(token)

    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def magik(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.magik(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://magik.{img.format}")
            mbed.set_footer(text=f'Magik | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"magik.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))


    @commands.command(aliases=['polaroid', 'plrd', 'frame'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def snap(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.polaroid(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://polaroid.{img.format}")
            mbed.set_footer(text=f'Polaroid Filter | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"polaroid.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

    @commands.command(aliases=['poster'])
    async def posterize(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.poster(), url)
            file = discord.File(fp=img.image, filename=f"posterized.{img.format}")
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://posterized.{img.format}")
            mbed.set_footer(text=f'Posterized | Requested by {ctx.author} ')
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

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
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> File size may be too big/is a Gif.', color=color))

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
                data = await r.json()
                msg = data['message']
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | Resonse: {r.status} -> {msg}.', color=color))

    @commands.command(aliases=['rb'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def rainbow(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.gay(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=err_color
            )
            mbed.set_image(url=f"attachment://rainbow.{img.format}")
            mbed.set_footer(text=f'Rainbow Filter | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"rainbow.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))


    @commands.command(aliases=['in'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def invert(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.invert(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=0x39ff14
            )
            mbed.set_image(url=f"attachment://inverted.{img.format}")
            mbed.set_footer(text=f'Inverted Filter | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"inverted.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

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
        try:
            img = await self.dagpi.image_process(ImageFeatures.sepia(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=0xfffac4
            )
            mbed.set_image(url=f"attachment://sepia.{img.format}")
            mbed.set_footer(text=f'Sepia Filter | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"sepia.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

    @commands.command(aliases=['shatter'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def glass(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.shatter(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://shattered.{img.format}")
            mbed.set_footer(text=f'Inverted Filter | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"shattered.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

    @commands.command(aliases=['oil'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def oilify(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.paint(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=0xf8de7e
            )
            mbed.set_image(url=f"attachment://oil.{img.format}")
            mbed.set_footer(text=f'Oil Painting Filter | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"oil.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

    @commands.command(aliases=['pixelify', 'pixel'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def pixelate(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.pixel(), url)
            file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://pixel.{img.format}")
            mbed.set_footer(text=f'Pixelated Filter | Requested by {ctx.author}')
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))


    @snap.error
    async def snap_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            url = f"{ctx.author.avatar_url}"
            try:
                img = await self.dagpi.image_process(ImageFeatures.polaroid(), url)
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://polaroid.{img.format}")
                mbed.set_footer(text=f'Polaroid Filter | Requested by {ctx.author}')
                file = discord.File(fp=img.image, filename=f"polaroid.{img.format}")
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))


    @pixelate.error
    async def pixel_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            url = str(ctx.author.avatar_url)
            try:
                img = await self.dagpi.image_process(ImageFeatures.pixel(), url)
                file = discord.File(fp=img.image, filename=f"pixel.{img.format}")
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://pixel.{img.format}")
                mbed.set_footer(text='Syntax: p! pixel <image link> | Quality may be bad. Specify url if this is the case.')
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> Error when making request.', color=color))


    @posterize.error
    async def poster_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            url = str(ctx.author.avatar_url)
            try:
                img = await self.dagpi.image_process(ImageFeatures.poster(), url)
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://posterized.{img.format}")
                mbed.set_footer(text=f'Syntax: p! posterize <image link> | Quality may be bad. Specify url if this is the case.')
                file = discord.File(fp=img.image, filename=f"posterized.{img.format}")
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

    @oilify.error
    async def oil_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            url = str(ctx.author.avatar_url)
            try:
                img = await self.dagpi.image_process(ImageFeatures.paint(), url)
                file = discord.File(fp=img.image, filename=f"oil.{img.format}")
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://oil.{img.format}")
                mbed.set_footer(text='Syntax: p! oil <image link> | Quality may be bad. Specify url if this is the case.')
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> Error when making request.', color=color))


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
                        mbed.set_footer(text=f'Syntax: p! blur <image link> | Requested by {ctx.author}')
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
            url = f"{ctx.author.avatar_url}"
            try:
                img = await self.dagpi.image_process(ImageFeatures.invert(), url)
                file = discord.File(fp=img.image, filename=f"inverted.{img.format}")
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://inverted.{img.format}")
                mbed.set_footer(text='Syntax: p! inverted <image link> | Quality may not be good. Specify url if this is the case.')
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

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
            url = f"{ctx.author.avatar_url}"
            try:
                img = await self.dagpi.image_process(ImageFeatures.shatter(), url)
                file = discord.File(fp=img.image, filename=f"shattered.{img.format}")
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://shattered.{img.format}")
                mbed.set_footer(text=f'Shattered Glass Filter | Requested by {ctx.author}')
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

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
            url = f"{ctx.author.avatar_url}"
            try:
                img = await self.dagpi.image_process(ImageFeatures.sepia(), url)
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://sepia.{img.format}")
                mbed.set_footer(text=f'Sepia Filter | Requested by {ctx.author}')
                file = discord.File(fp=img.image, filename=f"sepia.{img.format}")
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

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
            url = str(ctx.author.avatar_url_as(format="png"))
            mbed = discord.Embed(
                title='Snap!',
                color=0x616161
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/greyscale?avatar={url}")
            mbed.set_footer(text=f'Syntax: p! gryscl <image link> | Requested by {ctx.author}')
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
            url = f"{ctx.author.avatar_url}"
            try:
                img = await self.dagpi.image_process(ImageFeatures.rainbow(), url)
                file = discord.File(fp=img.image, filename=f"inverted.{img.format}")
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://inverted.{img.format}")
                mbed.set_footer(text='Syntax: p! in <image link>')
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))


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
            url = f"{ctx.author.avatar_url}"
            try:
                img = await self.dagpi.image_process(ImageFeatures.gay(), url)
                file = discord.File(fp=img.image, filename=f"rainbow.{img.format}")
                mbed = discord.Embed(
                    title='Snap!',
                    color=color
                )
                mbed.set_image(url=f"attachment://rainbow.{img.format}")
                mbed.set_footer(text='Syntax: p! rb <image link>')
                await ctx.send(embed=mbed, file=file)
            except:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))


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
                    mbed.set_footer(text=f'Syntax: p! blurp <image link> | Requested By {ctx.author}')
                    await ctx.send(embed=mbed)
                else:
                    data = await r.json()
                    msg = data['message']
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Your pfp may be a gif. | Resonse: {r.status} -> {msg}.', color=color))



def setup(bot):
    bot.add_cog(filters(bot))

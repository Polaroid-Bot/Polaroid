from discord.ext import commands
import discord
from discord.ext.commands import BucketType
from io import BytesIO
from PIL import Image
import os
from asyncdagpi import Client, ImageFeatures

err_color = discord.Color.red()
color = 0x0da2ff

class manipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ses = bot.aiohttp_session
        self.dag_token = os.getenv("DAGPI")
        self.dagpi = Client(self.dag_token)
    
    ## FUN COMMANDS


    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def wasted(self, ctx, url: str):
        http = 'https://', 'http://'
        if url.startswith(http):
            mbed = discord.Embed(
                title='Snap!',
                color=err_color
            )
            mbed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={url}")
            mbed.set_footer(text=f'Wasted | Requested by {ctx.author}')
            await ctx.send(embed=mbed)
        else:
            await ctx.send(embed=discord.Embed(description='Please pass in a proper url.', color=color))

    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def swirl(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.swirl(), url)
            mbed = discord.Embed(
                title='Snap!',
                color=color
            )
            mbed.set_image(url=f"attachment://swirled.{img.format}")
            mbed.set_footer(text=f'Swirl | Requested by {ctx.author}')
            file = discord.File(fp=img.image, filename=f"swirled.{img.format}")
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request. | Image may be a WEBP file', color=color))


    @commands.command(aliases=['fiveguysonegirl', '5g1g'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def fiveg1g(self, ctx, url1: str, url2: str):
        async with self.ses.get(f'https://api.dagpi.xyz/image/5g1g/?url={url1}&url2={url2}', headers={'Authorization': self.dag_token}) as r:
            if r.status in range(200, 299):
                img = Image.open(BytesIO(await r.read()), mode='r')
                b = BytesIO()
                img.save(b, format=f'{img.format}')
                b_im = b.getvalue()
                file = discord.File(filename=f'5g1g.{img.format}', fp=BytesIO(b_im))
                mbed = discord.Embed(
                    title='Snap',
                    color=color
                )
                mbed.set_image(url=f'attachment://5g1g.{img.format}')
                mbed.set_footer(text=f'Five Guys One Girl | Requested by {ctx.author}')
                await ctx.send(embed=mbed, file=file)
            else:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! | Response: {r.status}.', color=color))

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
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request. | Image may be a WEBP file', color=color))


    @commands.command()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def triggered(self, ctx, url: str):
        try:
            img = await self.dagpi.image_process(ImageFeatures.triggered(), url)
            file = discord.File(fp=img.image, filename=f"triggered.{img.format}")
            mbed = discord.Embed(
                title='Snap!',
                color=err_color
            )
            mbed.set_image(url=f"attachment://triggered.{img.format}")
            mbed.set_footer(text=f'Triggered | Requested by {ctx.author}')
            await ctx.send(embed=mbed, file=file)
        except:
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request. | Image may be a WEBP file', color=color))

    @magik.error
    async def magik_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))

                try:
                    img = await self.dagpi.image_process(ImageFeatures.magik(), url)
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url=f"attachment://magik.{img.format}")
                    mbed.set_footer(text=f'Syntax: p! magik <image link> | Quality may be bad. Specify url if this is the case.')
                    file = discord.File(fp=img.image, filename=f"magik.{img.format}")
                    await ctx.send(embed=mbed, file=file)
                except:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request.', color=color))

    @fiveg1g.error
    async def fiveg1g_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))

                async with self.ses.get(f'https://api.dagpi.xyz/image/5g1g/?url={url}&url2={url}', headers={'Authorization': self.dag_token}) as r:
                    if r.status in range(200, 299):
                        img = Image.open(BytesIO(await r.read()), mode='r')
                        b = BytesIO()
                        img.save(b, format=f'{img.format}')
                        b_im = b.getvalue()
                        file = discord.File(filename=f'5g1g.{img.format}', fp=BytesIO(b_im))
                        mbed = discord.Embed(
                            title='Snap',
                            color=color
                        )
                        mbed.set_image(url=f'attachment://5g1g.{img.format}')
                        mbed.set_footer(text=f'Five Of You, One Of You | Syntax: p! 5g1g <guy> <girl>')
                        await ctx.send(embed=mbed, file=file)
                    else:
                        await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! | Response: {r.status}.', color=color))

    @swirl.error
    async def swirl_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))

                try:
                    img = await self.dagpi.image_process(ImageFeatures.swirl(), url)
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url=f"attachment://swirled.{img.format}")
                    mbed.set_footer(text=f'Swirl | Requested by {ctx.author}')
                    file = discord.File(fp=img.image, filename=f"swirled.{img.format}")
                    await ctx.send(embed=mbed, file=file)
                except:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request. | Image may be a WEBP file', color=color))


    @triggered.error
    async def triggered_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))
                try:
                    img = await self.dagpi.image_process(ImageFeatures.triggered(), url)
                    file = discord.File(fp=img.image, filename=f"triggered.{img.format}")
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url=f"attachment://triggered.{img.format}")
                    mbed.set_footer(text='Syntax: p! triggered <image link> | Quality may not be good. Specify url if this is the case.')
                    await ctx.send(embed=mbed, file=file)
                except:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request. | Image may be a WEBP file', color=color))


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
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))

                try:
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color
                    )
                    mbed.set_image(url=f"https://some-random-api.ml/canvas/wasted?avatar={url}")
                    mbed.set_footer(text=f'Wasted | Requested by {ctx.author}')
                    await ctx.send(embed=mbed)
                except:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Error when making request. | Image may be a WEBP file', color=color))


    ## IMAGE EDITING AND PROCESSING


    @commands.command(aliases=['jpeg', 'jpegify'])
    async def tojpeg(self, ctx, url: str):
        async with self.ses.get(url) as r:
            if r.status in range(200, 299):
                img = Image.open(BytesIO(await r.read()), mode='r')
                b = BytesIO()
                img.save(b, format=f'{img.format}')
                file = discord.File(filename='tojpeg.jpeg', fp=BytesIO(b.getvalue()))
                mbed = discord.Embed(
                    title='Snap! | Converted to JPEG Format',
                    color=color
                )
                mbed.set_image(url='attachment://tojpeg.jpeg')
                await ctx.send(embed=mbed, file=file)
            else:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> Error when making request.', color=err_color))

    @commands.command(aliases=['png', 'pngify'])
    async def topng(self, ctx, url: str):
        async with self.ses.get(url) as r:
            if r.status in range(200, 299):
                img = Image.open(BytesIO(await r.read()), mode='r')
                b = BytesIO()
                img.save(b, format=f'{img.format}')
                file = discord.File(filename='topng.png', fp=BytesIO(b.getvalue()))
                mbed = discord.Embed(
                    title='Snap! | Converted to PNG Format',
                    color=color
                )
                mbed.set_image(url='attachment://topng.png')
                await ctx.send(embed=mbed, file=file)
            else:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> Error when making request.', color=err_color))

    @commands.group(aliases=['rs'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
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
                    title=f'Snap! | Image resized to {width}x{height}',
                    color=color
                )
                mbed.set_image(url='attachment://resized.png')
                await ctx.send(embed=mbed, file=file)
            else:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))

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

    @tojpeg.error
    async def jpeg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            try:
                mbed = discord.Embed(
                    title='Snap! | Converted to JPEG Format',
                    color=color
                )
                mbed.set_image(url=str(ctx.author.avatar_url_as(format='jpeg')))
                mbed.set_footer('Syntax: p! tojpeg <image link>')
                await ctx.send(embed=mbed)
            except:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> Error during conversion process.', color=err_color))

    @topng.error
    async def png_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            try:
                mbed = discord.Embed(
                    title='Snap! | Converted to PNG Format',
                    color=color
                )
                mbed.set_image(url=str(ctx.author.avatar_url_as(format='png')))
                mbed.set_footer('Syntax: p! topng <image link>')
                await ctx.send(embed=mbed)
            except:
                await ctx.send(embed=discord.Embed(description='<:error:806618798768652318> Error during conversion process.', color=err_color))

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
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))

                async with self.ses.get(url) as r:
                    if r.status in range(200, 299):
                        im = Image.open(BytesIO(await r.read()), mode='r')
                        im_rtt = im.rotate(angle=180)
                        b = BytesIO()
                        im_rtt.save(b, 'PNG')
                        b_im = b.getvalue()
                        file = discord.File(filename='rotated.png', fp=BytesIO(b_im))
                        mbed = discord.Embed(
                            title=f'Snap! | Automatically rotated by 180°',
                            color=color
                        )
                        mbed.set_image(url='attachment://rotated.png')
                        mbed.set_footer(text='Syntax: p! rtt <image link> <degrees>')
                        await ctx.send(embed=mbed, file=file)
                    else:
                        await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))

    @resize.error
    async def rs_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            async with self.ses.get(str(ctx.author.avatar_url)) as r:
                img = Image.open(BytesIO(await r.read()), mode='r')
                try:
                    img.seek(1)
                    url = str(ctx.author.avatar_url_as(format=f'gif'))
                except EOFError:
                    url = str(ctx.author.avatar_url_as(format=f'png'))

                async with self.ses.get(url) as r:
                    if r.status in range(200, 299):
                        im = Image.open(BytesIO(await r.read()), mode='r')
                        im_res = im.resize((500, 500))
                        b = BytesIO()
                        im_res.save(b, 'PNG')
                        b_im = b.getvalue()
                        file = discord.File(filename='resized.png', fp=BytesIO(b_im))
                        mbed = discord.Embed(
                            title=f'Snap! | Automatically resized to 500x500',
                            color=color
                        )
                        mbed.set_image(url='attachment://resized.png')
                        await ctx.send(embed=mbed, file=file)
                    else:
                        await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! Image may be a gif. | {r.status} response.', color=color))


def setup(bot):
    bot.add_cog(manipulation(bot))

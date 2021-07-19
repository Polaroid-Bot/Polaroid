import aiohttp
from io import BytesIO
import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from PIL import Image

color = 0x0da2ff

class emojis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ses = bot.aiohttp_session


    @commands.command(aliases=['ce', 'crem'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def cremoji(self, ctx, url: str, *, name):
        guild = ctx.guild
        if ctx.author.guild_permissions.manage_emojis:
            async with self.ses.get(url) as r:
                try:
                    if r.status in range(200, 299):
                        img = BytesIO(await r.read())
                        b_im = img.getvalue()
                        emoji = await guild.create_custom_emoji(image=b_im, name=name)
                        pil_img = Image.open(img, mode='r')
                        try:
                           pil_img.seek(1) 
                        except EOFError:
                            await ctx.send(embed=discord.Embed(description=f'Successfully Created Emoji: <:{name}:{emoji.id}>', color=color))
                        else:
                            await ctx.send(embed=discord.Embed(description=f'Successfully Created Emoji: <a:{name}:{emoji.id}>', color=color))
                    else:
                        await ctx.send(embed=discord.Embed(description='<:error:866754763482726461> Error when making request. | File size is too big', color=color))
                except discord.HTTPException:
                    await ctx.send(embed=discord.Embed(description='<:error:866754763482726461> File size is too big.', color=color))

    @commands.command(aliases=['de', 'drem'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def delemoji(self, ctx, emoji: discord.Emoji):
        if ctx.author.guild_permissions.manage_emojis:
            await emoji.delete()
            await ctx.send(f'Successfully Deleted Emoji: {emoji}')

    @cremoji.error
    async def ce_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                colour=color,
                description='Wait another 3 seconds before you can create another emoji!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                description='Syntax: -p! ce <image url> <emoji name>',
                color=color
            )
            if ctx.author.guild_permissions.manage_emojis:
                await ctx.send(embed=mbed)

        elif isinstance(error, commands.BotMissingPermissions):
            mbed = discord.Embed(
                title='Missing Required Permissions',
                color=color
            )
            mbed.set_image(url='https://cdn.discordapp.com/attachments/733132099208347698/802652650339565598/unknown.png')
            if ctx.author.guild_permissions.manage_emojis:
                await ctx.send(embed=mbed)

    @delemoji.error
    async def de_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=color,
                description='Wait 3 seconds before trying to delete another emoji!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                description='Syntax p! de <emoji>',
                color=color
            )
            if ctx.author.guild_permissions.manage_emojis:
                await ctx.send(embed=mbed)

        elif isinstance(error, commands.BotMissingPermissions):
            mbed = discord.Embed(
                title='Unable to Snap.',
                color=color
            )
            mbed.set_image(url='https://cdn.discordapp.com/attachments/733132099208347698/802652650339565598/unknown.png')
            if ctx.author.guild_permissions.manage_emojis:
                await ctx.send(embed=mbed)

def setup(bot):
    bot.add_cog(emojis(bot))

from discord.ext import commands
import discord
import random
from discord.ext.commands import BucketType

err_color = discord.Color.red()
colors = [0xe3a2fc, 0x0da2ff]

class extrautils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pfp', 'av'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def avatar(self, ctx, user: discord.User):
        mbed = discord.Embed(
            title=f"{user}'s avatar",
            color=random.choice(colors)
        )
        mbed.set_author(name=f'{user.name} | Requested by {ctx.author.mention}', icon_url=f'{user.avatar_url}')
        mbed.url = f'{user.avatar_url}'
        mbed.set_image(url=f"{user.avatar_url}")
        await ctx.send(embed=mbed)

    @avatar.error
    async def av_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                title=f"{ctx.author}'s avatar",
                color=random.choice(colors)
            )
            mbed.url = f'{ctx.author.avatar_url}'
            mbed.set_author(name=f'{ctx.author.name} | Requested by {ctx.author.mention}', icon_url=f'{user.avatar_url}')
            mbed.set_image(url=f"{ctx.author.avatar_url}")
            mbed.set_footer(text=f'Syntax: p!av <image link>')
            await ctx.send(embed=mbed)

def setup(bot):
    bot.add_cog(extrautils(bot))

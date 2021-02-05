from discord.ext import commands
import discord
import random
from discord.ext.commands import BucketType

err_color = discord.Color.red()
color = 0x0da2ff

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['h', 'info'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def help(self, ctx):
        mbed = discord.Embed(
            title='Commands | p! or @mention',
            description='Enjoy my list of image related commands. <:camera:804427554688598038>',
            color=color
        )
        mbed.add_field(name='Filters', value='> `p!greyscale <image link>`\n> `p!sepia <image link>`\n> `blurpify <image link>`\n> `rainbow <image link>`\n> `invert <image link>`')
        mbed.add_field(name='Manipulation', value='> `p!wasted <image link>`\n')
        mbed.add_field(name='Extras', value='> `p!avatar <image link>`\n> `p!help`', inline=True)
        await ctx.send(embed=mbed)


    @help.error
    async def hlp_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can recieve another help msg!'
            )
            await ctx.send(embed=errembed)

def setup(bot):
    bot.add_cog(help(bot))

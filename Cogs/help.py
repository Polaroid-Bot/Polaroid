from discord.ext import commands
import discord
import random
from discord.ext.commands import BucketType

err_color = discord.Color.red()
color = 0x0da2ff

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['h', 'info'], invoke_without_command=True)
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def help(self, ctx):
        mbed = discord.Embed(
            title='Commands | p! or @mention',
            description='Enjoy my list of image related commands. <:camera:804427554688598038>',
            color=color
        )
        mbed.add_field(name='Images', value='> `p! help images`')
        mbed.add_field(name='Emojis', value='> `p! help emojis`')
        mbed.add_field(name='Extras', value='> `p! avatar <image link>`\n> `p! help <subcommand>`')
        mbed.set_footer(text='Note that many of these commands do not support gifs.')
        await ctx.send(embed=mbed)

    @help.command(aliases=['img', 'image'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def images(self, ctx):
        mbed = discord.Embed(
            title='Image Commands 📸',
            color=color
        )
        mbed.add_field(name='Filters', value='> p! invert <image link> `p! blur <image link>`\n> `p! sepia <image link>`\n> `p! blurpify <image link>`\n> `p! rainbow <image link>`\n> `p! invert <image link>`')
        mbed.add_field(name='Manipulation', value='> `p! resize <image link> <width> <height>`\n> `p! rotate <image link> <degrees>`\n> `p! wasted <image url>`')
        await ctx.send(embed=mbed)

    @help.command(aliases=['emoji', 'em'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def emojis(self, ctx):
        mbed = discord.Embed(
            title='Emoji Commands <a:defaultFurret:807212291279552543>',
            color=color,
            description=f'> `p! cremoji <image link>`\n> `p! delemoji <emoji>`'
        )
        await ctx.send(embed=mbed)


    @images.error
    async def imgs_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can recieve another help message!'
            )
            await ctx.send(embed=errembed)

    @emojis.error
    async def em_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can recieve another help message!'
            )
            await ctx.send(embed=errembed)

    @help.error
    async def hlp_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can recieve another help message!'
            )
            await ctx.send(embed=errembed)

def setup(bot):
    bot.add_cog(help(bot))

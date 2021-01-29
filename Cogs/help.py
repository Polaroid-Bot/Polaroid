from discord.ext import commands
import discord
import random

err_color = discord.Color.red()
colors = [0xe3a2fc, 0x0da2ff]

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['h', 'info'])
	@commands.cooldown(rate=2, per=3, type=BucketType.user)
	async def help(self, ctx):
		mbed = discord.Embed(
			title='Commands | p! or @mention',
			description='Enjoy my list of image related commands. <:camera:804427554688598038>',
            color=random.choice(colors)
		)
		mbed.add_field(name='Manipulation', value='> `blur <image link>`\n> `rainbow <image link>`\n> `invert <image link>`')
		await ctx.send(embed=mbed)

    @help.error
    async def blur_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can recieve another help msg!'
            )
            await ctx.send(embed=errembed)

def setup(bot):
    bot.add_cog(help(bot))

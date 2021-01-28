import discord
from discord.ext import commands


class supportserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(member):
        if member.guild.id == 687177202823069697:
            channel = get(member.guild.channels, name='welcome')
            channel2 = get(member.guild.channels, name='rules')
            mbed = discord.Embed(
                title = 'Welcome',
                description = f'Hello {member.mention}, welcome to Polaroid! Please head over to {channel2.mention} to verify yourself.',
                color = discord.Color(0xe3a2fc)
            )
            mbed.set_image(url = f'{member.guild.icon_url}')
            await channel.send(embed = mbed)

    @commands.command(aliases=['a'])
    async def announce(ctx, channel: discord.TextChannel, *, msg: str):
        if ctx.guild.id == 687177202823069697:
            await channel.send(msg)
            await ctx.send(f'Successfully sent {msg} to {channel.mention}.')

def setup(bot):
    bot.add_cog(supportserver(bot))

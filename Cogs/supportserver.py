import discord
from discord.ext import commands
import random
import time
from datetime import datetime
colors = [0xe3a2fc, 0x0da2ff]

class supportserver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.utcnow()

    @commands.Cog.listener()
    async def on_member_join(self, member):
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
    async def announce(self, ctx, channel: discord.TextChannel, *, msg: str):
        if ctx.guild.id == 687177202823069697:
            if ctx.author.guild_permissions.administrator:
                await channel.send(msg)
                await ctx.send(f'Successfully sent {msg} to {channel.mention}.')

    @commands.command(aliases=['s'])
    async def stats(self, ctx):
        if ctx.guild.id == 687177202823069697:
            if ctx.author.guild_permissions.administrator:
                uptime = datetime.utcnow() - self.bot.launch_time
                hours, remainder = divmod(int(uptime.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)
                days, hours = divmod(hours, 24)
                before = time.monotonic()
                message = await ctx.send('Pinging...')
                ping = (time.monotonic() - before) * 1000
                if ping < 200:
                    color = 0x35fc03
                elif ping < 350:
                    color = 0xe3f51d
                elif ping < 500:
                    color = 0xf7700f
                else:
                    color = 0xf7220f
                pEmbed = discord.Embed(title=f"Member Count: {ctx.guild.member_count}", color=color)
                pEmbed.add_field(name="Latency", value=f'{int(ping)}ms')
                pEmbed.set_author(name=f'Polaroid Stats', icon_url=ctx.guild.icon_url)
                pEmbed.add_field(name="API", value=f'{round(self.bot.latency * 1000)}ms')
                pEmbed.add_field(name="Uptime", value=f"Taking photos for {days}d, {hours}h, {minutes}m")
                pEmbed.set_thumbnail(url=self.bot.user.avatar_url)
                await message.edit(content=None, embed=pEmbed)
                await ctx.send(embed=mbed)

def setup(bot):
    bot.add_cog(supportserver(bot))

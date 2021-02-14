import discord
import os
import aiohttp
from discord.ext import commands
from discord.ext.commands import BucketType

color = 0x0da2ff

class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pixabay = os.getenv("PIXABAY")
        self.ses = bot.aiohttp_session

    @commands.group()
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def search(self, ctx, *, query):
        query = query.replace(' ', '+')
        async with self.ses.get(f"https://pixabay.com/api/?key={self.pixabay}&q={query}&image_type=photo") as r:
            if r.status in range(200, 299):
                try:
                    data = await r.json()
                    image_url = data["hits"][0]["webformatURL"]
                    views = data["hits"][0]["views"]
                    likes = data["hits"][0]["likes"]
                    mbed = discord.Embed(
                        title='Snap!',
                        color=color,
                        description=f'[Link]({image_url})'
                    )
                    mbed.set_image(url=image_url)
                    mbed.set_footer(text=f'👀 Views: {views} 👍 Likes: {likes}')
                    await ctx.send(embed=mbed)
                except IndexError:
                    await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! | Image not found.', color=color))
            else:
                await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Problem while snapping! | Response: {r.status}.', color=color))


    @search.error
    async def search_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Please pass in proper arguments. | Syntax: p! search <query>', color=color))


def setup(bot):
    bot.add_cog(search(bot))
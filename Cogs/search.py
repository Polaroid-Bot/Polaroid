import discord
import os
import aiohttp
from discord.ext import commands
from discord.ext.commands import BucketType
import random

color = 0x0da2ff

class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pixabay = os.getenv("PIXABAY")
        self.ses = bot.aiohttp_session

    @commands.group(invoke_without_command=True)
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def search(self, ctx, *, query):
        query = query.replace(' ', '+')
        page = [1, 2, 3, 4, 5]
        type = ['illustration', 'photo']
        async with self.ses.get(f"https://pixabay.com/api/?key={self.pixabay}&q={query}&image_type={random.choice(type)}&safesearch=true&page={random.choice(page)}") as r:
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

    @search.command(aliases=['image'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def photo(self, ctx, *, query):
        query = query.replace(' ', '+')
        page = [1, 2, 3, 4, 5]
        async with self.ses.get(f"https://pixabay.com/api/?key={self.pixabay}&q={query}&image_type=photo&safesearch=true&page={random.choice(page)}") as r:
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

    @search.command(aliases=['illustration'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def art(self, ctx, *, query):
        query = query.replace(' ', '+')
        page = [1, 2, 3, 4, 5]
        async with self.ses.get(f"https://pixabay.com/api/?key={self.pixabay}&q={query}&image_type=illustration&safesearch=true&page={random.choice(page)}") as r:
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

    @search.command(aliases=['wallpaper'])
    @commands.cooldown(rate=2, per=3, type=BucketType.user)
    async def wall(self, ctx, *, query):
        query = query.replace(' ', '+')
        page = [1, 2, 3, 4, 5]
        type = ['illustration', 'photo']
        async with self.ses.get(f"https://pixabay.com/api/?key={self.pixabay}&q={query}&image_type={random.choice(type)}&safesearch=true&category=backgrounds&page={random.choice(page)}") as r:
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
    
    @search.error()
    async def search_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Please pass in proper arguments. | Syntax: p! search art <query>', color=color))
    
    @photo.error()
    async def photo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Please pass in proper arguments. | Syntax: p! search art <query>', color=color))

    @wall.error()
    async def wall_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Please pass in proper arguments. | Syntax: p! search art <query>', color=color))

    @art.error()
    async def art_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            errembed = discord.Embed(
                title='Hold on there, buddy',
                color=err_color,
                description='Wait 3 more seconds before you can get another snap!'
            )
            await ctx.send(embed=errembed)

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(description=f'<:error:806618798768652318> Please pass in proper arguments. | Syntax: p! search art <query>', color=color))


def setup(bot):
    bot.add_cog(search(bot))

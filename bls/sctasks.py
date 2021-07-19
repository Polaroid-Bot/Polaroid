from discord.ext import commands
import discord
import aiohttp
import asyncio
import dbl
import discordlists
import os

class sctasks(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.dbl_token = os.getenv('DBL')
		self.bfd_token = os.getenv('BFD')
		self.db_token = os.getenv('DB')
		self.dbg_token = os.getenv('DBG')
		self.dblpy = dbl.DBLClient(self.bot, self.db_token, autopost=True)
		self.api = discordlists.Client(self.bot)
		try:
			self.api.set_auth("botsfordiscord.com", self.bfd_token)
			self.api.set_auth("discord.bots.gg", self.dbg_token)
			self.api.set_auth("discordbotlist.com", self.dbl_token)
			self.api.start_loop()
		except:
			pass

def setup(bot):
	bot.add_cog(sctasks(bot))
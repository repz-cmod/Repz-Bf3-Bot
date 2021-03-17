import discord
import os
import random
import glob
from discord.ext import commands
import datetime
import aiohttp


class repz_bf3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="players")
    async def on_players(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://bf3.zloemu.net/servers?id=31197&json') as r:
                js = await r.json(content_type='text/html')
        await ctx.send(js['players'])

def setup(bot):
    bot.add_cog(repz_bf3(bot))


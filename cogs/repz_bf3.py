import discord
from discord.ext import commands
import aiohttp

#base class all cogs inherit from
class repz_bf3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #sends list of players in chat. sends the raw list so it needs formatting
    @commands.command(name="players")
    async def on_players(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://bf3.zloemu.net/servers?id=31197&json') as r:
                js = await r.json(content_type='text/html')
        await ctx.send(js['players'])

        
def setup(bot):
    bot.add_cog(repz_bf3(bot))

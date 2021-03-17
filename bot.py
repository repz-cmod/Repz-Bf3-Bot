import discord
from discord.ext import commands
import aiohttp
import json
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

#uncomment following lines when .env is in directory

#from dotenv import load_dotenv
#import os
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')

#for future ideas. filling your main bot.py with too many event/command handlers makes it harder to oversee
#I have provided a simple cog which makes it easier to add features

#client.load_extension("cogs.repz_bf3")

#as the bot goes online, status of bot changes to server stats.
#ToDo: iterate through the method every 2 seconds so it updates, json request does not work yet. 
@client.event
async def on_ready():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://bf3.zloemu.net/servers?id=31197&json') as r:
            if r.status == 200:
                js = await r.json()
                await client.change_presence(status=discord.Status.idle, activity=discord.Game(js['name']))
            else:
                await ctx.send("This aint supposed to happen")


#store your token in a .env file. Never hardcode tokens into source
#I have provided necessary code above.
client.run()

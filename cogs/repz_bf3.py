import discord
from discord.ext import commands
import aiohttp
from PIL import Image, ImageDraw, ImageFont

class repz_bf3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="bf3stats")
    async def gun_stats(self, ctx, playername):
        #displays ZLO bf3 stats in generated picture
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://bf3.zloemu.net/json?name={playername}') as r:
                js = await r.json(content_type= 'text/html')
        ########################
        #    Image Builder     #
        ########################
        image = Image.open('bf3.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r'path_to\Roboto-Bold.ttf', size=48) 
        ########################
        #       RANK           #
        ########################
        (x,y) = (420, 220) #x = r/l, y = o/u
        message = str(js['rank']['val'])
        color = 'rgb(250,250,250)'
        draw.text((x, y), message, fill=color, font=font)
        ########################
        #       KILLS          #
        ########################
        (x, y) = (1000, 220)  # x = r/l, y = o/u
        message = "KILLS:    " + str(js['c___k_g']['val'])
        color = 'rgb(250,250,250)'
        draw.text((x, y), message, fill=color, font=font)
        ########################
        #       SKILL          #
        ########################
        (x, y) = (1000, 280)  # x = r/l, y = o/u
        message = "SKILL:    " + str(int(js['elo'] ['val']))
        color = 'rgb(250,250,250)'
        draw.text((x, y), message, fill=color, font=font)
        ########################
        #      Saves image     #
        ########################
        image.save('stats.png')
        #to avoid taking up lots of hdd space it deletes old stats.png when command is issued
        await ctx.send(file=discord.File('stats.png'))

    @commands.command(name="players")
    async def on_players(self, ctx):
        #displays stats in embed in chat
        async with aiohttp.ClientSession() as session:
            async with session.get('https://bf3.zloemu.net/servers?id=31197&json') as r:
                js = await r.json(content_type='text/html')
        count = len(js['players'])
        embed=discord.Embed(title="RepZ Bf3 Server Players", color=0x3866f0)
        embed.add_field(name=js['players'], value=f"{str(count)} of 64 players playing", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(repz_bf3(bot))


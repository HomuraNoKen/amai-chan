import asyncio, os, platform, sys
from datetime import datetime
from function import *

# === downloaded from pypl/outside source ===
from discord.ext.commands import Bot
from discord.ext import commands

if not os.path.isfile("config.py"):
    sys.exit("\'config.py\' not found! Please add it and try again.")
else:
    import config

#time_set (might use database to set it instead)
alert_time_day = 8 
alert_time_night = alert_time_day + 12

bot = Bot(command_prefix=config.BOT_PREFIX) 

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" HENTAI. $help"))
    #bot.loop.create_task(time_check())

""" #finish up daily bot 
@bot.event
async def time_check():
    while not bot.is_closed():
        channel = bot.get_channel(config.CHANNEL_ID)

        now = int(datetime.strftime(datetime.now(),'%H'))
        if now == alert_time_day or now == alert_time_night:
            embed = doujin_generate(True)
"""

bot.remove_command("help")

@bot.command()
async def help(ctx):
    embed = help_message()
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('❌')


@bot.command()
async def search(ctx, *, arg):
    embed = doujin_search(arg)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('❌')

bot.run(config.TOKEN)
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

intents = discord.Intents.default() #remove

bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents) #remove : intents=intents

@bot.event
async def on_ready():
    bot.loop.create_task(status_check()) #remove

async def status_check(): #remove
    while True:
        await bot.change_presence(activity=discord.Game("with you!"))
        await asyncio.sleep(60)
        
        await bot.change_presence(activity=discord.Game("with humans!"))
        await asyncio.sleep(60)

bot.remove_command("help")

@bot.command()
async def search(ctx, *, arg):
    embed = doujin_search(arg)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('❌')

bot.run(config.TOKEN)
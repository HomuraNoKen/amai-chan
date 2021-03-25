import asyncio, os, platform, sys
from datetime import datetime
from function import help_message, doujin_search, doujin_generate, message_embed, error_embed, lang, tag
from db import add_channel_id

# === downloaded from pypl/outside source ===
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

from codetiming import Timer #for testing purpose only

if not os.path.isfile("config.py"):
    sys.exit("\'config.py\' not found! Please add it and try again.")
else:
    import config

#time_set (might use database to set it instead)
alert_time_day = 7
alert_time_night = alert_time_day + 12

bot = Bot(command_prefix=config.BOT_PREFIX) 

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    bot.loop.create_task(status_task())
    bot.loop.create_task(time_check())
    

#finish up daily bot 
async def status_task():
	while True:
		await bot.change_presence(activity=discord.Game("with your lust!"))
		await asyncio.sleep(60)
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" HENTAI"))
		await asyncio.sleep(60)
		await bot.change_presence(activity=discord.Game(f"{config.BOT_PREFIX} help"))
		await asyncio.sleep(60)

async def time_check():
    while not bot.is_closed():
        channel = bot.get_channel(config.CHANNEL_ID)

        now = int(datetime.strftime(datetime.now(),'%H'))
        if now == alert_time_day or now == alert_time_night:
            embed = doujin_generate("SFL")
            msg = await channel.send(embed=embed)
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
            await asyncio.sleep(39600)
        else:
            await asyncio.sleep(1200)
bot.remove_command("help")

@bot.command()
async def pong(ctx):
    embed = help_message()
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('❌')

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

@bot.command()
async def rand(ctx):
    with Timer(text="\nTotal elapsed time: {:.5f}"):
        embed = doujin_generate()
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('❌')

@rand.error
async def rand_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedErr = error_embed("No parameter inputted.","$rand")
        msg = await ctx.send(embed=embedErr)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('❌')

@bot.command()
async def rand_lang(ctx, *, arg):
    with Timer(text="\nTotal elapsed time: {:.5f}"):
        parameter = arg.split(',')
        embed = lang(parameter)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('❌')

@rand_lang.error
async def rand_lang_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedErr = error_embed("No parameter inputted.","$rand_lang")
        msg = await ctx.send(embed=embedErr)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('❌')

@bot.command()
async def rand_tag(ctx, *, arg):
    embed = tag(arg)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('❌')

@rand_tag.error
async def rand_tag_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedErr = error_embed("No parameter inputted.","$rand_tag")
        msg = await ctx.send(embed=embedErr)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        await msg.add_reaction('❌')

@bot.command()
async def set_channel(ctx):
    embed = discord.Embed()
    if not ctx.channel.is_nsfw():
        embed = error_embed("This is not a NSFW channel.","$set_channel")
    elif not ctx.message.author.id in config.OWNERS:
        print(ctx.message.author.id)
        embed = error_embed("You are not the owner.","$set_channel")
    else:
        isExist = add_channel_id(str(ctx.channel.id), str(ctx.channel.name))
        if isExist:
            embed = message_embed("Channel set.", f"ID:{str(ctx.channel.id)}   Channel:{str(ctx.channel.name)}")
        else:
            embed = message_embed("Channel has already been set as daily channel.", f"ID:{str(ctx.channel.id)}   Channel:{str(ctx.channel.name)}")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('❌')

@bot.event
async def on_raw_reaction_add(ctx):
    channelReaction = ctx.channel_id
    user = ctx.Author

    if ctx.emoji.name == '❌':
        channelVar = bot.get_channel(channelReaction)
        message = await channelVar.fetch_message(ctx.message_id)
        reaction = get(message.reactions, emoji=ctx.emoji.name)
        if reaction and reaction.count > 1 and user == message.author:
            await message.delete()

bot.run(config.TOKEN)
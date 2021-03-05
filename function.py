import random
import urllib.request, urllib.error
from nhDetail import nhDetail

# === downloaded from pypl/outside source ===
import nhentai
import discord

#tag
bannedTag = ["guro","rape","torture","necrophilia","amputee","drugs"]
softBannedTag = ["lolicon","shotacon"]
weirdKink = ["netorare","fisting", "exhibitionism"]

#reply message
thank = []
reply_normalTag = []
reply_weirdKink = []
reply_softBannedTag = []
reply_bannedTag = []

#error message
error_msg = ["OWO UWU, WE MADE A FUCKY WUCKY", "beep boop, hopefully it is not a 404 error", "The operation failed successfully", "There is an errRRRRRRRRRRRRR", "pls call @tiktok e-boy#0180 real quick, I\'m having a headache"]

#colour
colour_embed = 0x00ff00
colour_error = 0xf83f3f

#embed
def doujin_embed(doujin, isDaily=False):
    embed=discord.Embed(title=str(doujin.get_title_en()),  url=str(doujin.get_url()), description='#'+str(doujin.get_id()) ,color=colour_embed)
    embed.set_image(url=str(doujin.get_thumbnail()))
    embed.add_field(name="Tag", value=', '.join('` {0} `'.format(x) for x in doujin.get_tag()), inline=False)
    embed.add_field(name="Author", value=', '.join('` {0} `'.format(x) for x in doujin.get_author()), inline=True)
    embed.add_field(name="Language", value=', '.join('` {0} `'.format(x) for x in doujin.get_language()), inline=True)
    embed.add_field(name="Pages", value='`' + str(doujin.get_pages()) + '`' , inline=True)
    #add footer later
    return embed

def error_embed(error, origin):
    embed=discord.Embed(title="⚠️ THIS IS AN ERROR MESSAGE ⚠️", color=colour_error)
    embed.add_field(name="Error", value=error, inline=False)
    embed.add_field(name="Command", value=origin, inline=False)
    embed.set_footer(text=error_msg[random.randint(0,len(error_msg)-1)])
    return embed

def help_message():
    embed=discord.Embed(description="Hello, I'm Amai-chan and I am a nHentai bot.")
    embed.add_field(name="** **", value="Exclude `[ ]` when executing a command", inline=False)
    embed.add_field(name="** **", value="`[ parameters* ]` are optional", inline=False)
    embed.add_field(name="Commands:", value="** **", inline=False)
    embed.add_field(name="** **", value='''``` 
    $search [ ID ]              Search doujin based on ID  
    $read [ ID ][ PAGE NUM* ]   Read doujin based on ID and can accept page    
    $give                       Give random doujin
    $give_lang [ EN/JP ]        Give random doujin with selected language
    $give_tag [ TAG ]           Give random doujin with tag    
    $thank [ ID* ]              Thank the bot
    
     ```''', inline=False) #create table Extra comman, finish up help message
    embed.set_footer(text="Feel free to use me master ^ - ^")
    return embed

#doujin related function
def doujin_search(sauce):
    try:
        doujin_result = nhDetail(nhentai.get_doujin(int(sauce)))
        embed = doujin_embed(doujin_result, False)
        return embed

    except Exception as e: #err for invalid value
        return error_embed(f"{type(e).__name__}: {e}", "doujin_search(sauce)")

def doujin_generate(isDaily=False):
    doujin_result = nhDetail(nhentai.get_random_id())

    if(isDaily):
        while True:
            if set(bannedTag).isdisjoint(doujin_result.get_tag()):
                break
            else:
                doujin_result.replace_doujin(nhentai.get_random_id())
    
    return doujin_embed(doujin_result, True)
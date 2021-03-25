import random, asyncio
from nhDetail import nhDetail

# === downloaded from pypl/outside source ===
import nhentai
import discord
import requests

from codetiming import Timer #for testing purpose only

#tag
bannedTag = ["guro","rape","torture","necrophilia","amputee", "drugs"]
softBannedTag = ["lolicon", "shotacon", "incest", "blackmail"]
weirdKink = ["netorare", "fisting", "exhibitionism"]

#reply message
thank = ["your welcome"]
reply_normalTag = ["normal tag"]
reply_weirdKink = ["weird kink"]
reply_softBannedTag = ["SOFT banned tag"]
reply_bannedTag = ["BANNED tag"]

#error message
error_msg = ["OWH UWH UWU, WE MADE A FUCKY WUCKY", "beep boop, hopefully it is not a 404 error", "The operation failed successfully", "There is an errRRRRRRRRRRRRR", "pls call @tiktok e-boy#0180 real quick, I\'m having a headache"]

#colour
colour_embed = 0x00ff00
colour_error = 0xf83f3f

#random generated
#limit
rand_limit = 399999
#function
def rand_id_generate():
    link = "https://nhentai.net/g/" 
    hdr = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    
    timer = Timer(text=f"Randomize sauce elapsed time: {{:.5f}}")
    timer.start()
    while True:
        sauce = random.randint(0,rand_limit)
        link_comp = link+str(sauce)
        req = requests.get(link_comp, hdr)
        try:
            req.raise_for_status()
        except requests.exceptions.RequestException:
            continue
        timer.stop()
        return sauce

#embed
def message_embed(message_title:str, message:str="** **", title:str=" ", url:str="", desc:str=" "):
    embed=discord.Embed(title=title, url=url, description=desc, color=colour_embed)
    embed.add_field(name=message_title, value=message, inline=False)
    return embed

def doujin_embed(doujin, isDaily=False):
    embed=discord.Embed(title=str(doujin.get_title_en()),  url=str(doujin.get_url()), description='#'+str(doujin.get_id()) ,color=colour_embed)
    embed.set_image(url=str(doujin.get_thumbnail()))
    embed.add_field(name="Tag", value=', '.join('` {0} `'.format(x) for x in doujin.get_tag()), inline=False)
    embed.add_field(name="Author", value=', '.join('` {0} `'.format(x) for x in doujin.get_author()), inline=True)
    embed.add_field(name="Language", value=', '.join('` {0} `'.format(x) for x in doujin.get_language()), inline=True)
    embed.add_field(name="Pages", value='`' + str(doujin.get_page_len()) + '`' , inline=True)
    if not isDaily:
        if not set(bannedTag).isdisjoint(doujin.get_tag()):
            embed.set_footer(text=reply_bannedTag[random.randint(0,len(reply_bannedTag)-1)])
        elif not set(softBannedTag).isdisjoint(doujin.get_tag()):
            embed.set_footer(text=reply_softBannedTag[random.randint(0,len(reply_softBannedTag)-1)])
        elif not set(weirdKink).isdisjoint(doujin.get_tag()):
            embed.set_footer(text=reply_weirdKink[random.randint(0,len(reply_weirdKink)-1)])
        else:
            embed.set_footer(text=reply_normalTag[random.randint(0,len(reply_normalTag)-1)])

    return embed

def error_embed(error, origin):
    embed=discord.Embed(title="⚠️ THIS IS AN ERROR MESSAGE ⚠️", color=colour_error)
    embed.add_field(name="Error", value=error, inline=False)
    embed.add_field(name="Command", value=origin, inline=False)
    embed.set_footer(text=error_msg[random.randint(0,len(error_msg)-1)])
    return embed

def help_message():
    embed=discord.Embed(description="Hello, I'm Amai-chan and I am a nHentai bot. (NSFW bot obviously)")
    embed.add_field(name="Exclude `[ ]` when executing a command", value="** **", inline=False)
    embed.add_field(name="`[ parameters* ]` are optional", value="** **", inline=False)
    embed.add_field(name="Commands:", value="** **", inline=False)
    embed.add_field(name="** **", value='''``` 
$search [ ID ]              Search doujin based on ID

$rand                       Give random doujin

$rand_lang [ EN/JP ]        Give random doujin with selected 
                            language

$rand_tag [ TAG ]           Give random doujin with tag

$thank [ ID* ]              Thank the bot
    
     ```''', inline=False) #create table Extra comman, finish up help message
    embed.set_footer(text="Feel free to use me master ^ - ^")
    return embed

def doujin_read_embed(doujin,cur_page,max_page):
    embed=discord.Embed(title=str(doujin.get_title_en()),  url=str(doujin.get_url()), description='#'+str(doujin.get_id()) ,color=colour_embed)
    embed.set_image(url=str(doujin.get_pages(cur_page)))
    embed.set_footer(text=f"{cur_page+1}/{max_page}")

    return embed

#doujin related function
def doujin_search(sauce):
    try:
        doujin_result = nhDetail(nhentai.get_doujin(int(sauce)))
        embed = doujin_embed(doujin_result, False)
        return embed

    except Exception as e: #err for invalid value
        return error_embed(f"{type(e).__name__}: {e}.", "doujin_search(sauce)")

def doujin_generate(isDaily=False):
    try:
        x=0
        while True:
            sauce = rand_id_generate()
            doujin_result = nhDetail(nhentai.get_doujin(sauce))
            if set(bannedTag).isdisjoint(doujin_result.get_tag()):
                embed = doujin_embed(doujin_result, False)
                return embed
            x+=1
            if x > 20:
                raise TimeoutError("Doujin could not be generated before a Timeout Error was raised.")

    except Exception as e:
        return error_embed(f"{type(e).__name__}: {e}.", "doujin_generate(param_type, parameter)")

def lang(parameter):
    try:
        if parameter[0].lower() == "en":
            parameter[0] = "english"
        if parameter[0].lower() == "jp":
            parameter[0] = "japanese"
        if parameter[0].lower() == "cn":
            parameter[0] = "chinese"
        
        if not parameter[0].lower() in ["english", "japanese", "chinese"]:
            raise ValueError("Parameter value does not match with existing option")
        
        randPage = random.randint(1,20)
        randDoujin = random.randint(0,24)
        print(randPage)

        doujin_list = nhentai.search(parameter[0], randPage, "popular-today")
        doujin = nhDetail(doujin_list[randDoujin])
        embed = doujin_embed(doujin)
        return embed

    except Exception as e:
        return error_embed(f"{type(e).__name__}: {e}.", "rand_lang(param_type, parameter)")

def tag(parameter):
    try:
        randPage = random.randint(1,20)
        randDoujin = random.randint(0,24)

        doujin_list = nhentai.search(parameter, randPage, "popular-today")
        doujin = nhDetail(doujin_list[randDoujin])
        embed = doujin_embed(doujin)
        return embed

    except IndexError as e:
        return error_embed(f"{type(e).__name__}: {e}. (include less tag if this error persist)", "rand_lang(param_type, parameter)")
    except Exception as e:
        return error_embed(f"{type(e).__name__}: {e}.", "rand_lang(param_type, parameter)")
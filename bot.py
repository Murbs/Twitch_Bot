# bot.py

import os
import random

from twitchio.ext import commands
from initializer import Initializer
from playsound import playsound
from random import randint

nicecount = 0

init = Initializer()
bot = commands.Bot(
    irc_token=init.cfg.token,
    client_id=init.cfg.client_id,
    nick=init.cfg.bot_nick,
    prefix=init.cfg.prefix,
    initial_channels=[init.cfg.channel]
)


@bot.event
async def event_ready():
    'When bot goes online, send a random quote from Super Smash Bros.'
    
    loginlist = ["HAS ENTERED THE MESA!", "Steals the Show!", "Joins the Battle!", "Gets Wicked!", "Draws Near!", "Faces the Fury!", "Is Raring to Go!", "Joins Smash House!", "Turns up the Heat!", "Pipes Up!", "Crosses Over!", "Hits the Big Time!"]
    
    ws = bot._ws  # Needed to send messages within event_ready
    await ws.send_privmsg(os.environ['TWITCH_CHANNEL'], f"" +("/me " + random.choice(loginlist)))

# Command List
@bot.command(name='commands')
async def commands(ctx):
    
    commandlist = "!nice, !roll, !sounds, !coinflip"
    await ctx.send(commandlist)

# Ongoing Nice Counter    
@bot.event
async def event_message(ctx):
    'Respond to nice numbers like 69 or 420... nice'
   
    global nicecount
    nicelist = [69, 420]
    
    # Ignore self/streamer 
    if ctx.author.name.lower() == os.environ['TWITCH_BOT_NICK'].lower():
        return
    
    for x in nicelist:
        if str(x) in ctx.content.lower():
            nicecount += 1
    await bot.handle_commands(ctx)


# Output Nice Counter To Chat    
@bot.command(name='nice')
async def nice(ctx):
    
    if str(nicecount) == '0':
        await ctx.send(f"Nice Count: " + str(nicecount) + ". Not Nice :|")
        
    elif str(nicecount) == '69':
        await ctx.send(f"NICE COUNT: " + str(nicecount) + ". NICEEEEEEEEEEEEE ;)")
        
    elif str(nicecount) == '420':
        await ctx.send(f"WEED NUMBER ALERT 420 WEED NUMBER ALERT 420 WEED NUMBER ALERT 420 ALL HANDS ON DECK BLAZE IT")
        
    else:
        await ctx.send(f"Nice count: " + str(nicecount) + ". Nice.")

# Coin Flip        
@bot.command(name='coinflip')
async def coinflip(ctx):
    
    Coin = ['Heads', 'Tails']
    flip = random.choice(Coin)
    
    if flip == 'Heads':
        await ctx.send(f"@{ctx.author.name} flips a coin.. Heads!")
        
    else:
        await ctx.send(f"@{ctx.author.name} flips a coin.. Tails!")
    
# Dice Roll
@bot.command(name='roll')
async def roll(ctx):
    global nicecount
    
    for _ in range(1):
        
        value = random.randint(0, 100)
        
        if value == 69:
            await ctx.send(f"@{ctx.author.name} has rolled a " + str(value) + "!! NICEEEEEEEEEEEEE ;)")
            nicecount += 1
            
        elif value == 0:
            await ctx.send(f"@{ctx.author.name} has rolled a " + str(value) + "... bro...")
            
        elif value == 100:
            await ctx.send(f"@{ctx.author.name} has rolled a " + str(value) + "!! BRO!!") 
            
        else:
            await ctx.send(f"@{ctx.author.name} has rolled a " + str(value) + "!")

# Sounds List
@bot.command(name='sounds')
async def sounds(ctx):
    soundslist = "!sound1, !sound2, etc..."
    await ctx.send(soundslist)
    
# Sounds
@bot.command(name='AAAAA')
async def AAAAA(ctx):
    playsound('<PATH TO SOUND GOES HERE>')
    

if __name__ == "__main__":
    bot.run()
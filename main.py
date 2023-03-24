import asyncio
import keep_alive
import os
import discord
from discord.ext import commands
import json

keep_alive.keep_alive()

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="=", intents=intents, help_command=None)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Dev GamingBotNew"), status=discord.Status.idle)

@bot.event
async def on_guild_join(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
    
    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)
 
@bot.event
async def on_guild_remove(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role.pop(str(guild.id))
    
    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)

@bot.event
async def on_guild_join(guild):
    with open("cogs/jsonfiles/members.json.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
    
    with open("cogs/jsonfiles/members.json", "w") as f:
        json.dump(mute_role, f, indent=4)
 
@bot.event
async def on_guild_remove(guild):
    with open("cogs/jsonfiles/members.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role.pop(str(guild.id))
    
    with open("cogs/jsonfiles/members.json", "w") as f:
        json.dump(mute_role, f, indent=4)

import logging
logging.basicConfig(level=logging.INFO)

async def main():
    await load()
    await bot.start("MTA1OTE2MTY4OTUxOTU2Mjc1Mg.Gf_mvX.9E0ganqY-5TrZpsfOmxBw4TmBJOCxU1Cz28ZGw")


asyncio.run(main())
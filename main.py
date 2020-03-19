import os
import discord
from discord.ext import commands
import time
import asyncio
# settings.py
from dotenv import load_dotenv
from pathlib import Path  

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
bot = commands.Bot(command_prefix='-')
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print('%s has connected to Discord!' % (bot.user))

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kickAll(ctx):
    memberList = ctx.message.guild.members
    for member in memberList:
      if len(member.roles) == 1:
        kickMessage = await ctx.send('kicking %s..' % (member.display_name))
        await member.kick()
        await asyncio.sleep(1)
        kickMessage.delete()
    finalMessage = await ctx.send('kicked all refugees')
    await asyncio.sleep(3)
    await finalMessage.delete()


@bot.command(pass_context=True)
async def test(ctx):
    greetMessage = await ctx.send('hello! your test worked!')
    await asyncio.sleep(1)
    goodbyeMessage = await ctx.send('later!')
    await asyncio.sleep(3)
    await greetMessage.delete()
    await goodbyeMessage.delete()

bot.run(TOKEN)
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')
clearly = False

@Bot.command()
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))
    await ctx.message.delete()
    
@Bot.command()
async def clean():
    await channel.message.delete()

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

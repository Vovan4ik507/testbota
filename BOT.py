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
    
@Bor.command()
async def clean(quant):
    await channel.message.delete(int(quant))

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

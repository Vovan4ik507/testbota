import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')
Bot.remove_command('hello')

@Bot.command()
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))
    await ctx.delete_message(ctx.message)

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

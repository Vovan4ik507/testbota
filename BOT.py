import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))
    await ctx.message.delete()    
    
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")
    await member.add_roles(mute_role)
    await ctx.message.delete()
    await ctx.send('Muted sucsesful')

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

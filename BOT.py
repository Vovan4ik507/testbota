import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def hello(ctx):
    	await ctx.send("Hello {}".format(ctx.message.author.mention))

@Bot.command()
async def say(ctx, arg):
	await ctx.send(arg)

@Bot.command()
async def info(ctx, member: discord.Member):
	emb = discord.Embed(title = "Info about <@{}>".format(member.id), color = 0x39d0d6)
	emb.add_field(name = "Name", value = member.name)
	emb.add_field(name = "Joined at", value = str(member.joined_at)[:16])
	emb.add_field(name = "ID", value = member.id)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_author(name = "Bot paradise", url = "https://discordapp.com/oauth2/authorize?client_id=513405344718782464&scope=bot&permissions=8")
	emb.set_footer(text = "Caused by: <@{}>".format(member.id), icon_url = member.avatar_url)
	await ctx.send(embed = emb)
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

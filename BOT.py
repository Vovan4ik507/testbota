import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def hello(ctx):
    	await ctx.send("Hello {}".format(ctx.message.author.mention))

@Bot.command()
async def say(ctx, *, arg):
	await ctx.send(arg)

@Bot.command()
async def info(ctx, member: discord.Member):
	emb = discord.Embed(title = "Info about {}".format(member.mention), color = 0x39d0d6)
	emb.add_field(name = "Name", value = member.name, inline = False)
	emb.add_field(name = "Status", value = member.status, inline = False)
	emb.add_field(name = "Highest role", value = member.roles, inline = False)
	emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_author(name = "@Vovan#0901", url = "https://discordapp.com/oauth2/authorize?client_id=513405344718782464&scope=bot&permissions=8")
	emb.set_footer(text = "Caused by: {}".format(member.name), icon_url = member.avatar_url)
	await ctx.send(embed = emb)
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

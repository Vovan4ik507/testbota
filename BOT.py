import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def hello(ctx):
    	await ctx.send("Hello {}".format(ctx.message.author.mention))
    	await ctx.message.delete()    
    
@Bot.command()
async def mute(ctx, member: discord.Member):
    	mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")
    	await member.add_roles(mute_role)
    	await ctx.send('Muted successful')
	await ctx.message.delete()
    
@Bot.command()
async def info(ctx, member: discord.Member):
	emb = discord.Embed(title = "Info about {}".format(member.mention), color= 0x39d0d6)
	emd.add_field(name = "Name", value = member.mention)
	emb.add_field(name = "Joined at", value = str(member.joined at)[:23])
	emb.add_field(name = "ID", value = member.id)
	if user.game != None:
		emb.add_field(name = "Game", value = member.game)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_author(name = "Vovan408#0901", url = "https://discordapp.com/oauth2/authorize?client_id=513405344718782464&scope=bot&permissions=8")
	emb.set_footer(text = "Caused by: {}".format(member.mention), icon_url = member.avatar_url)
	await ctx.send(embed = emb)

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

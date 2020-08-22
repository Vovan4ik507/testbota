import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

Bot = commands.Bot(command_prefix = '-')
#value = str(member.joined_at)[:19]

@Bot.command()
async def user(ctx, member: discord.Member):
    	emb = discord.Embed(title = str(member), description = member.mention, color = member.top_role.color)
    	emb.add_field(name = "ID", value = member.id, inline = False)
	if str(member.joined_at)[8:10] == '01' or str(member.joined_at)[8:10] == '21' or str(member.joined_at)[8:10] == '31':
		day = str(member.joined_at)[8:10] + 'st'
	else:
		day = str(member.joined_at)[8:10]
    	emb.add_field(name = "Joined server at", value = str(member.joined_at)[8:10], inline = False)
    	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
    	if member.top_role == member.roles[0]:
        	emb.add_field(name = "Highest role", value = member.top_role, inline = False)
    	else:
        	emb.add_field(name = "Highest role", value = member.top_role.mention, inline = False)
    	emb.set_thumbnail(url = member.avatar_url)
    	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
    	await ctx.send(embed = emb)

@Bot.event
async def on_ready():
	print('Bot is online')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Playing with developer'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

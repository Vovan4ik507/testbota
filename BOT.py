import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import datetime
import time

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def now-time(ctx):
	await ctx.send(datetime.datetime.year)

@Bot.command()
async def user(ctx, member: discord.Member):
	emb = discord.Embed(title = str(member), description = member.mention, color = member.top_role.color)
	emb.add_field(name = "ID", value = member.id, inline = False)
	if str(member.joined_at)[8:10] == '01':
		join_day = str(member.joined_at)[9:10] + 'st'
	elif str(member.joined_at)[8:10] == '02':
		join_day = str(member.joined_at)[9:10] + 'nd'
	elif str(member.joined_at)[8:10] == '03':
		join_day = str(member.joined_at)[9:10] + 'rd'
	elif (str(member.joined_at)[8:10] == '04' or str(member.joined_at)[8:10] == '05' or str(member.joined_at)[8:10] == '06'
	      or str(member.joined_at)[8:10] == '07' or str(member.joined_at)[8:10] == '08' or str(member.joined_at)[8:10] == '09'):
		join_day = str(member.joined_at)[9:10] + 'th'
	elif str(member.joined_at)[8:10] == '21' or str(member.joined_at)[8:10] == '31':
		join_day = str(member.joined_at)[8:10] + 'st'
	elif str(member.joined_at)[8:10] == '22':
		join_day = str(member.joined_at)[8:10] + 'nd'
	elif str(member.joined_at)[8:10] == '23':
		join_day = str(member.joined_at)[8:10] + 'rd'
	else:
		join_day = str(member.joined_at)[8:10] + 'th'
	if str(member.joined_at)[5:7] == '01':
		join_month = ' February '
	elif str(member.joined_at)[5:7] == '02':
		join_month = ' January '
	elif str(member.joined_at)[5:7] == '03':
		join_month = ' March '
	elif str(member.joined_at)[5:7] == '04':
		join_month = ' April '
	elif str(member.joined_at)[5:7] == '05':
		join_month = ' May '
	elif str(member.joined_at)[5:7] == '06':
		join_month = ' June '
	elif str(member.joined_at)[5:7] == '07':
		join_month = ' July '
	elif str(member.joined_at)[5:7] == '08':
		join_month = ' August '
	elif str(member.joined_at)[5:7] == '09':
		join_month = ' September '
	elif str(member.joined_at)[5:7] == '10':
		join_month = ' October '
	elif str(member.joined_at)[5:7] == '11':
		join_month = ' November '
	elif str(member.joined_at)[5:7] == '12':
		join_month = ' December '
	join_date = join_day + join_month + str(member.joined_at)[2:4]
	emb.add_field(name = "Joined servert", value = join_date, inline = False)
	if str(member.created_at)[8:10] == '01':
		create_day = str(member.created_at)[9:10] + 'st'
	elif str(member.created_at)[8:10] == '02':
		create_day = str(member.created_at)[9:10] + 'nd'
	elif str(member.created_at)[8:10] == '03':
		create_day = str(member.created_at)[9:10] + 'rd'
	elif (str(member.created_at)[8:10] == '04' or str(member.created_at)[8:10] == '05' or str(member.created_at)[8:10] == '06'
	      or str(member.created_at)[8:10] == '07' or str(member.created_at)[8:10] == '08' or str(member.created_at)[8:10] == '09'):
		create_day = str(member.created_at)[9:10] + 'th'
	elif str(member.created_at)[8:10] == '21' or str(member.created_at)[8:10] == '31':
		create_day = str(member.created_at)[8:10] + 'st'
	elif str(member.created_at)[8:10] == '22':
		create_day = str(member.created_at)[8:10] + 'nd'
	elif str(member.created_at)[8:10] == '23':
		create_day = str(member.created_at)[8:10] + 'rd'
	else:
		create_day = str(member.created_at)[8:10] + 'th'
	if str(member.created_at)[5:7] == '01':
		create_month = ' February '
	elif str(member.created_at)[5:7] == '02':
		create_month = ' January '
	elif str(member.created_at)[5:7] == '03':
		create_month = ' March '
	elif str(member.created_at)[5:7] == '04':
		create_month = ' April '
	elif str(member.created_at)[5:7] == '05':
		create_month = ' May '
	elif str(member.created_at)[5:7] == '06':
		create_month = ' June '
	elif str(member.created_at)[5:7] == '07':
		create_month = ' July '
	elif str(member.created_at)[5:7] == '08':
		create_month = ' August '
	elif str(member.created_at)[5:7] == '09':
		create_month = ' September '
	elif str(member.created_at)[5:7] == '10':
		create_month = ' October '
	elif str(member.created_at)[5:7] == '11':
		create_month = ' November '
	elif str(member.created_at)[5:7] == '12':
		create_month = ' December '
	create_date = create_day + create_month + str(member.created_at)[2:4]
	emb.add_field(name = "Created account", value = create_date, inline = False)
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

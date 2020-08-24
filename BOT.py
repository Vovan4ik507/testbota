import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import datetime
import time

Bot = commands.Bot(command_prefix = '-')
	
@Bot.command()
async def ping(ctx):
	channel = ctx.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	latency = round(Bot.latency *1000)
	t = round((t2-t1)*1000)
	green = discord.Color.green()
	desc=f":heartbeat: **{latency}**ms \n :stopwatch: **{t}**ms"
	em = discord.Embed(title = ":ping_pong: Pong",description = desc, color = green)
	em.set_footer(text = f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
	await ctx.send(embed = em)
	
@Bot.command()
async def say(ctx, channel = None, *, word = None):
	stop = False
	guild = ctx.guild
	channel_list = guild.text_channels
	for i in range(0, len(channel_list)):
		if channel == channel_list[i].name or channel == channel_list[i].id or channel == channel_list[i].mention:
			if word == None:
				stop = True
				await ctx.send('You don\'t wrote what to say')
			else:
				stop = True
				channel = channel_list[i]
				await channel.send(word)
	else:
			if channel == None:
				await ctx.send('You don\'t wrote what to say')
			else:
				if stop == False:
					if word == None:
						await ctx.send(channel)
					else:
						await ctx.send(channel + f' {word}')
						
@Bot.command()
async def clean(ctx, channel = None, msgs = None):
		
	if channel == None:
		await ctx.send('These command need argument')
	else:
		stop = False
		guild = ctx.guild
		channel_list = guild.text_channels
		for i in range(0, len(channel_list)):
			if channel == channel_list[i].name or channel == channel_list[i].id or channel == channel_list[i].mention:
				if msgs == None:
					stop = True
					await ctx.send('You don\'t wrote how many messages I need to delete.')
				else:
					stop = True
					channel = channel_list[i]
					deleted = await channel.purge(limit = int(msgs))
					if len(deleted) == 1:
						await channel.purge(limit = 1)
						await channel.send(f'Deleted {len(deleted)} message')
					else:
						await channel.purge(limit = 1)
						await channel.send(f'Deleted {len(deleted)} messages')
		else:
			if stop == False:
				deleted = await ctx.channel.purge(limit = int(channel))
				if len(deleted) == 1:
					await ctx.channel.purge(limit = 1)
					await ctx.send(f'Deleted {len(deleted)} message')
				else:
					await ctx.channel.purge(limit = 1)
					await ctx.send(f'Deleted {len(deleted)} messages')
	
@Bot.command()
async def user(ctx, member = None):
	
	guild = ctx.guild
	member_list = guild.members
	member_stop = False
	mention1 = ''
	mention2 = ''
	mention_list = []
	
	author_mention = str(member)
	if author_mention[1] == '@' and author_mention[2] != '!':
		author_mention = member[0:2] + '!' + member[2 : len(member)]
		member = author_mention
	
	for i in range(0, len(member_list)):
		mention1 = member_list[i].mention
		if mention1[1] == '@' and mention1[2] == '!':
			mention_list.append(mention1)
		else:
			mention2 = mention1[0 : 2] + '!' + mention1[2 : len(mention1)]
			mention_list.append(mention2)	
	
	for i in range(0, len(member_list)):
		if member == member_list[i].name or member == str(member_list[i].id) or member == mention_list[i]:
			member_stop = True
			member = member_list[i]
	else:
		if member_stop == False:
			if member == None:
				member = ctx.author
			else:
				await ctx.send(f'You wrote member index incorectly, `{member}`')
	
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
	
	now_time_year = str(datetime.date.today())[0:4]
	now_time_year = int(now_time_year)
	joined_time_year = str(member.joined_at)[0:4]
	joined_time_year = int(joined_time_year)
	
	now_time_month = str(datetime.date.today())[5:7]
	now_time_month = int(now_time_month)
	joined_time_month = str(member.joined_at)[5:7]
	joined_time_month = int(joined_time_month)
	
	if (now_time_month == 1 or now_time_month == 3 or now_time_month == 5 or now_time_month == 7
	    or now_time_month == 8 or now_time_month == 10 or now_time_month == 12):
		day_bonus = 31
	elif now_time_month == 2:
		day_bonus = 28
	else:
		day_bonus = 30
	
	now_time_day = str(datetime.date.today())[8:10]
	now_time_day = int(now_time_day)
	joined_time_day = str(member.joined_at)[8:10]
	joined_time_day = int(joined_time_day)
	week = 0
	
	if now_time_day < joined_time_day:
		now_time_month -= 1
		now_time_day += day_bonus
		day = now_time_day - joined_time_day
	else:
		day = now_time_day - joined_time_day
	
	if now_time_month < joined_time_month:
		now_time_year -= 1
		now_time_month += 12
		month = now_time_month - joined_time_month
	else:
		month = now_time_month - joined_time_month
	
	while day // 7:
		week += 1
		day -= 7
	
	year = now_time_year - joined_time_year
	
	if year == 0:
		if month == 0:
			if week == 0:
				if day == 0:
					join_msg = 'Today'
				elif day == 1:
					join_msg = '1 day ago'
				else:
					join_msg = f'{str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = '1 week ago'
				elif day == 1:
					join_msg = '1 week and 1 day ago'
				else:
					join_msg = f'1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					join_msg = f'{str(week)} weeks ago'
				elif day == 1:
					join_msg = f'{str(week)} weeks and 1 day ago'
				else:
					join_msg = f'{str(week)} weeks and ' + str(day) + ' days ago'
		elif month == 1:
			if week == 0:
				if day == 0:
					join_msg = '1 month ago'
				elif day == 1:
					join_msg = '1 month and 1 day ago'
				else:
					join_msg = f'1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = '1 month and 1 week ago'
				elif day == 1:
					join_msg = '1 month, 1 week and 1 day ago'
				else:
					join_msg = f'1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					join_msg = f'1 month {str(week)} weeks ago'
				elif day == 1:
					join_msg = f'1 month, {str(week)} weeks and 1 day ago'
				else:
					join_msg = f'1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					join_msg = f'{str(month)} month ago'
				elif day == 1:
					join_msg = f'{str(month)} month and 1 day ago'
				else:
					join_msg = f'{str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = f'{month} month and 1 week ago'
				elif day == 1:
					join_msg = f'{month} month, 1 week and 1 day ago'
				else:
					join_msg = f'{month} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					join_msg = f'{month} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					join_msg = f'{month} month and ' + str(week) + ' weeks and 1 day ago'
				else:
					join_msg = f'{month} month and ' + str(week) + f' weeks and {str(day)} days ago'
					
	elif year == 1:
		if month == 0:
			if week == 0:
				if day == 0:
					join_msg = '1 year ago'
				elif day == 1:
					join_msg = '1 year and 1 day ago'
				else:
					join_msg = f'1 year and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = '1 year and 1 week ago'
				elif day == 1:
					join_msg = '1 year, 1 week and 1 day ago'
				else:
					join_msg = f'1 year, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					join_msg = f'1 year and {str(week)} weeks ago'
				elif day == 1:
					join_msg = f'1 year, {str(week)} weeks and 1 day ago'
				else:
					join_msg = f'1 year, {str(week)} weeks and ' + str(day) + ' days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					join_msg = '1 year and 1 month ago'
				elif day == 1:
					join_msg = '1 year, 1 month and 1 day ago'
				else:
					join_msg = f'1 year, 1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = '1 year, 1 month and 1 week ago'
				elif day == 1:
					join_msg = '1 year, 1 month, 1 week and 1 day ago'
				else:
					join_msg = f'1 year, 1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					join_msg = f'1 year, 1 month and {str(week)} weeks ago'
				elif day == 1:
					join_msg = f'1 year, 1 month, {str(week)} weeks and 1 day ago'
				else:
					join_msg = f'1 year, 1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					join_msg = f'1 year and {str(month)} month ago'
				elif day == 1:
					join_msg = f'1 year, {str(month)} month and 1 day ago'
				else:
					join_msg = f'1 year, {str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = f'1 year, {str(month)} month and 1 week ago'
				elif day == 1:
					join_msg = f'1 year, {str(month)} month, 1 week and 1 day ago'
				else:
					join_msg = f'1 year, {str(month)} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					join_msg = f'1 year, {str(month)} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					join_msg = f'1 year, {str(month)} month, ' + str(week) + ' weeks and 1 day ago'
				else:
					join_msg = f'1 year, {str(month)} month, ' + str(week) + f' weeks and {str(day)} days ago'
	else:
		if month == 0:
			if week == 0:
				if day == 0:
					join_msg = f'{str(year)} years ago'
				elif day == 1:
					join_msg = f'{str(year)} years and 1 day ago'
				else:
					join_msg = f'{str(year)} years and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = f'{str(year)} years and 1 week ago'
				elif day == 1:
					join_msg = f'{str(year)} years, 1 week and 1 day ago'
				else:
					join_msg = f'{str(year)} years, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					join_msg = f'{str(year)} years and ' + str(week) + ' weeks ago'
				elif day == 1:
					join_msg = f'{str(year)} years, ' + str(week) + ' weeks and 1 day ago'
				else:
					join_msg = f'{str(year)} years, ' + str(week) + f' weeks and {str(day)} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					join_msg = f'{str(year)} years and 1 month ago'
				elif day == 1:
					join_msg = f'{str(year)} years, 1 month and 1 day ago'
				else:
					join_msg = f'{str(year)} years, 1 month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = f'{str(year)} years, 1 month and 1 week ago'
				elif day == 1:
					join_msg = f'{str(year)} years, 1 month, 1 week and 1 day ago'
				else:
					join_msg = f'{str(year)} years, 1 month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					join_msg = f'{str(year)} years, 1 month and ' + str(week) + ' weeks ago'
				elif day == 1:
					join_msg = f'{str(year)} years, 1 month, ' + str(week) + ' weeks and 1 day ago'
				else:
					join_msg = f'{str(year)} years, 1 month, ' + str(week) + f' weeks and {str(day)} days ago'
					
		else:
			if week == 0:
				if day == 0:
					join_msg = f'{str(year)} years and ' + str(month) + ' month ago'
				elif day == 1:
					join_msg = f'{str(year)} years, ' +  str(month) + ' month and 1 day ago'
				else:
					join_msg = f'{str(year)} years, ' + str(month) + f' month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					join_msg = f'{str(year)} years, ' + str(month) + ' month and 1 week ago'
				elif day == 1:
					join_msg = f'{str(year)} years, ' + str(month) + ' month, 1 week and 1 day ago'
				else:
					join_msg = f'{str(year)} years, ' + str(month) + f' month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					join_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks ago'
				elif day == 1:
					join_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and 1 day ago'
				else:
					join_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and ' + str(day) + ' days ago'
	
	join_info = join_date + f' ({join_msg})'
	
	emb.add_field(name = "Joined server", value = join_info, inline = False)
	
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
	
	now_time_year = str(datetime.date.today())[0:4]
	now_time_year = int(now_time_year)
	created_time_year = str(member.created_at)[0:4]
	created_time_year = int(created_time_year)
	
	now_time_month = str(datetime.date.today())[5:7]
	now_time_month = int(now_time_month)
	created_time_month = str(member.created_at)[5:7]
	created_time_month = int(created_time_month)
	
	if (now_time_month == 1 or now_time_month == 3 or now_time_month == 5 or now_time_month == 7
	    or now_time_month == 8 or now_time_month == 10 or now_time_month == 12):
		day_bonus = 31
	elif now_time_month == 2:
		day_bonus = 28
	else:
		day_bonus = 30
	
	now_time_day = str(datetime.date.today())[8:10]
	now_time_day = int(now_time_day)
	created_time_day = str(member.created_at)[8:10]
	created_time_day = int(created_time_day)
	week = 0
	
	if now_time_day < created_time_day:
		now_time_month -= 1
		now_time_day += day_bonus
		day = now_time_day - created_time_day
	else:
		day = now_time_day - created_time_day
	
	if now_time_month < created_time_month:
		now_time_year -= 1
		now_time_month += 12
		month = now_time_month - created_time_month
	else:
		month = now_time_month - created_time_month
	
	while day // 7:
		week += 1
		day -= 7
	
	year = now_time_year - created_time_year
	
	if year == 0:
		if month == 0:
			if week == 0:
				if day == 0:
					create_msg = 'Today'
				elif day == 1:
					create_msg = '1 day ago'
				else:
					create_msg = f'{str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = '1 week ago'
				elif day == 1:
					create_msg = '1 week and 1 day ago'
				else:
					create_msg = f'1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					create_msg = f'{str(week)} weeks ago'
				elif day == 1:
					create_msg = f'{str(week)} weeks and 1 day ago'
				else:
					create_msg = f'{str(week)} weeks and ' + str(day) + ' days ago'
		elif month == 1:
			if week == 0:
				if day == 0:
					create_msg = '1 month ago'
				elif day == 1:
					create_msg = '1 month and 1 day ago'
				else:
					create_msg = f'1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = '1 month and 1 week ago'
				elif day == 1:
					create_msg = '1 month, 1 week and 1 day ago'
				else:
					create_msg = f'1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					create_msg = f'1 month {str(week)} weeks ago'
				elif day == 1:
					create_msg = f'1 month, {str(week)} weeks and 1 day ago'
				else:
					create_msg = f'1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					create_msg = f'{str(month)} month ago'
				elif day == 1:
					create_msg = f'{str(month)} month and 1 day ago'
				else:
					create_msg = f'{str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = f'{month} month and 1 week ago'
				elif day == 1:
					create_msg = f'{month} month, 1 week and 1 day ago'
				else:
					create_msg = f'{month} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					create_msg = f'{month} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					create_msg = f'{month} month and ' + str(week) + ' weeks and 1 day ago'
				else:
					create_msg = f'{month} month and ' + str(week) + f' weeks and {str(day)} days ago'
					
	elif year == 1:
		if month == 0:
			if week == 0:
				if day == 0:
					create_msg = '1 year ago'
				elif day == 1:
					create_msg = '1 year and 1 day ago'
				else:
					create_msg = f'1 year and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = '1 year and 1 week ago'
				elif day == 1:
					create_msg = '1 year, 1 week and 1 day ago'
				else:
					create_msg = f'1 year, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					create_msg = f'1 year and {str(week)} weeks ago'
				elif day == 1:
					create_msg = f'1 year, {str(week)} weeks and 1 day ago'
				else:
					create_msg = f'1 year, {str(week)} weeks and ' + str(day) + ' days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					create_msg = '1 year and 1 month ago'
				elif day == 1:
					create_msg = '1 year, 1 month and 1 day ago'
				else:
					create_msg = f'1 year, 1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = '1 year, 1 month and 1 week ago'
				elif day == 1:
					create_msg = '1 year, 1 month, 1 week and 1 day ago'
				else:
					create_msg = f'1 year, 1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					create_msg = f'1 year, 1 month and {str(week)} weeks ago'
				elif day == 1:
					create_msg = f'1 year, 1 month, {str(week)} weeks and 1 day ago'
				else:
					create_msg = f'1 year, 1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					create_msg = f'1 year and {str(month)} month ago'
				elif day == 1:
					create_msg = f'1 year, {str(month)} month and 1 day ago'
				else:
					create_msg = f'1 year, {str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = f'1 year, {str(month)} month and 1 week ago'
				elif day == 1:
					create_msg = f'1 year, {str(month)} month, 1 week and 1 day ago'
				else:
					create_msg = f'1 year, {str(month)} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					create_msg = f'1 year, {str(month)} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					create_msg = f'1 year, {str(month)} month, ' + str(week) + ' weeks and 1 day ago'
				else:
					create_msg = f'1 year, {str(month)} month, ' + str(week) + f' weeks and {str(day)} days ago'
	else:
		if month == 0:
			if week == 0:
				if day == 0:
					create_msg = f'{str(year)} years ago'
				elif day == 1:
					create_msg = f'{str(year)} years and 1 day ago'
				else:
					create_msg = f'{str(year)} years and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = f'{str(year)} years and 1 week ago'
				elif day == 1:
					create_msg = f'{str(year)} years, 1 week and 1 day ago'
				else:
					create_msg = f'{str(year)} years, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					create_msg = f'{str(year)} years and ' + str(week) + ' weeks ago'
				elif day == 1:
					create_msg = f'{str(year)} years, ' + str(week) + ' weeks and 1 day ago'
				else:
					create_msg = f'{str(year)} years, ' + str(week) + f' weeks and {str(day)} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					create_msg = f'{str(year)} years and 1 month ago'
				elif day == 1:
					create_msg = f'{str(year)} years, 1 month and 1 day ago'
				else:
					create_msg = f'{str(year)} years, 1 month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = f'{str(year)} years, 1 month and 1 week ago'
				elif day == 1:
					create_msg = f'{str(year)} years, 1 month, 1 week and 1 day ago'
				else:
					create_msg = f'{str(year)} years, 1 month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					create_msg = f'{str(year)} years, 1 month and ' + str(week) + ' weeks ago'
				elif day == 1:
					create_msg = f'{str(year)} years, 1 month, ' + str(week) + ' weeks and 1 day ago'
				else:
					create_msg = f'{str(year)} years, 1 month, ' + str(week) + f' weeks and {str(day)} days ago'
					
		else:
			if week == 0:
				if day == 0:
					create_msg = f'{str(year)} years and ' + str(month) + ' month ago'
				elif day == 1:
					create_msg = f'{str(year)} years, ' +  str(month) + ' month and 1 day ago'
				else:
					create_msg = f'{str(year)} years, ' + str(month) + f' month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					create_msg = f'{str(year)} years, ' + str(month) + ' month and 1 week ago'
				elif day == 1:
					create_msg = f'{str(year)} years, ' + str(month) + ' month, 1 week and 1 day ago'
				else:
					create_msg = f'{str(year)} years, ' + str(month) + f' month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					create_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks ago'
				elif day == 1:
					create_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and 1 day ago'
				else:
					create_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and ' + str(day) + ' days ago'
	
	create_info = create_date + f' ({create_msg})'
	
	emb.add_field(name = "Created account", value = create_info, inline = False)
	if member.top_role == member.roles[0]:
		emb.add_field(name = "Highest role", value = member.top_role, inline = False)
	else:
		emb.add_field(name = "Highest role", value = member.top_role.mention, inline = False)
	if len(member.roles) >= 2:
		for i in range(1, len(member.roles)):
			if i == 1:
				mention = member.roles[i].mention
			else:
				mention += ', '
				mention += member.roles[i].mention
	else:
		mention = 'You don\'t have any roles.'
	emb.add_field(name = "Roles", value = mention, inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)

@Bot.command()
async def server(ctx):
	server = ctx.guild
	online_members = 0
	inactive_members = 0
	busy_members = 0
	bot_members = 0
	bans = await server.bans()
	s_e = discord.Embed(title = server.name, description = server.description, color = discord.Color.green())
	s_e.add_field(name = "Server ID", value = server.id)
	s_e.add_field(name = "Server Owner", value = server.owner.mention)
	for i in range(0, len(server.members)):
		if server.members[i].status == discord.Status.online:
			if server.members[i].bot == False:
				online_members += 1
		elif server.members[i].status == discord.Status.idle:
			if server.members[i].bot == False:
				inactive_members += 1
		elif server.members[i].status == discord.Status.dnd:
			if server.members[i].bot == False:
				busy_members += 1
	for i in range(0, len(server.members)):
		if server.members[i].bot == True:
			bot_members += 1
	members = (f'<:online:747352635643920385> {online_members} Online<:transparent:747360968773730325><:idle:747490969984958544> {inactive_members} Inactive'
		   +f'<:transparent:747360968773730325><:dnd:747492056087134289> {busy_members} Busy<:transparent:747360968773730325>'
		   +f'\n<:offline:747355444250542141> {len(server.members) - bot_members} Members')
	s_e.add_field(name = "Members", value = members, inline = False)
	channels = f'<:textchannel:747403102650368032> {len(server.text_channels)} Text<:transparent:747360968773730325><:voicechannel:747410314630266960> {len(server.voice_channels)} Voice'
	s_e.add_field(name = "Channels", value = channels, inline = False)
	s_e.add_field(name = "Roles", value = len(server.roles))
	s_e.add_field(name = "Emojis", value = f':grinning: {len(server.emojis)}')
	
	if str(server.created_at)[8:10] == '01':
		server_day = str(server.created_at)[9:10] + 'st'
	elif str(server.created_at)[8:10] == '02':
		server_day = str(server.created_at)[9:10] + 'nd'
	elif str(server.created_at)[8:10] == '03':
		server_day = str(server.created_at)[9:10] + 'rd'
	elif (str(server.created_at)[8:10] == '04' or str(server.created_at)[8:10] == '05' or str(server.created_at)[8:10] == '06'
	      or str(server.created_at)[8:10] == '07' or str(server.created_at)[8:10] == '08' or str(server.created_at)[8:10] == '09'):
		server_day = str(server.created_at)[9:10] + 'th'
	elif str(server.created_at)[8:10] == '21' or str(server.created_at)[8:10] == '31':
		server_day = str(server.created_at)[8:10] + 'st'
	elif str(server.created_at)[8:10] == '22':
		server_day = str(server.created_at)[8:10] + 'nd'
	elif str(server.created_at)[8:10] == '23':
		server_day = str(server.created_at)[8:10] + 'rd'
	else:
		server_day = str(server.created_at)[8:10] + 'th'
		
	if str(server.created_at)[5:7] == '01':
		server_month = ' February '
	elif str(server.created_at)[5:7] == '02':
		server_month = ' January '
	elif str(server.created_at)[5:7] == '03':
		server_month = ' March '
	elif str(server.created_at)[5:7] == '04':
		server_month = ' April '
	elif str(server.created_at)[5:7] == '05':
		server_month = ' May '
	elif str(server.created_at)[5:7] == '06':
		server_month = ' June '
	elif str(server.created_at)[5:7] == '07':
		server_month = ' July '
	elif str(server.created_at)[5:7] == '08':
		server_month = ' August '
	elif str(server.created_at)[5:7] == '09':
		server_month = ' September '
	elif str(server.created_at)[5:7] == '10':
		server_month = ' October '
	elif str(server.created_at)[5:7] == '11':
		server_month = ' November '
	elif str(server.created_at)[5:7] == '12':
		server_month = ' December '
		
	server_date = server_day + server_month + str(server.created_at)[2:4]
	
	now_time_year = str(datetime.date.today())[0:4]
	now_time_year = int(now_time_year)
	server_time_year = str(server.created_at)[0:4]
	server_time_year = int(server_time_year)
	
	now_time_month = str(datetime.date.today())[5:7]
	now_time_month = int(now_time_month)
	server_time_month = str(server.created_at)[5:7]
	server_time_month = int(server_time_month)
	
	if (now_time_month == 1 or now_time_month == 3 or now_time_month == 5 or now_time_month == 7
	    or now_time_month == 8 or now_time_month == 10 or now_time_month == 12):
		day_bonus = 31
	elif now_time_month == 2:
		day_bonus = 28
	else:
		day_bonus = 30
	
	now_time_day = str(datetime.date.today())[8:10]
	now_time_day = int(now_time_day)
	server_time_day = str(server.created_at)[8:10]
	server_time_day = int(server_time_day)
	week = 0
	
	if now_time_day < server_time_day:
		now_time_month -= 1
		now_time_day += day_bonus
		day = now_time_day - server_time_day
	else:
		day = now_time_day - server_time_day
	
	if now_time_month < server_time_month:
		now_time_year -= 1
		now_time_month += 12
		month = now_time_month - server_time_month
	else:
		month = now_time_month - server_time_month
	
	while day // 7:
		week += 1
		day -= 7
	
	year = now_time_year - server_time_year
	
	if year == 0:
		if month == 0:
			if week == 0:
				if day == 0:
					server_msg = 'Today'
				elif day == 1:
					server_msg = '1 day ago'
				else:
					server_msg = f'{str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 week ago'
				elif day == 1:
					server_msg = '1 week and 1 day ago'
				else:
					server_msg = f'1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(week)} weeks ago'
				elif day == 1:
					server_msg = f'{str(week)} weeks and 1 day ago'
				else:
					server_msg = f'{str(week)} weeks and ' + str(day) + ' days ago'
		elif month == 1:
			if week == 0:
				if day == 0:
					server_msg = '1 month ago'
				elif day == 1:
					server_msg = '1 month and 1 day ago'
				else:
					server_msg = f'1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 month and 1 week ago'
				elif day == 1:
					server_msg = '1 month, 1 week and 1 day ago'
				else:
					server_msg = f'1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'1 month {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'1 month, {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					server_msg = f'{str(month)} month ago'
				elif day == 1:
					server_msg = f'{str(month)} month and 1 day ago'
				else:
					server_msg = f'{str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{month} month and 1 week ago'
				elif day == 1:
					server_msg = f'{month} month, 1 week and 1 day ago'
				else:
					server_msg = f'{month} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'{month} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'{month} month and ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'{month} month and ' + str(week) + f' weeks and {str(day)} days ago'
					
	elif year == 1:
		if month == 0:
			if week == 0:
				if day == 0:
					server_msg = '1 year ago'
				elif day == 1:
					server_msg = '1 year and 1 day ago'
				else:
					server_msg = f'1 year and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 year and 1 week ago'
				elif day == 1:
					server_msg = '1 year, 1 week and 1 day ago'
				else:
					server_msg = f'1 year, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'1 year and {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'1 year, {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'1 year, {str(week)} weeks and ' + str(day) + ' days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					server_msg = '1 year and 1 month ago'
				elif day == 1:
					server_msg = '1 year, 1 month and 1 day ago'
				else:
					server_msg = f'1 year, 1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 year, 1 month and 1 week ago'
				elif day == 1:
					server_msg = '1 year, 1 month, 1 week and 1 day ago'
				else:
					server_msg = f'1 year, 1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'1 year, 1 month and {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'1 year, 1 month, {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'1 year, 1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					server_msg = f'1 year and {str(month)} month ago'
				elif day == 1:
					server_msg = f'1 year, {str(month)} month and 1 day ago'
				else:
					server_msg = f'1 year, {str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'1 year, {str(month)} month and 1 week ago'
				elif day == 1:
					server_msg = f'1 year, {str(month)} month, 1 week and 1 day ago'
				else:
					server_msg = f'1 year, {str(month)} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'1 year, {str(month)} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'1 year, {str(month)} month, ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'1 year, {str(month)} month, ' + str(week) + f' weeks and {str(day)} days ago'
	else:
		if month == 0:
			if week == 0:
				if day == 0:
					server_msg = f'{str(year)} years ago'
				elif day == 1:
					server_msg = f'{str(year)} years and 1 day ago'
				else:
					server_msg = f'{str(year)} years and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{str(year)} years and 1 week ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 week and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(year)} years and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(week) + f' weeks and {str(day)} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					server_msg = f'{str(year)} years and 1 month ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 month and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{str(year)} years, 1 month and 1 week ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 month, 1 week and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(year)} years, 1 month and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 month, ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 month, ' + str(week) + f' weeks and {str(day)} days ago'
					
		else:
			if week == 0:
				if day == 0:
					server_msg = f'{str(year)} years and ' + str(month) + ' month ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' +  str(month) + ' month and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{str(year)} years, ' + str(month) + ' month and 1 week ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' + str(month) + ' month, 1 week and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(month) + f' month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and ' + str(day) + ' days ago'
	
	server_info = server_date + f' ({server_msg})'
	
	s_e.add_field(name = "Created at", value = server_info, inline = False)
	
	if server.region == discord.VoiceRegion('amsterdam'):
		s_e.add_field(name = "Voice Region", value = ":flag_nl: Nethelands")
	elif server.region == discord.VoiceRegion('brazil'):
		s_e.add_field(name = "Voice Region", value = ":flag_br: Brazil")
	elif server.region == discord.VoiceRegion('dubai'):
		s_e.add_field(name = "Voice Region", value = ":flag_ae: United Arab Emirates")
	elif server.region == discord.VoiceRegion('europe'):
		s_e.add_field(name = "Voice Region", value = ":flag_eu: Europe")
	elif server.region == discord.VoiceRegion('frankfurt'):
		s_e.add_field(name = "Voice Region", value = ":flag_de: Germany")
	elif server.region == discord.VoiceRegion('hongkong'):
		s_e.add_field(name = "Voice Region", value = ":flag_hk: Hong Kong")
	elif server.region == discord.VoiceRegion('india'):
		s_e.add_field(name = "Voice Region", value = ":flag_in: India")
	elif server.region == discord.VoiceRegion('japan'):
		s_e.add_field(name = "Voice Region", value = ":flag_jp: Japan")
	elif server.region == discord.VoiceRegion('london'):
		s_e.add_field(name = "Voice Region", value = ":flag_gb: United Kingdom")
	elif server.region == discord.VoiceRegion('russia'):
		s_e.add_field(name = "Voice Region", value = ":flag_ru: Russia")
	elif server.region == discord.VoiceRegion('singapore'):
		s_e.add_field(name = "Voice Region", value = ":flag_sg: Singapore")
	elif server.region == discord.VoiceRegion('southafrica'):
		s_e.add_field(name = "Voice Region", value = ":flag_za: South Africa")
	elif server.region == discord.VoiceRegion('south_korea'):
		s_e.add_field(name = "Voice Region", value = ":flag_kr: South Korea")
	elif server.region == discord.VoiceRegion('sydney'):
		s_e.add_field(name = "Voice Region", value = ":flag_au: Australia")
	elif (server.region == discord.VoiceRegion('us_central') or server.region == discord.VoiceRegion('us_east')
	      or server.region == discord.VoiceRegion('vip_us_east') or server.region == discord.VoiceRegion('us_south')
	      or server.region == discord.VoiceRegion('us_west') or server.region == discord.VoiceRegion('vip_us_west')):
		s_e.add_field(name = "Voice Region", value = ":flag_us: USA")
	s_e.add_field(name = "Bans", value = f'<:banhammer:747471683140452391> {len(bans)}')
	s_e.set_thumbnail(url = server.icon_url)
	s_e.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = s_e)
	
@Bot.event
async def on_ready():
	print('Bot is online')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Ave Phoenix Ave CHVR'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

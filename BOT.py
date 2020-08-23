import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import datetime
import time

Bot = commands.Bot(command_prefix = '-')		
	
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
	
	if now_time_month < joined_time_month:
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
	mention = member.roles[0].name
	for i in range(1, len(member.roles)):
		mention += ', '
		mention += member.roles[i].mention
	emb.add_field(name = "Roles", value = mention, inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)

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
	
@Bot.event
async def on_ready():
	print('Bot is online')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Playing with developer'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

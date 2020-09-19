import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import datetime
import time

b_m = discord.Guild.me.mention

prefix = ['p!', b_m]

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def emoji(ctx, emoji:discord.Emoji):
	e_e = discord.Embed(title = f'`<:{emoji.name}:{emoji.id}>`', color = discord.Color.from_rgb(255, 0, 0))
	e_e.set_image(url = emoji.url)
	e_e.add_field(name = 'Name', value = emoji.name)
	e_e.add_field(name = 'ID', value = emoji.id)
	e_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = e_e)
	
@Bot.command()
async def ping(ctx):
	channel = ctx.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	latency = round(Bot.latency *1000)
	t = round((t2 - t1) * 1000)
	desc=f":heartbeat: **{latency}**ms \n :stopwatch: **{t}**ms"
	em = discord.Embed(title = ":ping_pong: Pong", description = desc, color = discord.Color.from_rgb(255, 0, 0))
	em.set_footer(text = f"Requested by {ctx.author.name}", icon_url = ctx.author.avatar_url)
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
async def membercount(ctx):
	guild = ctx.guild
	mention_msg = ''
	name_msg = ''
	bots = 0
	
	for i in range(0, len(guild.members)):
		if guild.members[i].bot == False:
			mention_msg += f'{guild.members[i].mention}, '
		else:
			bots += 1
	else:
		mention_msg = mention_msg[0 : len(mention_msg) - 2]
	mcm_e = discord.Embed(title = 'Server Members', color = discord.Color.from_rgb(255, 0, 0))
	mcm_e.add_field(name = f'Members ({len(guild.members) - bots})', value = mention_msg)
	mcm_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = mcm_e)
	
	for i in range(0, len(guild.members)):
		if guild.members[i].bot == False:
			name_msg += f'{str(guild.members[i])}, '
	else:
		name_msg = name_msg[0 : len(name_msg) - 2]
	mcn_e = discord.Embed(title = 'Server Members', color = discord.Color.from_rgb(255, 0, 0))
	mcn_e.add_field(name = f'Members ({len(guild.members) - bots})', value = name_msg)
	mcn_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = mcn_e)
						
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
async def avatar(ctx, member = None):
	if member == None:
		member = ctx.author
	else:
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
				if member != None:
					await ctx.send('You wrote member index incorectly.')
	a_e = discord.Embed(title = f'{member} avatar', color = discord.Color.from_rgb(255, 0, 0))
	a_e.set_image(url = member.avatar_url)
	a_e.set_footer(text = f'Caused by: {ctx.author}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = a_e)

def calculator(num):
	
	num = str(num)
	
	if num[8:10] == '01':
		day = num[9:10] + 'st'
	elif num[8:10] == '02':
		day = num[9:10] + 'nd'
	elif num[8:10] == '03':
		day = num[9:10] + 'rd'
	elif num[8:10] == '04' or num[8:10] == '05' or num[8:10] == '06' or num[8:10] == '07' or num[8:10] == '08' or num[8:10] == '09':
		day = num[9:10] + 'th'
	elif num[8:10] == '21' or num[8:10] == '31':
		day = num[8:10] + 'st'
	elif num[8:10] == '22':
		day = num[8:10] + 'nd'
	elif num[8:10] == '23':
		day = num[8:10] + 'rd'
	else:
		day = num[8:10] + 'th'
		
	if num[5:7] == '01':
		month = ' February '
	elif num[5:7] == '02':
		month = ' January '
	elif num[5:7] == '03':
		month = ' March '
	elif num[5:7] == '04':
		month = ' April '
	elif num[5:7] == '05':
		month = ' May '
	elif num[5:7] == '06':
		month = ' June '
	elif num[5:7] == '07':
		month = ' July '
	elif num[5:7] == '08':
		month = ' August '
	elif num[5:7] == '09':
		month = ' September '
	elif num[5:7] == '10':
		month = ' October '
	elif num[5:7] == '11':
		month = ' November '
	elif num[5:7] == '12':
		month = ' December '
		
	date = day + month + f'{num[2:4]} '
	
	now_year = int(str(datetime.date.today())[0:4])
	year = int(num[0:4])

	
	now_month = int(str(datetime.date.today())[5:7])
	month = int(num[5:7])
	
	if now_month == 1 or now_month == 3 or now_month == 5 or now_month == 7 or now_month == 8 or now_month == 10 or now_month == 12:
		day_bonus = 31
	elif now_month == 2:
		day_bonus = 28
	else:
		day_bonus = 30
	
	now_day = int(str(datetime.date.today())[8:10])
	day = int(num[8:10])
	week = 0
	
	if now_day < day:
		now_month -= 1
		now_day += day_bonus
		day = now_day - day
	else:
		day = now_day - day
	
	if now_month < month:
		now_year -= 1
		now_month += 12
		month = now_month - month
	else:
		month = now_month - month
	
	while day // 7:
		week += 1
		day -= 7
	
	year = now_year - year
	
	if year == 0:
		if month == 0:
			if week == 0:
				if day == 0:
					msg = 'Today'
				elif day == 1:
					msg = '1 day ago'
				else:
					msg = f'{day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 week ago'
				elif day == 1:
					msg = '1 week and 1 day ago'
				else:
					msg = f'1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{week} weeks ago'
				elif day == 1:
					msg = f'{week} weeks and 1 day ago'
				else:
					msg = f'{week} weeks and {day} days ago'
		elif month == 1:
			if week == 0:
				if day == 0:
					msg = '1 month ago'
				elif day == 1:
					msg = '1 month and 1 day ago'
				else:
					msg = f'1 month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 month and 1 week ago'
				elif day == 1:
					msg = '1 month, 1 week and 1 day ago'
				else:
					msg = f'1 month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 month {week} weeks ago'
				elif day == 1:
					msg = f'1 month, {week} weeks and 1 day ago'
				else:
					msg = f'1 month, {week} weeks and {day} days ago'
					
		else:
			if week == 0:
				if day == 0:
					msg = f'{month} month ago'
				elif day == 1:
					msg = f'{month} month and 1 day ago'
				else:
					msg = f'{month} month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{month} month and 1 week ago'
				elif day == 1:
					msg = f'{month} month, 1 week and 1 day ago'
				else:
					msg = f'{month} month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{month} month and {week} weeks ago'
				elif day == 1:
					msg = f'{month} month and {week} weeks and 1 day ago'
				else:
					msg = f'{month} month and {week} weeks and {day} days ago'
					
	elif year == 1:
		if month == 0:
			if week == 0:
				if day == 0:
					msg = '1 year ago'
				elif day == 1:
					msg = '1 year and 1 day ago'
				else:
					msg = f'1 year and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 year and 1 week ago'
				elif day == 1:
					msg = '1 year, 1 week and 1 day ago'
				else:
					msg = f'1 year, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 year and {week} weeks ago'
				elif day == 1:
					msg = f'1 year, {week} weeks and 1 day ago'
				else:
					msg = f'1 year, {week} weeks and {day} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					msg = '1 year and 1 month ago'
				elif day == 1:
					msg = '1 year, 1 month and 1 day ago'
				else:
					msg = f'1 year, 1 month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 year, 1 month and 1 week ago'
				elif day == 1:
					msg = '1 year, 1 month, 1 week and 1 day ago'
				else:
					msg = f'1 year, 1 month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 year, 1 month and {week} weeks ago'
				elif day == 1:
					msg = f'1 year, 1 month, {week} weeks and 1 day ago'
				else:
					msg = f'1 year, 1 month, {week} weeks and {day} days ago'
					
		else:
			if week == 0:
				if day == 0:
					msg = f'1 year and {month} month ago'
				elif day == 1:
					msg = f'1 year, {month} month and 1 day ago'
				else:
					msg = f'1 year, {month} month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'1 year, {month} month and 1 week ago'
				elif day == 1:
					msg = f'1 year, {month} month, 1 week and 1 day ago'
				else:
					msg = f'1 year, {month} month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 year, {month} month and {week} weeks ago'
				elif day == 1:
					msg = f'1 year, {month} month, {week} weeks and 1 day ago'
				else:
					msg = f'1 year, {month} month, {week} weeks and {day} days ago'
	else:
		if month == 0:
			if week == 0:
				if day == 0:
					msg = f'{year} years ago'
				elif day == 1:
					msg = f'{year} years and 1 day ago'
				else:
					msg = f'{year} years and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{year} years and 1 week ago'
				elif day == 1:
					msg = f'{year} years, 1 week and 1 day ago'
				else:
					msg = f'{year} years, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{year} years and {week} weeks ago'
				elif day == 1:
					msg = f'{year} years, {week} weeks and 1 day ago'
				else:
					msg = f'{year} years, {week} weeks and {day} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					msg = f'{year} years and 1 month ago'
				elif day == 1:
					msg = f'{year} years, 1 month and 1 day ago'
				else:
					msg = f'{year} years, 1 month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{year} years, 1 month and 1 week ago'
				elif day == 1:
					msg = f'{year} years, 1 month, 1 week and 1 day ago'
				else:
					msg = f'{year} years, 1 month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{year} years, 1 month and {week} weeks ago'
				elif day == 1:
					msg = f'{year} years, 1 month, {week} weeks and 1 day ago'
				else:
					msg = f'{year} years, 1 month, {week} weeks and {day} days ago'
					
		else:
			if week == 0:
				if day == 0:
					msg = f'{year} years and {month} month ago'
				elif day == 1:
					msg = f'{year} years, {month} month and 1 day ago'
				else:
					msg = f'{year} years, {month} month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{year} years, {month} month and 1 week ago'
				elif day == 1:
					msg = f'{year} years, {month} month, 1 week and 1 day ago'
				else:
					msg = f'{year} years, {month} month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{year} years, {month} month and {week} weeks ago'
				elif day == 1:
					msg = f'{year} years, {month} month and {week} weeks and 1 day ago'
				else:
					msg = f'{year} years, {month} month and {week} weeks and {day} days ago'
	
	info = date + f'({msg})'
	
	return info

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
				await ctx.send('You wrote member index incorectly.')
	
	emb = discord.Embed(title = 'Member information', description = member.mention, color = member.top_role.color)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.add_field(name = "Joined server", value = calculator(member.joined_at), inline = False)
	emb.add_field(name = "Created account", value = calculator(member.created_at), inline = False)
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
async def role(ctx, role = None):
	
	guild = ctx.guild
	role_list = guild.roles
	role_stop = 0
	
	for i in range(0, len(role_list)):
		if role == role_list[i].name or role == str(role_list[i].id) or role == role_list[i].mention:
			role_stop = True
			role = role_list[i]
	else:
		if role_stop == False:	
			await ctx.send('You didn\'t write role index.')
				
	r_e = discord.Embed(title = 'Role information', color = role.color)
	r_e.add_field(name = 'Name', value = role.name)
	r_e.add_field(name = 'ID', value = role.id)
	r_e.add_field(name = 'Mention', value = f'`{role.mention}`')
	r_e.add_field(name = 'Color', value = role.color)
	r_e.add_field(name = 'Members', value = len(role.members))
	if role.is_default() == True:
		r_e.add_field(name = 'Default', value = 'Yes')
	else:
		r_e.add_field(name = 'Default', value = 'No')
	r_e.add_field(name = 'Position (from top)', value = f'{len(ctx.guild.roles) - role.position}/{len(ctx.guild.roles)}')
	if role.hoist == True:
		r_e.add_field(name = 'Hoisted', value = 'Yes')
	else:
		r_e.add_field(name = 'Hoisted', value = 'No')
	if role.mentionable == True:
		r_e.add_field(name = 'Mentionable', value = 'Yes')
	else:
		r_e.add_field(name = 'Mentionable', value = 'No')
	r_e.add_field(name = 'Created at', value = calculator(role.created_at), inline = False)
		
	if role.permissions.administrator == True:
		r_e.add_field(name = 'Key Permissions', value = 'Administrator (all permissions)', inline = False)
	else:
		permissions = ''
		if role.permissions.kick_members == True:
			permissions += 'Kick members, '
		if role.permissions.ban_members == True:
			permissions += 'Ban members, '
		if role.permissions.manage_channels == True:
			permissions += f'Manage channels, '
		if role.permissions.manage_guild == True:
			permissions += f'Manage server, '
		if role.permissions.manage_messages == True:
			permissions += f'Manage messages, '
		if role.permissions.mention_everyone == True:
			permissions += f'Mention everyone, '
		if role.permissions.mute_members == True:
			permissions += f'Mute members, '
		if role.permissions.deafen_members == True:
			permissions += f'Deafen members, '
		if role.permissions.move_members == True:
			permissions += f'Move members, '
		if role.permissions.manage_nicknames == True:
			permissions += f'Manage nicknames, '
		if role.permissions.manage_roles == True:
			permissions += f'Manage roles, '
		if role.permissions.manage_webhooks == True:
			permissions += f'Manage webhooks, '
		if role.permissions.manage_emojis == True:
			permissions += f'Manage emojis, '
		if role.permissions.view_audit_log == True:
			permissions += f'View audit log, '
		if len(permissions) == 0:
			r_e.add_field(name = 'Key Permissions', value = 'Don\'t have any key permission.', inline = False)
		else:
			permissions = permissions[0 : len(permissions) - 2]
			r_e.add_field(name = 'Key Permissions', value = permissions, inline = False)
		
	await ctx.send(embed = r_e)

@Bot.command()
async def server(ctx):
	server = ctx.guild
	online_members = 0
	inactive_members = 0
	busy_members = 0
	bot_members = 0
	bans = await server.bans()
	s_e = discord.Embed(title = 'Server information', description = server.description, color = discord.Color.from_rgb(255, 0, 0))
	s_e.add_field(name = "Server ID", value = server.id)
	s_e.add_field(name = "Name", value = server.name)
	s_e.add_field(name = "Server Owner", value = server.owner.mention)
	for i in range(0, len(server.members)):
		if server.members[i].status == discord.Status.online or server.members[i].status == discord.Status.idle or server.members[i].status == discord.Status.dnd:
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
	statuses = (f'<:online:747352635643920385> **{online_members}** Online \n<:idle:747490969984958544> **{inactive_members}** Inactive'
		   +f'\n<:dnd:747492056087134289> **{busy_members}** Busy \n<:offline:747355444250542141> **{len(server.members) - bot_members}** Offline')
	s_e.add_field(name = "People statuses", value = statuses)
	members = (f'**{len(server.members)}** All \n**{len(server.members) - bot_members}** People \n**{bot_members}** Bots')
	s_e.add_field(name = "Server members", value = members)
	channels = f'<:textchannel:747403102650368032> {len(server.text_channels)} Text \n<:voicechannel:747410314630266960> {len(server.voice_channels)} Voice'
	s_e.add_field(name = "Channels", value = channels)
	s_e.add_field(name = "Emojis", value = f':grinning: {len(server.emojis)}')
	s_e.add_field(name = "Bans", value = f'<:banhammer:747471683140452391> {len(bans)}')
	s_e.add_field(name = "Roles", value = len(server.roles))
	
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
	s_e.add_field(name = "Created at", value = calculator(server.created_at), inline = False)
	s_e.set_thumbnail(url = server.icon_url)
	s_e.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = s_e)
	
@Bot.command()
async def channel(ctx, channel = None):
	
	guild = ctx.guild
	role_list = guild.roles
	r_roles_quantity = 0
	r_roles_msg = ''
	read_list = []
	antiread_list = []
	w_roles_quantity = 0
	w_roles_msg = ''
	h_roles_quantity = 0
	h_roles_msg = ''
	channel_list = guild.text_channels
	channel_stop = False
	special = False
	fake = 0
	
	for i in range(0, len(channel_list)):
		if channel == channel_list[i].name or channel == str(channel_list[i].id) or channel == channel_list[i].mention:
			channel_stop = True
			channel = channel_list[i]
	else:
		if channel_stop == False:
			if channel == None:	
				channel = ctx.channel
			else:
				await ctx.send('You wrote channel index incorectly.')
	
	for i in range(0, len(role_list)):
		if channel.overwrites_for(role_list[0]).read_messages == False:
			if role_list[i].permissions.read_messages == True:
				if channel.overwrites_for(role_list[i]).read_messages == True or role_list[i].permissions.administrator == True:
					r_roles_quantity += 1
					r_roles_msg += f'{role_list[i].mention}, '
					read_list.append(role_list[i])
			else:
				if channel.overwrites_for(role_list[i]).read_messages == True or role_list[i].permissions.administrator == True:
					r_roles_quantity += 1
					r_roles_msg += f'{role_list[i].mention}, '
					read_list.append(role_list[i])
		else:
			if channel.overwrites_for(role_list[i]).read_messages == False:
				fake +=  1
				r_roles_msg += f'{role_list[i].mention}, '
				antiread_list.append(role_list[i])
				special = True
			else:
				read_list.append(role_list[i])
			r_roles_quantity = len(role_list) - fake
	else:
		if special == True:
			read_list.append(role_list[0])
			r_roles_msg = f'{role_list[0]} except {r_roles_msg[0 : len(r_roles_msg) - 2]}'
		else:
			r_roles_msg = role_list[0].name
		special = False
		fake = 0
		
	for i in range(0, len(role_list)):
		if role_list[i] in read_list and role_list[i] not in antiread_list:
			if channel.overwrites_for(role_list[0]).send_messages == False:
				if role_list[i].permissions.send_messages == True:
					if (channel.overwrites_for(role_list[i]).send_messages == True or role_list[i].permissions.administrator == True
					    or channel.overwrites_for(role_list[i]).send_messages == None):
						w_roles_quantity += 1
						w_roles_msg += f'{role_list[i].mention}, '
				else:
					if channel.overwrites_for(role_list[i]).send_messages == True or role_list[i].permissions.administrator == True:
						w_roles_quantity += 1
						w_roles_msg += f'{role_list[i].mention}, '
			else:
				if channel.overwrites_for(role_list[i]).send_messages == False:
					fake +=  1
					w_roles_msg += f'{role_list[i].mention}, '
					special = True
				w_roles_quantity = len(read_list) - fake
	else:
		if special == True:
			w_roles_msg = f'{role_list[0]} except {w_roles_msg[0 : len(w_roles_msg) - 2]}'
		else:
			w_roles_msg = role_list[0].name
		special = False
		fake = 0
		
	for i in range(0, len(role_list)):
		if role_list[i] in read_list:
			if channel.overwrites_for(role_list[0]).send_messages == False:
				if role_list[i].permissions.read_message_history == True:
					if (channel.overwrites_for(role_list[i]).read_message_history == True or role_list[i].permissions.administrator == True
					    or channel.overwrites_for(role_list[i]).read_message_history == None):
						h_roles_quantity += 1
						h_roles_msg += f'{role_list[i].mention}, '
				else:
					if channel.overwrites_for(role_list[i]).read_message_history == True or role_list[i].permissions.administrator == True:
						h_roles_quantity += 1
						h_roles_msg += f'{role_list[i].mention}, '
			else:
				if channel.overwrites_for(role_list[i]).read_message_history == False:
					fake +=  1
					h_roles_msg += f'{role_list[i].mention}, '
					special = True
				h_roles_quantity = len(read_list) - fake
	else:
		if special == True:
			h_roles_msg = f'{role_list[0]} except {h_roles_msg[0 : len(h_roles_msg) - 2]}'
		else:
			h_roles_msg = role_list[0].name
		special = False
		fake = 0
	
	c_e = discord.Embed(title = 'Channel information', color = discord.Color.from_rgb(255, 0, 0))
	c_e.add_field(name = 'Name', value = channel.name)
	c_e.add_field(name = 'ID', value = channel.id)
	c_e.add_field(name = 'Mention', value = f'`{channel.mention}`')
	if channel.category != None:
		c_e.add_field(name = 'Category', value = channel.category)
	if channel.is_nsfw() == True:
		c_e.add_field(name = 'NSFW', value = 'Yes')
	else:
		c_e.add_field(name = 'NSFW', value = 'No')
	if channel.topic != None:
		c_e.add_field(name = 'Topic', value = channel.topic, inline = False)
	role = ctx.author.roles[0]
	c_e.add_field(name = f'Roles that can view this channel ({r_roles_quantity})', value = r_roles_msg, inline = False)
	c_e.add_field(name = f'Roles that can write in this channel ({w_roles_quantity})', value = w_roles_msg, inline = False)
	c_e.add_field(name = f'Roles that can read this channel ({h_roles_quantity})', value = h_roles_msg, inline = False)
	c_e.add_field(name = 'Created at', value = calculator(channel.created_at), inline = False)
	c_e.set_footer(text = f'Caused by: {ctx.author}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = c_e)
	
@Bot.event
async def on_ready():
	print('Bot is online')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Ave Phoenix Ave CHVR'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

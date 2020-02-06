import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def hello(ctx):
    	await ctx.send(f"Hello {ctx.author.mention}")

@Bot.command()
async def say(ctx, *, text):
	await ctx.send(text)
	
@Bot.command()
async def clear(ctx):
	await ctx.channel.purge(limit=10000)
		
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
async def user(ctx, member: discord.Member):
	emb = discord.Embed(title = str(member), description = member.mention, color = member.top_role.color)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
	if member.top_role == member.roles[0]:
		emb.add_field(name = "Highest role", value = member.top_role, inline = False)
	else:
		emb.add_field(name = "Highest role", value = member.top_role.mention, inline = False)
	for i in range(2):
		try:
    			f1 = open(f'{member}.txt', 'w')
    			f1.write(f'{member.roles}')
		finally:
			f1.close()
	try:
		f2 = open(f'{member}.txt', 'r')
		info = f2.read()
	finally:
		f2.close()
	if len(info) > 47:
		emb.add_field(name = 'Roles', value = member.roles[0], inline = True)
		for i in range(47, len(info)):
    			if info[i] == 'd':
        			role_id = info[i + 2 : i + 20]
				emb.add_field(name = None, value = f'<@&{role_id}>', inline = False)
	else:
		emb.add_field(name = 'Roles', value = member.roles[0], inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)
        
@Bot.event
async def on_ready():
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Playing with developer'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

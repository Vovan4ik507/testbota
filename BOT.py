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
async def say(ctx, *, arg):
	await ctx.send(arg)
	
@Bot.command()
async def role(ctx, member: discord.Member):
	await ctx.send(member.roles)

@Bot.command()
async def count(ctx, member: discord.Member):
	await ctx.send(len(member.roles))

@Bot.command()
async def info(ctx, member: discord.Member):
	await ctx.send(member.roles[0])
	
@Bot.command()
async def roles(ctx, member: discord.Member):
	id = []
	for role in range(len(member.roles)):
		id[role] += member.roles[9:18]
		await ctx.send('<@{id[role}')
		
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
	emb.add_field(name = "Highest role", value = member.top_role.mention, inline=False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

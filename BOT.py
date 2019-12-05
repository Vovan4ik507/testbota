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
	author = member
	emb = discord.Embed(title = f"Info about {author}", color = 0x39d0d6)
	emb.add_field(name = "ID", value = author.id, inline = False)
	emb.add_field(name = "Joined server at", value = author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
	emb.add_field(name = "Created account at", value = author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
	emb.add_field(name= "Their roles: ", value=" ".join([role.mention for role in roles]), inline=False)
  	emb.add_field(name= "Highest role: ", value=member.top_role.mention, inline=False)
	emb.set_thumbnail(url = author.avatar_url)
	emb.set_author(name = f"Caused by: {str(ctx.author)}")
	await ctx.send(embed = emb)
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

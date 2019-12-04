import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

Bot = commands.Bot(command_prefix = '-')

@Bot.command()
async def hello(ctx):
    	await ctx.send(f"Hello {ctx.message.author.mention}")

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
	emb = discord.Embed(title = f"Info about {member.mention}", color = 0x39d0d6)
	if member == None:
		emb.add_field(name = "ID", value = ctx.message.author.id, inline = False)
		emb.add_field(name = "Joined server at", value = str(ctx.message.author.joined_at)[:19], inline = False)
		emb.add_field(name = "Created account at", value = str(ctx.message.author.created_at)[:19], inline = False)
		emb.set_thumbnail(url = ctx.message.author.avatar_url)
		emb.set_author(name = f"Caused by: {ctx.message.author.name + '#' + str(ctx.message.author.discriminator)}")
	else:
		emb.add_field(name = "ID", value = member.id, inline = False)
		emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
		emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
		emb.set_thumbnail(url = member.avatar_url)
		emb.set_author(name = f"Caused by: {member.name + '#' + str(member.discriminator)}")
	await ctx.send(embed = emb)
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

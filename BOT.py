import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = '-'

bot = commands.Bot(command_prefix = prefix)

Bot.remove_command('help')

@bot.command()
async def hello(ctx):
    	await ctx.send("Hello {}".format(ctx.message.author.mention))

@bot.command()
async def say(ctx, *, arg):
	await ctx.send(arg)
	
@bot.command()
async def help(ctx):
	embed = discord.Embed(title = "My commands", color = 0x39d0d6)
	embed.add_field(name = f"{prefix}ping", value = "Show ping")
	embed.add_field(name = f"{prefix}user", value = "Information about anyone in your server")
	await ctx.sendembed = embed)

@bot.command()
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
    em.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)
	
@Bot.command()
async def user(ctx, member: discord.Member):
	emb = discord.Embed(title = f"Info about {member.mention}", color = 0x39d0d6)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_author(name = member.name + '#' + str(member.discriminator))
	emb.set_footer(text = f"Caused by: {member.name}", icon_url = member.avatar_url)
	await ctx.send(embed = emb)
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

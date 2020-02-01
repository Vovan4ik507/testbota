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
async def roles(ctx, member: discord.Member):
	e = discord.Embed(title = 'Roles', color = 0x39d0d6)
	if member.top_role == '@everyone':
		e.add_field(name = 'Role', value = member.top_role)
	else:
		e.add_field(name = 'Role', value = member.top_role.mention)
	e.add_field(name = 'Roles', value = member.roles)
	await ctx.send(embed = e)

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
	emb = discord.Embed(name = str(member), color = 0x39d0d6)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
	emb.add_field(name = "Highest role", value = member.top_role.mention, inline=False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_author(name = member.mention)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}")
	await ctx.send(embed = emb)
	
@Bot.command()
async def game(ctx, user):
	comp = random.choice(['камень', 'бумага', 'ножницы'])
    if user == 'камень' and comp == 'камень':
        await ctx.send('Ничья. Камень против камня.')
    elif user == 'камень' and comp == 'бумага':
        await ctx.send('Ви проиграли. Камень против бумаги.')
    elif user == 'камень' and comp == 'ножницы':
        await ctx.send('Ви выиграли. Камень против ножниц.')
    elif user == 'бумага' and comp == 'камень':
        await ctx.send('Ви выиграли. Бумага против камня.')
    elif user == 'бумага' and comp == 'бумага':
        await ctx.send('Ничья. Бумага против бумаги.')
    elif user == 'бумага' and comp == 'ножницы':
        await ctx.send('Ви проиграли. Бумага против ножниц.')
    elif user == 'ножницы' and comp == 'ножницы':
        await ctx.send('Ничья. Ножницы против ножниц.')
    elif user == 'ножницы' and comp == 'бумага':
        await ctx.send('Ви выиграли. Ножницы против бумаги.')
    elif user == 'ножницы' and comp == 'камень':
        await ctx.send('Ви проиграли. Ножницы против камня.')
        
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

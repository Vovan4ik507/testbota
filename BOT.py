import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '-')
clearly = False

@Bot.command()
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))
    await ctx.message.delete()
    
@Bot.command()
async def info(ctx, user: discord.User):
	emb = discord/Embed(title = "Info about {}".format(user.mention), color=0x39d0d6)
	emd.add_field(name = "Name", value = user.mention)
	emb.add_field(name = "Joined at", value = str(user.joined at)[:23])
	emb.add_field(name = "ID", value = user.id)
	if user.game != None:
		emb.add_field(name = "Game", value = user.game)
	emb.set_thumbnail(url = user.avatar_url)
	emb.set_author(name = Bot.user.name, url = "https://discordapp.com/oauth2/authorize?client_id=513405344718782464&scope=bot&permissions=8")
	emb.set_footer(text = "Вызвано: {}".format(user.mention), icon_url = user.avater_url)
	await ctx.send(embed = emb)
	await ctx.message.delete()    
    
@Bot.command()
async def clean(ctx):
    await ctx.message.delete()
    
@Bot.command()
async def mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name="Mute")
    await member.add_roles(mute_role)

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))

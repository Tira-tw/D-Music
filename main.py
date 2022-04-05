import os
import discord
import keep_alive
from discord import Intents
from discord.ext import commands
from pretty_help import PrettyHelp

owners = [848164182334898216]
activity = discord.Activity(type=discord.ActivityType.playing, name="打上D!help可以獲得所有指令")
bot = commands.Bot(command_prefix="D!", activity=activity, owner_ids = set(owners), intents=Intents.all())
ending_note = "使用 D!help 來顯示這個訊息\n這是一個幫助訊息，能列出所有指令，好讓你能輕鬆自在的使用這個機器人"
bot.help_command = PrettyHelp(color=0xffffff, ending_note=ending_note)

@bot.event
#當機器人完成啟動時
async def on_ready():
	print('> 目前登入身分：', bot.user)
	print('> bot is online')
@bot.command()
async def load(ctx, extension):
  """開發者專用"""
  is_owner = await ctx.bot.is_owner(ctx.author)
  if is_owner:
	  bot.load_extension(f'cogs.{extension}')
	  await ctx.send(f'載入{extension}完成')
  else:
    await ctx.send("你好像沒有權限使用這個指令欸你卻定你是開發者嗎?")

@bot.command()
async def unload(ctx, extension):
  """開發者專用"""
  is_owner = await ctx.bot.is_owner(ctx.author)
  if is_owner:
	  bot.unload_extension(f'cogs.{extension}')
	  await ctx.send(f'卸載{extension}完成')
  else:
    await ctx.send("你好像沒有權限使用這個指令欸你卻定你是開發者嗎?")

@bot.command()
async def reload(ctx, extension):
  """開發者專用"""
  is_owner = await ctx.bot.is_owner(ctx.author)
  if is_owner:
	  bot.reload_extension(f'cogs.{extension}')
	  await ctx.send(f'重新載入{extension}完成')
  else:
    await ctx.send("你好像沒有權限使用這個指令欸你卻定你是開發者嗎?")

@bot.command()
async def reloadall(ctx):
  """開發者專用"""
  is_owner = await ctx.bot.is_owner(ctx.author)
  if is_owner:
    for file in os.listdir("cogs"):
      if file.endswith(".py"):
        name = file[:-3]
        bot.reload_extension(f"cogs.{name}")
    await ctx.send("重新載入成功")
  else:
    await ctx.send("你好像沒有權限使用這個指令欸你卻定你是開發者嗎?")

for Filename in os.listdir('./cogs'):
	if Filename.endswith('.py'):
		bot.load_extension(f'cogs.{Filename[:-3]}')

if __name__ == "__main__":
	keep_alive.keep_alive()
	bot.run(os.environ['TOKEN'])
    #TOKEN HERE
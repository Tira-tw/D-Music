import discord
from discord.ext import commands

class Event(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
"""
  @commands.Cog.listener(name='on_command')
  async def print(self, ctx):
    server = ctx.guild.name
    user = ctx.author
    command = ctx.message.content
    msg = f'{server} > {user} > {command}'
    ch = self.bot.get_channel(916956523937271858)
    await ch.send(msg)
    print(msg)
"""
def setup(bot):
  bot.add_cog(Event(bot))
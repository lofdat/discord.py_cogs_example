import discord
from discord.ext import commands

class mycog:
  """my cogerino"""
  # these next two lines, always keep in all ur cogs !!
  def __init__(self, bot):
    self.bot = bot
  
  # In cogs, always use @commands.command, regardless of your bot's name !!
  # self = always required
  # to get the context, use pass_context=True and put ctx as your first arg (after self ofc)
  @commands.command(pass_context=True)
  async def sayhi(self, ctx):
    await self.bot.say("Hi, " + ctx.message.author.name + "!")
  
def setup(bot):
  bot.add_cog(mycog(bot))
  # setup the cogs. always keep
  # replace mycog with your class name at the top!

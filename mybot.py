import discord
from discord.ext import commands

mybotdescription = ```An example bot to showoff discord.ext.commands``` # shown in help menu

# let's make the bot
mybot = commands.Bot(command_prefix='m!', description=mybotdescription)

# example event
@mybot.event
async def on_ready():
  print('im in boiz!!!')
  print('username' + mybot.user.name)
  # LOAD IN THOSE COGS BOI!!!
  mybot.load_extension("cogs.mycog")
  # cogs.mycog = <ProgramDir>/cogs/mycog.py
  # ;P
  
# example non-cog'd command
@bot.command()
async def add(left: int, right: int):
  """Adds two numbers ;P"""
  # ABOVE STRING IS THE HELP LISTING FOR THIS COMMAND !!
  await bot.say(left + right) # <-- bot.say can only be used in commands !!
  

# run that shit boi!
bot.run('myshittokenxd')

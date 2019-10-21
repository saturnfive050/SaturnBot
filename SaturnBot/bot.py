# SETUP STUFF

import traceback
from importlib import reload
from os import listdir
from os.path import isfile, join

import discord
from discord.ext import commands

# =======================================================================================

owner_id = 375375057138089986       # put user id here
STATUS = 'with Saturnfive\'s emotions'       # put desired "playing" status between quotes
PREFIX = 's!'

# =======================================================================================

bot = commands.Bot(command_prefix=PREFIX)


async def is_owner(ctx):
    return ctx.author.id == owner_id


# --------------------------------------------------------------------
# EVENTS

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    status = STATUS
    await bot.change_presence(activity=discord.Game(status))


# --------------------------------------------------------------------

bot.load_extension("cogs.Moderation")
bot.load_extension("cogs.Owner")
bot.load_extension("cogs.CogCommands")
bot.load_extension("cogs.User")
bot.load_extension("cogs.Voice")
# --------------------------------------------------------------------
import important
bot.run(important.TOKEN)

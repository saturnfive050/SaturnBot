import discord
from discord.ext import commands
import asyncio
import random
import os
from os import listdir
from os.path import isfile, join
import sys, traceback


async def is_owner(ctx):
    return ctx.author.id == 375375057138089986



# --------------------------------------------------------------------


class CogCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(is_owner)
    async def list_cogs(self, ctx):
        """Lists all available cogs"""
        print(f'[{ctx.author} / {ctx.guild.name} / {ctx.channel.name}] Cog-list command used"')
        embed = discord.Embed(title="Available Extensions:", description=f"&load/unload [extension]",
                              color=discord.Color.dark_green())
        for folder in listdir("./"):
            if not isfile(folder):
                print(f"Discovered directory {folder}")
                for extension in [f.replace('.py', '') for f in listdir(folder) if isfile(join(folder, f))]:
                    print(f'- {extension}')
                    embed.add_field(name=f"{folder}.{extension}",
                                    value=f"-------------------------------------------")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, extension_name: str):
        """Loads an extension"""
        print(f'[{ctx.author} / {ctx.guild.name} / {ctx.channel.name}] Loaded cog {extension_name}"')
        try:
            self.bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            print("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await ctx.send("{} loaded.".format(extension_name))
        print("{} loaded.".format(extension_name))

    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, extension_name: str):
        """Unloads an extension"""
        print(f'[{ctx.author} / {ctx.guild.name} / {ctx.channel.name}] Unloaded cog {extension_name}"')
        if extension_name == "startup_all.CogCommands":
            print("attempt to unload CogCommands was blocked")
            await ctx.send("You can't unload CogCommands!")
        else:
            self.bot.unload_extension(extension_name)
            await ctx.send("{} unloaded.".format(extension_name))
            print("{} unloaded.".format(extension_name))

# --------------------------------------------------------------------


def setup(bot):
    bot.add_cog(CogCommands(bot))

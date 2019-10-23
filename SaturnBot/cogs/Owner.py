import discord
from discord.ext import commands

async def is_owner(ctx):
    return ctx.author.id == 375375057138089986


# --------------------------------------------------------------------


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(is_owner)
    async def say(self, ctx, channel: discord.TextChannel, *, things: commands.clean_content):
        '''OWNER ONLY: Messages a channel'''
        await channel.send(things)
        await ctx.send("sent to channel")

    @commands.command()
    @commands.check(is_owner)
    async def spam(self, ctx):
        '''OWNER ONLY: Sends a message to every channel'''
        for channel in ctx.guild.text_channels:
            await channel.send('<:beeg_yoshi:559146255771500554>')

    @commands.command()
    @commands.check(is_owner)
    async def dm(self, ctx, member: discord.Member, *, stuff: commands.clean_content):
        '''OWNER ONLY: DM's a user'''
        await member.send(stuff)
        await ctx.send("sent to user")

   

# --------------------------------------------------------------------


def setup(bot):
    bot.add_cog(Owner(bot))

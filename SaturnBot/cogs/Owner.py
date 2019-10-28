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
        '''OWNER ONLY: Adds 100 channels, sends a message to every channel and then deletes those 100'''
        guild = ctx.guild
        for x in range(100):
            await guild.create_text_channel(name='spam')
        for channel in ctx.guild.text_channels:
            await channel.send('<a:crabrave:628709260964134949>')
        for channel in ctx.guild.channels:
            if channel.name == "spam":
                await channel.delete()

    @commands.command()
    @commands.check(is_owner)
    async def dm(self, ctx, member: discord.Member, *, stuff: commands.clean_content):
        '''OWNER ONLY: DM's a user'''
        await member.send(stuff)
        await ctx.send("sent to user")

   

# --------------------------------------------------------------------


def setup(bot):
    bot.add_cog(Owner(bot))

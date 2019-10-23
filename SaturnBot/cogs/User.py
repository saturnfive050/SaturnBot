import discord
from discord.ext import commands

VERSION = 'Saturn v0.1.1a'           # replace part inside quotes with desired output
FEATURES = 'a bot.'    # replace part inside quotes with desired output
PREFIX = 's!'                        # change to desired prefix

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        """Bot responds to you"""
        await ctx.send('Shut the frick up')


    @commands.command()
    async def botinfo(self, ctx):
        """Basic Info about the bot"""
        embed = discord.Embed(title=VERSION, description=FEATURES, color=discord.Color.dark_green())
        embed.add_field(name="Prefix", value=PREFIX)
        await ctx.send(embed=embed)


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        """info about a user"""
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color,timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)

        embed.add_field(name="Created:", value=member.created_at.strftime("%a,%#d %B %Y,%I:%M %p UTC"))
        embed.add_field(name="Joined:", value=member.joined_at.strftime("%a,%#d %B %Y,%I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name=f"Highest Role", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)

        await ctx.send(embed=embed)

    @commands.command()
    async def link(self, ctx):
        '''Gives you the bot's invite link'''
        await ctx.send('<https://discordapp.com/oauth2/authorize?&client_id=633853231587655681&scope=bot&permissions=0>')

def setup(bot):
    bot.add_cog(User(bot))

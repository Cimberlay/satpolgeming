import discord
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ban.py aman.")

    @commands.command()
    @commands.has_role("🤖 | Official Bot")
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} Udah Gw Ban")


async def setup(bot):
    await bot.add_cog(ban(bot))
import discord
from discord.ext import commands

class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("clear.py aman.")

    @commands.command(aliases=['clean','cls'])
    @commands.has_role("🛡️ · Staff")
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)


async def setup(bot):
    await bot.add_cog(clear(bot))
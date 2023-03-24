import discord
from discord.ext import commands
import time


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py aman.")

    @commands.command()
    async def ping(self, ctx:commands.Context):
        before = time.monotonic()
        message = await ctx.send(":ping_pong: Pong !")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f":ping_pong: Pong ! in `{float(round(ping/1000.0,3))}s` ||{int(ping)}ms||")


async def setup(bot):
    await bot.add_cog(ping(bot))
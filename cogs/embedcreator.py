import discord
from discord.ext import commands

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("embedcreator.py aman.")


    @commands.command()
    @commands.has_role("🛡️ · Staff")
    async def create_embed(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("Apa judul dari embed kamu?")
        title = await self.bot.wait_for("message", check=check, timeout=500)

        await ctx.send("Apa deskripsi dari embed kamu?")
        description = await self.bot.wait_for("message", check=check, timeout=500)

        await ctx.send("Apa warna dari embed kamu? (format hex tanpa '#')")
        color = await self.bot.wait_for("message", check=check, timeout=500)

        embed = discord.Embed(title=title.content, description=description.content, color=int(color.content, 16))
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(embed(bot))
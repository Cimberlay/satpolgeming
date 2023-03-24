import discord
from discord.ext import commands

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("kick.py aman.")

    @commands.command()
    @commands.has_role("🛡️ · Staff")
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

        conf_embed = discord.Embed(title="Berhasil!", color=discord.Color.green())
        conf_embed.add_field(name="Kick", value=f"{member.mention} Telah Di Kick Oleh {ctx.author.mention} Karena **{reason}**", inline=False)
        await ctx.send(embed=conf_embed)

async def setup(bot):
    await bot.add_cog(kick(bot))
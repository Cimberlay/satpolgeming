import discord
from discord.ext import commands

class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("role.py aman.")
      
    @commands.command()
    @commands.has_role("🛡️ · Staff")
    async def giverole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        embed = discord.Embed(title="Role Added", color=discord.Color.green())
        embed.add_field(name="User", value=member.mention)
        embed.add_field(name="Role", value=role.name)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(role(bot))
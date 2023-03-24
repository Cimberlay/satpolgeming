import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py aman.")

    @commands.command()
    @commands.has_role("🛡️ · Staff")
    async def help(self, ctx):
        embed = discord.Embed
        

        bjirr = discord.Embed(title='**Satpol Commands**', description="", color=0x66ffff)
        bjirr.add_field(name="**Clear**", value=f"Command Clear Di Gunakan Untuk NgeClear Chat\nCommand : `=clear <Berapa Banyak>`", inline=False)
        bjirr.add_field(name="**Mute**", value=f"Command Mute Di Gunakan Untuk NgeMute Orang\nCommand : `=mute <orang>`", inline=False)
        bjirr.add_field(name="**UnMute**", value=f"Command UnMute Di Gunakan Untuk UnMute Orang\nCommand : `=unmute <orang>`", inline=False)
        bjirr.add_field(name="**Ping**", value=f"Command Ping Di Gunakan Untuk Ngelihat Ping\nCommand : `=ping`", inline=False)
        bjirr.add_field(name="**Kick**", value=f"Command Kick Di Gunakan Untuk NgeKink Orang\nCommand : `=kick <orang> <karena>`", inline=False)
        bjirr.add_field(name="**Ban**", value=f"Command Ban Di Gunakan Untuk NgeBan Orang\nCommand : `=ban <orang>`", inline=False)
        bjirr.set_thumbnail(url="https://cdn.discordapp.com/attachments/858206310205489194/1059162173689036800/channels4_profile_-_Copy.jpg")
        await ctx.send(embed=bjirr)


async def setup(bot):
    await bot.add_cog(help(bot))
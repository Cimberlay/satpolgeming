import discord
from discord.ext import commands
import json
 
class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("mute.py aman.")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setmuterole(self, ctx, role: discord.Role):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            mute_role = json.load(f)
            
            mute_role[str(ctx.guild.id)] = role.name
    
        with open("cogs/jsonfiles/mutes.json", "w") as f:
            json.dump(mute_role, f, indent=4)
            
        conf_embed = discord.Embed(title="Berhasil!", color=discord.Color.green())
        conf_embed.add_field(name="Mute Role Berhasil Di Set", value=f"Mute Role Telah Diubah Menjadi '{role.mention}' Untuk Server Ini. Semua Anggota Yang Dimute Akan Dilengkapi Dengan Role Ini.", inline=False)
            
        await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setmemberrole(self, ctx, role: discord.Role):
        with open("cogs/jsonfiles/members.json", "r") as f:
            member_role = json.load(f)
            
            member_role[str(ctx.guild.id)] = role.name
    
        with open("cogs/jsonfiles/members.json", "w") as f:
            json.dump(member_role, f, indent=4)
            
        conf_embed = discord.Embed(title="Berhasil!", color=discord.Color.green())
        conf_embed.add_field(name="Member Role Berhasil Di Set", value=f"Member Role Telah Diubah Menjadi '{role.mention}'", inline=False)
            
        await ctx.send(embed=conf_embed)

    @commands.command()
    @commands.has_role("🛡️ · Staff")
    async def mute(self, ctx, member: discord.Member):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            role = json.load(f)

            mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])

        with open("cogs/jsonfiles/members.json", "r") as f:
            role = json.load(f)

            member_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])       
        
        await member.add_roles(mute_role)
        await member.remove_roles(member_role)
 
        conf_embed = discord.Embed(title="Berhasil!", color=discord.Color.green())
        conf_embed.add_field(name="Mute", value=f"{member.mention} Telah Di Mute Oleh {ctx.author.mention}.", inline=False)
        await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_role("🛡️ · Staff")
    async def unmute(self, ctx, member: discord.Member):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            role = json.load(f)

            mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])

        with open("cogs/jsonfiles/members.json", "r") as f:
            role = json.load(f)

            member_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])       
        
        await member.remove_roles(mute_role)
        await member.add_roles(member_role)

        conf_embed = discord.Embed(title="Berhasil!", color=discord.Color.green())
        conf_embed.add_field(name="Unmute", value=f"{member.mention} Telah Di Unmute Oleh {ctx.author.mention}.", inline=False)
        await ctx.send(embed=conf_embed)
        
async def setup(bot):
    await bot.add_cog(Mute(bot))

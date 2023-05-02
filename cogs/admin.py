import discord
from discord.ext import commands
from discord.ext.commands import Context

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: Context, guild: discord.Object = None):

        synced = await ctx.bot.tree.sync(guild=guild if guild else None)

        await ctx.send(
            f"Synced {len(synced)} commands {'to this guild.' if guild else 'globally.'}"
        )

    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx: Context, guild: discord.Object = None):

        ctx.bot.tree.clear_commands(guild=ctx.guild)
        await ctx.bot.tree.sync(guild=ctx.guild) 

        await ctx.send("Cleared")
        
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: Context, extension: str):
        try:
            await ctx.bot.reload_extension(f"cogs.{extension}")
            embed = discord.Embed(title='Reload', description=f'{extension.capitalize()} successfully reloaded', color=0xff00c8)    
        except Exception as error:
            embed = discord.Embed(title='Reload', description=f'{error}', color=0xff00c8)  
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Admin(bot))
import discord
from discord.ext import commands
from typing import List, Optional
from os import getenv
import asyncio
from dotenv import load_dotenv

load_dotenv()

class MyBot(commands.Bot):
    def __init__(
        self,
        *args,
        initial_extensions: List[str],
        testing_guild_id: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.testing_guild_id = testing_guild_id
        self.initial_extensions = initial_extensions
    
    async def setup_hook(self):
        for extension in self.initial_extensions:
            await self.load_extension(extension)

        if self.testing_guild_id:
            guild = discord.Object(int(self.testing_guild_id))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
    
async def main():
    
    async with MyBot(
        commands.when_mentioned,
        intents=discord.Intents.all(),
        initial_extensions=['cogs.admin', 'cogs.cavernosos'],
        testing_guild_id=getenv('TESTING_GUILD', '')) as bot:
        
        await bot.start(getenv('TOKEN', ''))

asyncio.run(main())


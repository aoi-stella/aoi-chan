import discord
from discord.ext import commands
from bot.bot_initializer import BotInitializer

class BotController():
    bot_initializer: BotInitializer = None
    bot: commands.bot = None
    
    def __init__(self) -> None:
        self.bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
        self.bot_initializer = BotInitializer(bot=self.bot)
                
    async def run_bot(self) -> None:
        await self.bot_initializer.bot_run()
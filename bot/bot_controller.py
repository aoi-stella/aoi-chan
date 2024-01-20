import discord
from bot.bot_initializer import BotInitializer

class BotController():
    bot_initializer: BotInitializer = None
    bot_client: discord.Client = None
    
    def __init_instance(self) -> None:
        self.bot_client = discord.Client(intents=discord.Intents.all())
        self.bot_initializer = BotInitializer(client=self.bot_client)

    def run_bot(self) -> None:
        self.__init_instance()
        self.bot_initializer.bot_run()
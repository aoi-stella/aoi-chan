import discord
from utils.env import DotEnvLoader
from utils.key import Key

class BotInitializer():
    def __init__(self, client: discord.Client):
        self.client = client
        
    def bot_run(self) -> bool:
        TOKEN,resut = DotEnvLoader.get(Key.BOT_TOKEN)
        
        if not resut:
            #TODO : エラーログ出す
            return False
        
        self.client.run(TOKEN)
        return True
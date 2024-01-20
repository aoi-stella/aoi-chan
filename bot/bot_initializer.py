from discord.ext import commands
from utils.env import DotEnvLoader
from utils.key import Key

class BotInitializer():
    global bots
    def __init__(self, bot: commands.Bot):
        global bots
        self.bot = bot
        bots = bot
    
    async def bot_run(self):
        TOKEN,_ = DotEnvLoader.get(Key.BOT_TOKEN)
        await self.bot.load_extension("bot.bot_cmds_list.utils_cog")
        await self.bot.start(TOKEN)
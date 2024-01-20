from discord.ext import commands
from discord import app_commands
import discord

class UtilsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # コマンドデコレーター(descriptionで説明が書ける)
    @app_commands.command(name="hello")
    async def hello(self,interaction:discord.Interaction):
        await interaction.response.send_message("hello!")
        
async def setup(bot):
    await bot.add_cog(UtilsCog(bot))
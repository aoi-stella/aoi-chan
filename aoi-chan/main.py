import discord
import os
from log import log
from log import LogLevel
from dotenv import load_dotenv

load_dotenv()
client = discord.Client(intents=discord.Intents.all())

TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    log("初期化完了", LogLevel.INFO)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "ping":
        # Send a reply with a mention to the sender
        await message.channel.send(f"{message.author.mention} pong")
        
client.run(TOKEN)
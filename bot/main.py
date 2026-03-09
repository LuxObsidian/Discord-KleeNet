import discord
from discord.ext import commands
from discord import app_commands
import os
import importlib
from dotenv import load_dotenv

# Load Token
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

COMMANDS_FOLDER = "bot/commands"

@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user}")
    
    # Commands automatisch laden
    for filename in os.listdir(COMMANDS_FOLDER):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"bot.commands.{module_name}")
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, app_commands.Command):
                    bot.tree.add_command(obj)

    await bot.tree.sync()
    print("✅ Alle Commands synchronisiert")

bot.run(TOKEN)
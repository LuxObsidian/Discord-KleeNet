import discord
from discord.ext import commands
from discord import app_commands  # <--- das war der fehlende Import
from bot.config import DISCORD_TOKEN
import os
import importlib

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    commands_folder = "bot.commands"

    for filename in os.listdir("bot/commands"):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"{commands_folder}.{module_name}")

            # alle Commands laden
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, app_commands.Command):
                    bot.tree.add_command(obj)

    await bot.tree.sync()
    print(f"✅ Eingeloggt als {bot.user}")

bot.run(DISCORD_TOKEN)
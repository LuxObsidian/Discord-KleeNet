import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import importlib
import inspect
from bot.config import TOKEN, TEST_GUILD_ID

# -------------------------------
# Token prüfen
# -------------------------------
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN nicht gefunden! .env prüfen.")

print("Starte Bot …")
print("TOKEN geladen:", TOKEN[:5] + "...")

# -------------------------------
# Intents
# -------------------------------
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# -------------------------------
# Bot Klasse mit setup_hook
# -------------------------------
class KleeNetBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
        self.test_guild = discord.Object(id=TEST_GUILD_ID)

    async def setup_hook(self):
        # Alle Command-Dateien importieren und setup(bot) aufrufen
        commands_folder = os.path.join(os.path.dirname(__file__), "commands")
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module_path = f"bot.commands.{module_name}"
                try:
                    module = importlib.import_module(module_path)
                    setup_func = getattr(module, "setup", None)
                    if setup_func and inspect.iscoroutinefunction(setup_func):
                        await setup_func(self)
                        print(f"✅ {module_name}.py geladen")
                except Exception as e:
                    print(f"❌ Fehler beim Laden von {module_name}: {e}")

        # Globale Commands in die Test-Guild kopieren für sofortige Verfügbarkeit
        self.tree.copy_global_to(guild=self.test_guild)

        # Debug: Registrierte Commands anzeigen
        commands_list = [cmd.name for cmd in self.tree.get_commands(guild=self.test_guild)]
        print(f"📋 Registrierte Commands: {commands_list}")

        # Commands für Test-Guild synchronisieren
        await self.tree.sync(guild=self.test_guild)
        print(f"✅ Alle Commands für Test-Guild {TEST_GUILD_ID} synchronisiert")

    async def on_ready(self):
        print(f"✅ Eingeloggt als {self.user}")

# -------------------------------
# Bot starten
# -------------------------------
bot = KleeNetBot()
bot.run(TOKEN)

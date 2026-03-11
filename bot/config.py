import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# Bot-Token
# -------------------------------
TOKEN = os.getenv("DISCORD_TOKEN")

# -------------------------------
# Bot-Einstellungen
# -------------------------------
PREFIX = "!"
TEST_GUILD_ID = 134690944296550400

# -------------------------------
# Benutzer-IDs
# -------------------------------
OWNER_ID = 307259127778902017
BOT_ID = 1479995039097819278
KLEEMANN_ID = 257239098379468801

# -------------------------------
# Logging
# -------------------------------
LOG_FILE = "bot_command.log"

# -------------------------------
# Datenbank (für später)
# -------------------------------
DB_FILE = "word_counts.json"
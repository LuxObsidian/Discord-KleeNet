import os
import logging
from logging.handlers import RotatingFileHandler
import discord

# -------------------------------
# Logging Setup mit Rotation
# -------------------------------

LOG_FILE = "bot_command.log"
MAX_BYTES = 5 * 1024 * 1024  # 5 MB pro Logfile
BACKUP_COUNT = 4             # Anzahl alter Logs, die behalten werden

logger = logging.getLogger("KleeNetLogger")
logger.setLevel(logging.INFO)

# RotatingFileHandler erstellen
handler = RotatingFileHandler(LOG_FILE, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT, encoding="utf-8")
formatter = logging.Formatter("[%(asctime)s] %(levelname)s | %(name)s | %(message)s", "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Funktion für Command-Logging
def log_command(user: discord.User, command_name: str, success: bool, message: str = ""):
    status = "SUCCESS" if success else "ERROR"
    log_msg = f"{user} | {command_name} | {message}"
    if success:
        logger.info(log_msg)
    else:
        logger.error(log_msg)
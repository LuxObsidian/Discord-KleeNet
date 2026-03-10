import discord
from discord.ext import commands
from discord import app_commands
from bot.logger import log_command
from bot.config import DB_FILE
import json
import os

# -------------------------------
# Konfiguration
# -------------------------------
TRACKED_WORDS = ["hdf", "gestank", "geruch", "lurk", "lurken", "dicktitter", "drache", "abseilen"]

# -------------------------------
# Cog Definition
# -------------------------------
class WordTracker(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.word_counts = self._load_word_counts()

    # -------------------------------
    # Laden aus JSON
    # -------------------------------
    def _load_word_counts(self) -> dict:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, "r") as f:
                try:
                    data = json.load(f)
                    return {
                        (int(k.split("_")[0]), k.split("_")[1]): v
                        for k, v in data.items()
                    }
                except json.JSONDecodeError:
                    return {}
        return {}

    # -------------------------------
    # Speichern in JSON
    # -------------------------------
    def _save_word_counts(self):
        data = {
            f"{user_id}_{word}": info
            for (user_id, word), info in self.word_counts.items()
        }
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)

    # -------------------------------
    # Listener: Nachrichten tracken
    # -------------------------------
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        content = message.content.lower()
        found_word = False

        for word in TRACKED_WORDS:
            if word in content:
                key = (message.author.id, word)
                if key not in self.word_counts:
                    self.word_counts[key] = {"count": 0, "last_name": message.author.display_name}
                self.word_counts[key]["count"] += 1
                self.word_counts[key]["last_name"] = message.author.display_name
                log_command(message.author, f"WORD_TRACK ({word})", success=True)
                found_word = True

        # Nur einmal speichern nach der ganzen Schleife
        if found_word:
            self._save_word_counts()

        await self.bot.process_commands(message)

    # -------------------------------
    # /poweruser Command
    # -------------------------------
    @app_commands.command(
        name="poweruser",
        description="Zeigt die meistgenutzten getrackten Wörter eines Users"
    )
    @app_commands.describe(user="User auswählen")
    async def poweruser(self, interaction: discord.Interaction, user: discord.Member):
        user_words = {
            word: info["count"]
            for (uid, word), info in self.word_counts.items()
            if uid == user.id
        }

        if not user_words:
            await interaction.response.send_message(
                f"{user.display_name} hat noch keine getrackten Wörter benutzt.",
                ephemeral=True
            )
            log_command(interaction.user, "poweruser", False, f"Keine Daten für {user.display_name}")
            return

        sorted_words = sorted(user_words.items(), key=lambda x: x[1], reverse=True)
        msg = f"**Top-Wörter von {user.display_name}:**\n"
        for word, count in sorted_words:
            msg += f"- {word}: {count}x\n"

        await interaction.response.send_message(msg)
        log_command(interaction.user, "poweruser", True, f"Stats für {user.display_name} angezeigt")

# -------------------------------
# Cog Setup
# -------------------------------
async def setup(bot: commands.Bot):
    await bot.add_cog(WordTracker(bot))
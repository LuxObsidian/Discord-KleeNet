import discord
from discord.ext import commands
import time
from bot.logger import log_command
from bot.config import OWNER_ID, BOT_ID

# -------------------------------
# Cog für persönliche Begrüßung mit Cooldown
# -------------------------------
class Greeting(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.greetings = ["hallo", "hi", "hey", "servus", "salut"]
        self.cooldown = 30  # Sekunden, bevor erneut gegrüßt wird
        self.last_greet = 0

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Bot-Nachrichten ignorieren
        if message.author.bot:
            return

        # Prüfen: Nachricht von dir und Bot erwähnt
        if message.author.id == OWNER_ID and any(user.id == BOT_ID for user in message.mentions):
            content_lower = message.content.lower()
            if any(greet in content_lower for greet in self.greetings):
                now = time.time()
                if now - self.last_greet >= self.cooldown:
                    await message.channel.send(
                        "Ich grüsse dich mein gutaussehender Luxemburgischer Held und genialer Pilot!"
                    )
                    log_command(message.author, "greeting", True, "Begrüßung gesendet")
                    self.last_greet = now

        # Andere Commands weiterhin ausführen
        await self.bot.process_commands(message)

# -------------------------------
# Setup
# -------------------------------
async def setup(bot: commands.Bot):
    await bot.add_cog(Greeting(bot))
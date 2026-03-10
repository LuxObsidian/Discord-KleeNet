import discord
from discord.ext import commands
from discord import app_commands
from bot.logger import log_command
from bot.config import KLEEMANN_ID

# -------------------------------
# Cooldown Konfiguration (in Sekunden)
# -------------------------------
COMMAND_COOLDOWNS = {
    "klee": 30,
    "zahlen": 60,
    "geruch": 15
}

# -------------------------------
# Cog für Spaß-Commands
# -------------------------------
class FunCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_used = {}  # key: (user_id, command_name), value: timestamp

    # -------------------------------
    # Hilfsfunktionen
    # -------------------------------
    def check_cooldown(self, user_id: int, command_name: str) -> float:
        """Gibt 0 zurück wenn OK, sonst die verbleibenden Sekunden."""
        import time
        now = time.time()
        last = self.last_used.get((user_id, command_name), 0)
        cooldown = COMMAND_COOLDOWNS.get(command_name, 30)
        remaining = cooldown - (now - last)
        if remaining > 0:
            return remaining
        self.last_used[(user_id, command_name)] = now
        return 0

    def get_target_member(self, guild: discord.Guild) -> discord.Member | None:
        return guild.get_member(KLEEMANN_ID)

    # -------------------------------
    # Commands
    # -------------------------------
    @app_commands.command(name="klee", description="Spaßbefehl für Kleemann")
    async def klee(self, interaction: discord.Interaction):
        remaining = self.check_cooldown(interaction.user.id, "klee")
        if remaining > 0:
            await interaction.response.send_message(
                f"⏳ Langsam! Noch {remaining:.0f} Sekunden Cooldown.", ephemeral=True
            )
            log_command(interaction.user, "klee", False, "Cooldown aktiv")
            return

        member = self.get_target_member(interaction.guild)
        if not member:
            await interaction.response.send_message("Kleemann ist nicht auf dem Server.", ephemeral=True)
            log_command(interaction.user, "klee", False, "Kleemann nicht gefunden")
            return

        await interaction.response.send_message(
            f"Hallo {member.mention}, wie sieht es aus in deiner kleinen Französischen Provinz?"
        )
        log_command(interaction.user, "klee", True)

    @app_commands.command(name="zahlen", description="Spaßbefehl nur für Kleemann")
    async def zahlen(self, interaction: discord.Interaction):
        remaining = self.check_cooldown(interaction.user.id, "zahlen")
        if remaining > 0:
            await interaction.response.send_message(
                f"⏳ Langsam! Noch {remaining:.0f} Sekunden Cooldown.", ephemeral=True
            )
            log_command(interaction.user, "zahlen", False, "Cooldown aktiv")
            return

        member = self.get_target_member(interaction.guild)
        if not member:
            await interaction.response.send_message("Kleemann ist nicht auf dem Server.", ephemeral=True)
            log_command(interaction.user, "zahlen", False, "Kleemann nicht gefunden")
            return

        await interaction.response.send_message(
            f"{member.mention}, Hol die Kreditkarten raus! Zeit zu donaten!?"
        )
        log_command(interaction.user, "zahlen", True)

    @app_commands.command(name="geruch", description="Noch ein Spaßbefehl für Kleemann")
    async def geruch(self, interaction: discord.Interaction):
        remaining = self.check_cooldown(interaction.user.id, "geruch")
        if remaining > 0:
            await interaction.response.send_message(
                f"⏳ Langsam! Noch {remaining:.0f} Sekunden Cooldown.", ephemeral=True
            )
            log_command(interaction.user, "geruch", False, "Cooldown aktiv")
            return

        member = self.get_target_member(interaction.guild)
        if not member:
            await interaction.response.send_message("Kleemann ist nicht auf dem Server.", ephemeral=True)
            log_command(interaction.user, "geruch", False, "Kleemann nicht gefunden")
            return

        await interaction.response.send_message(
            f"{member.mention}, Ich atme lieber nicht mehr, wenn du in der Nähe bist!"
        )
        log_command(interaction.user, "geruch", True)

# -------------------------------
# Setup
# -------------------------------
async def setup(bot: commands.Bot):
    await bot.add_cog(FunCommands(bot))

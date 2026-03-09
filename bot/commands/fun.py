import discord
from discord import app_commands
from bot.logger import log_command
import time

# -------------------------------
# Konfiguration
# -------------------------------
TARGET_USER_ID = 257239098379468801  # Discord-ID von Kleemann

# -------------------------------
# Cooldown Setup
# -------------------------------
last_used = {}  # key: (user_id, command_name), value: timestamp
COMMAND_COOLDOWNS = {
    "klee": 30,
    "zahlen": 60,
    "geruch": 15
}

def check_cooldown(user_id: int, command_name: str) -> bool:
    now = time.time()
    last = last_used.get((user_id, command_name), 0)
    cooldown = COMMAND_COOLDOWNS.get(command_name, 30)
    if now - last < cooldown:
        return False
    last_used[(user_id, command_name)] = now
    return True

# -------------------------------
# Hilfsfunktion: Kleemann holen
# -------------------------------
def get_target_member(guild: discord.Guild):
    return guild.get_member(TARGET_USER_ID)

# ----------------------------------------
# /klee Command
# ----------------------------------------
@app_commands.command(name="klee", description="Spaßbefehl für Kleemann")
async def klee(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id, "klee"):
        await interaction.response.send_message(
            "Langsam! Du bist noch im Cooldown.", ephemeral=True
        )
        log_command(interaction.user, "klee", False, "Cooldown aktiv")
        return

    member = get_target_member(interaction.guild)
    if not member:
        await interaction.response.send_message(
            "Kleemann ist nicht auf dem Server.", ephemeral=True
        )
        log_command(interaction.user, "klee", False, "Kleemann nicht gefunden")
        return

    await interaction.response.send_message(
        f"Hallo {member.mention}, wie sieht es aus in deiner kleinen Französischen Provinz?"
    )
    log_command(interaction.user, "klee", True)

# ----------------------------------------
# /zahlen Command
# ----------------------------------------
@app_commands.command(name="zahlen", description="Spaßbefehl nur für Kleemann")
async def zahlen(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id, "zahlen"):
        await interaction.response.send_message(
            "Langsam! Du bist noch im Cooldown.", ephemeral=True
        )
        log_command(interaction.user, "zahlen", False, "Cooldown aktiv")
        return

    member = get_target_member(interaction.guild)
    if not member:
        await interaction.response.send_message(
            "Kleemann ist nicht auf dem Server.", ephemeral=True
        )
        log_command(interaction.user, "zahlen", False, "Kleemann nicht gefunden")
        return

    await interaction.response.send_message(
        f"{member.mention}, Hol die Kreditkarten raus! Zeit zu donaten!?"
    )
    log_command(interaction.user, "zahlen", True)

# ----------------------------------------
# /geruch Command
# ----------------------------------------
@app_commands.command(name="geruch", description="Noch ein Spaßbefehl für Kleemann")
async def geruch(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id, "geruch"):
        await interaction.response.send_message(
            "Langsam! Du bist noch im Cooldown.", ephemeral=True
        )
        log_command(interaction.user, "geruch", False, "Cooldown aktiv")
        return

    member = get_target_member(interaction.guild)
    if not member:
        await interaction.response.send_message(
            "Kleemann ist nicht auf dem Server.", ephemeral=True
        )
        log_command(interaction.user, "geruch", False, "Kleemann nicht gefunden")
        return

    await interaction.response.send_message(
        f"{member.mention}, Ich atme lieber nicht mehr, wenn du in der Nähe bist!"
    )
    log_command(interaction.user, "geruch", True)
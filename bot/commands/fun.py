import discord
from discord import app_commands
import time

TARGET_USER = "Kleemann"  # nur auf diesen User reagiert der Bot

# -------------------------------
# Cooldown Setup
# -------------------------------
# speichert die letzte Benutzung pro User und pro Command
last_used = {}  # key: (user_id, command_name), value: timestamp

# Cooldowns pro Command (in Sekunden)
COMMAND_COOLDOWNS = {
    "klee": 30,
    "zahlen": 60,
    "geruch": 15
}

def check_cooldown(user_id: int, command_name: str) -> bool:
    """Prüft, ob der User den Command benutzen darf"""
    now = time.time()
    last = last_used.get((user_id, command_name), 0)
    cooldown = COMMAND_COOLDOWNS.get(command_name, 30)
    if now - last < cooldown:
        return False
    last_used[(user_id, command_name)] = now
    return True

# ----------------------------------------
# /klee Command
# ----------------------------------------
@app_commands.command(
    name="klee",
    description="Spaßbefehl für Kleemann"
)
async def klee(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id, "klee"):
        await interaction.response.send_message(
            "Langsam! Du bist noch im Cooldown.", ephemeral=True
        )
        return

    member = discord.utils.get(interaction.guild.members, name=TARGET_USER)
    if not member:
        await interaction.response.send_message(
            f"{TARGET_USER} ist nicht im Channel.", ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"Hallo {member.mention} wie sieht es aus in deiner kleinen Französischen Provinz?"
    )

# ----------------------------------------
# /zahlen Command
# ----------------------------------------
@app_commands.command(
    name="zahlen",
    description="Spaßbefehl nur für Kleemann"
)
async def zahlen(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id, "zahlen"):
        await interaction.response.send_message(
            "Langsam! Du bist noch im Cooldown.", ephemeral=True
        )
        return

    member = discord.utils.get(interaction.guild.members, name=TARGET_USER)
    if not member:
        await interaction.response.send_message(
            f"{TARGET_USER} ist nicht im Channel.", ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"{member.mention}, Hol die Kreditkarten raus! Zeit zu donaten!?"
    )

# ----------------------------------------
# /geruch Command
# ----------------------------------------
@app_commands.command(
    name="geruch",
    description="Noch ein Spaßbefehl für Kleemann"
)
async def geruch(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id, "geruch"):
        await interaction.response.send_message(
            "Langsam! Du bist noch im Cooldown.", ephemeral=True
        )
        return

    member = discord.utils.get(interaction.guild.members, name=TARGET_USER)
    if not member:
        await interaction.response.send_message(
            f"{TARGET_USER} ist nicht im Channel.", ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"{member.mention}, Ich atme lieber nicht mehr, wenn du in der Nähe bist.!"
    )
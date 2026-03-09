import discord
from discord import app_commands
import time

TARGET_USER = "Kleemann"  # nur auf diesen User reagiert der Bot

# -------------------------------
# Cooldown Setup
# -------------------------------
last_used = {}  # speichert die letzte Benutzung pro User
COOLDOWN_SECONDS = 30  # Sekunden zwischen Benutzungen (anpassbar)

def check_cooldown(user_id: int) -> bool:
    """Prüft, ob der User den Command benutzen darf"""
    now = time.time()
    last = last_used.get(user_id, 0)
    if now - last < COOLDOWN_SECONDS:
        return False
    last_used[user_id] = now
    return True

# ----------------------------------------
# /klee Command
# ----------------------------------------
@app_commands.command(
    name="klee",
    description="Spaßbefehl für Kleemann"
)
async def klee(interaction: discord.Interaction):
    if not check_cooldown(interaction.user.id):
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
    if not check_cooldown(interaction.user.id):
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
    if not check_cooldown(interaction.user.id):
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
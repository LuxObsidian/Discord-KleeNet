import discord
from discord import app_commands

TARGET_USER = "Kleemann"  # nur auf diesen User reagiert der Bot

# ----------------------------------------
# /klee Command
# ----------------------------------------
@app_commands.command(
    name="klee",
    description="Spaßbefehl für Kleemann"
)
async def klee(interaction: discord.Interaction):
    # Bot reagiert nur, wenn Kleemann im Channel ist
    member = discord.utils.get(interaction.guild.members, name=TARGET_USER)
    if not member:
        await interaction.response.send_message(
            f"{TARGET_USER} ist nicht im Channel.",
            ephemeral=True
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
    # Bot reagiert nur, wenn Kleemann im Channel ist
    member = discord.utils.get(interaction.guild.members, name=TARGET_USER)
    if not member:
        await interaction.response.send_message(
            f"{TARGET_USER} ist nicht im Channel.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"{member.mention}, Hol die Kreditkarten raus! Zeit zu donaten!? 😎"
    )
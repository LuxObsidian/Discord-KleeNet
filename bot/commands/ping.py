import discord
from discord.ext import commands
from discord import app_commands
from bot.logger import log_command

class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Zeigt die aktuelle Bot-Latenz an"
    )
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  # in ms
        await interaction.response.send_message(f"🏓 Pong! Latenz: {latency}ms")
        log_command(interaction.user, "ping", True, f"Latenz: {latency}ms")

async def setup(bot: commands.Bot):
    await bot.add_cog(PingCommand(bot))
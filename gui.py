import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import os

# -------------------------------
# Farben & Fonts modernisiert
# -------------------------------
BG_COLOR = "#2b2b2b"
BTN_COLOR = "#3a3f44"
BTN_HOVER = "#50575e"
TXT_BG = "#1e1e1e"
TXT_FG = "#ffffff"
FONT_TEXT = ("Consolas", 13)
FONT_BTN = ("Arial", 12, "bold")

# -------------------------------
# Dateien / Ordner
# -------------------------------
LOG_FILE = "bot_command.log"
COMMANDS_FOLDER = "bot/commands"
WORD_COUNT_FILE = "word_counts.json"
os.makedirs(COMMANDS_FOLDER, exist_ok=True)

# -------------------------------
# Command Templates
# -------------------------------
TEMPLATES = {
    "Fun": """import discord
from discord.ext import commands
from discord import app_commands

class {ClassName}Command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="{cmd_name}",
        description="{cmd_desc}"
    )
    async def {cmd_name}(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fun Command {cmd_name} ausgeführt!")

async def setup(bot: commands.Bot):
    await bot.add_cog({ClassName}Command(bot))
""",
    "Moderation": """import discord
from discord.ext import commands
from discord import app_commands

class {ClassName}Command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="{cmd_name}",
        description="{cmd_desc}"
    )
    async def {cmd_name}(self, interaction: discord.Interaction):
        await interaction.response.send_message("Moderation Command {cmd_name} ausgeführt!")

async def setup(bot: commands.Bot):
    await bot.add_cog({ClassName}Command(bot))
"""
}

CATEGORIES = list(TEMPLATES.keys())

# -------------------------------
# Hilfsfunktionen
# -------------------------------
def create_scroll_window(title, content, width=80, height=35):
    """Hilfsfunktion für dunkles Scrollfenster"""
    window = tk.Toplevel(root)
    window.title(title)

    frame = tk.Frame(window, bg=BG_COLOR)
    frame.pack(fill="both", expand=True, padx=5, pady=5)

    text_area = tk.Text(frame, width=width, height=height, bg=TXT_BG, fg=TXT_FG, font=FONT_TEXT, wrap="word")
    text_area.insert(tk.END, content)
    text_area.configure(state='disabled')
    text_area.pack(side="left", fill="both", expand=True)

    scroll = ttk.Scrollbar(frame, orient="vertical", command=text_area.yview)
    scroll.pack(side="right", fill="y")
    text_area.configure(yscrollcommand=scroll.set)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Vertical.TScrollbar", background=BTN_COLOR, troughcolor=BG_COLOR, bordercolor=BG_COLOR, arrowcolor=TXT_FG)

    return window

def add_hover_effect(button):
    button.bind("<Enter>", lambda e: button.configure(bg=BTN_HOVER))
    button.bind("<Leave>", lambda e: button.configure(bg=BTN_COLOR))

# -------------------------------
# Logs anzeigen
# -------------------------------
def show_logs():
    if not os.path.exists(LOG_FILE):
        messagebox.showinfo("Info", "Keine Log-Datei gefunden!")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = f.read()
    create_scroll_window("Bot Logs", logs, width=120, height=35)

# -------------------------------
# Word Counts anzeigen
# -------------------------------
def show_word_counts():
    if not os.path.exists(WORD_COUNT_FILE):
        messagebox.showinfo("Info", "Keine word_counts.json gefunden!")
        return
    with open(WORD_COUNT_FILE, "r", encoding="utf-8") as f:
        try:
            data = f.read()
        except:
            data = "Fehler beim Lesen der Datei!"
    create_scroll_window("Word Counts", data, width=120, height=35)

# -------------------------------
# Neuer Command erstellen
# -------------------------------
def create_new_command():
    cmd_name = simpledialog.askstring("Neuer Command", "Name des Commands:")
    if not cmd_name:
        return

    cmd_desc = simpledialog.askstring("Beschreibung", "Beschreibung des Commands:")
    if not cmd_desc:
        cmd_desc = "Keine Beschreibung angegeben"

    category = category_var.get()

    filename = f"{cmd_name}.py"
    filepath = os.path.join(COMMANDS_FOLDER, filename)
    if os.path.exists(filepath):
        messagebox.showerror("Fehler", "Datei existiert bereits!")
        return

    template = TEMPLATES[category].format(ClassName=cmd_name.capitalize(), cmd_name=cmd_name, cmd_desc=cmd_desc)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template)

    messagebox.showinfo("Erfolg", f"Command {cmd_name} erstellt!")

# -------------------------------
# Hauptfenster
# -------------------------------
root = tk.Tk()
root.title("KleeNet Dashboard v0.01")
root.geometry("950x700")
root.configure(bg=BG_COLOR)

# Kategorie Dropdown
category_var = tk.StringVar(root)
category_var.set(CATEGORIES[0])
tk.Label(root, text="Kategorie auswählen:", bg=BG_COLOR, fg=TXT_FG, font=FONT_BTN).pack(pady=(10,0))
tk.OptionMenu(root, category_var, *CATEGORIES).pack(pady=(0,10))

# Buttons
buttons = []
btn_logs = tk.Button(root, text="Logs anzeigen", command=show_logs, width=40, bg=BTN_COLOR, fg=TXT_FG, font=FONT_BTN)
btn_logs.pack(pady=5)
buttons.append(btn_logs)

btn_words = tk.Button(root, text="Word Counts anzeigen", command=show_word_counts, width=40, bg=BTN_COLOR, fg=TXT_FG, font=FONT_BTN)
btn_words.pack(pady=5)
buttons.append(btn_words)

btn_new_cmd = tk.Button(root, text="Neuen Command erstellen", command=create_new_command, width=40, bg=BTN_COLOR, fg=TXT_FG, font=FONT_BTN)
btn_new_cmd.pack(pady=5)
buttons.append(btn_new_cmd)

for btn in buttons:
    add_hover_effect(btn)

# -------------------------------
# Scrollfenster für Commands mit automatischer Aktualisierung
# -------------------------------
latest_files = []

cmd_list_frame = tk.Frame(root, bg=BG_COLOR)
cmd_list_frame.pack(fill="both", expand=True, padx=5, pady=5)

cmd_text_area = tk.Text(cmd_list_frame, width=80, height=22, bg=TXT_BG, fg=TXT_FG, font=FONT_TEXT, wrap="word")
cmd_text_area.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(cmd_list_frame, orient="vertical", command=cmd_text_area.yview)
scroll.pack(side="right", fill="y")
cmd_text_area.configure(yscrollcommand=scroll.set, state="disabled")

def update_command_list():
    global latest_files
    current_files = [f for f in os.listdir(COMMANDS_FOLDER) if f.endswith(".py") and f != "__init__.py"]
    if current_files != latest_files:
        latest_files = current_files
        cmd_text_area.configure(state="normal")
        cmd_text_area.delete("1.0", tk.END)
        cmd_text_area.insert(tk.END, "\n".join(current_files))
        cmd_text_area.configure(state="disabled")
    root.after(2000, update_command_list)

update_command_list()

# -------------------------------
# Copyright / Footer
# -------------------------------
copyright_label = tk.Label(
    root,
    text="© 2026 Becker Alain – KleeNet Dashboard | www.luxobsidian.eu",
    bg=BG_COLOR,
    fg=TXT_FG,
    font=("Arial", 10)
)
copyright_label.pack(side="bottom", pady=5)

root.mainloop()
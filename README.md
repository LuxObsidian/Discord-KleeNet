# KleeNet Discord Bot

A modular Discord bot built with Python and discord.py, featuring slash commands, word tracking, and fun commands.

---

## Features

### Commands
| Command | Description |
|--------|-------------|
| `/ping` | Shows the current bot latency in ms |
| `/klee` | Fun command targeting a specific user |
| `/zahlen` | Fun command targeting a specific user |
| `/geruch` | Fun command targeting a specific user |
| `/poweruser` | Shows the most used tracked words of a user |

### Word Tracking
The bot automatically tracks specific words in messages and stores them in a `word_counts.json` file. Use `/poweruser` to view statistics for any user.

### Logging
All commands are logged to `bot_command.log` with rotating file handler (max 5MB per file, 4 backups).

---

## Project Structure

```
DiscordBot/
├── bot/
│   ├── commands/
│   │   ├── fun.py            # Fun slash commands
│   │   ├── greetings.py      # Auto-greeting on mention
│   │   ├── ping.py           # Ping/latency command
│   │   └── word_tracker.py   # Word tracking + /poweruser
│   ├── config.py             # Central configuration
│   ├── database.py           # Database (reserved for future use)
│   ├── logger.py             # Logging setup
│   └── main.py               # Bot entry point
├── venv/                     # Virtual environment (not tracked)
├── .env                      # Secret tokens (not tracked)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### Prerequisites
- Python 3.10+
- A Discord Bot Token ([Discord Developer Portal](https://discord.com/developers/applications))

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/LuxObsidian/Discord-KleeNet.git
   cd Discord-KleeNet
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file**
   ```
   DISCORD_TOKEN=your_token_here
   ```

5. **Configure `bot/config.py`**
   ```python
   TEST_GUILD_ID = your_server_id
   OWNER_ID = your_discord_user_id
   BOT_ID = your_bot_id
   KLEEMANN_ID = target_user_id
   ```

6. **Run the bot**
   ```bash
   python -m bot.main
   ```

---

## Configuration

All configuration values are stored in `bot/config.py`:

| Variable | Description |
|----------|-------------|
| `TOKEN` | Discord bot token (loaded from `.env`) |
| `PREFIX` | Command prefix (default: `!`) |
| `TEST_GUILD_ID` | Server ID for instant slash command sync |
| `OWNER_ID` | Discord user ID of the bot owner |
| `BOT_ID` | Discord bot ID |
| `KLEEMANN_ID` | Target user ID for fun commands |
| `LOG_FILE` | Log file name |
| `DB_FILE` | Word counts JSON file |

---

## Security

- The bot token is stored in a `.env` file and never committed to the repository
- `.gitignore` excludes `.env`, `venv/`, logs, and generated files
- Password-based SSH login is disabled on the production server (key-based auth only)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

This is a private project. If you have suggestions or find bugs, feel free to open an issue or contact the owner directly.

---

*Built with ❤️ by LuxObsidian*

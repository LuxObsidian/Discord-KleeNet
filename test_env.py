from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

if token:
    print("✅ .env funktioniert!")
else:
    print("❌ Token wurde nicht gefunden.")
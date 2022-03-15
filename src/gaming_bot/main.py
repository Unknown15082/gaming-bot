from os import environ as env

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = env["TOKEN"]
ALL_INTENTS = disnake.Intents.all()

bot = commands.Bot(intents=ALL_INTENTS)

EXTENSIONS = [
    "bot_events",
]

for extension in EXTENSIONS:
    bot.load_extension(extension)

if __name__ == "__main__":
    bot.run(TOKEN)

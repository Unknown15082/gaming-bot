from os import environ as env

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = env["TOKEN"]
ALL_INTENTS: disnake.Intents = disnake.Intents.all()

bot: commands.Bot = commands.Bot(intents=ALL_INTENTS)

EXTENSIONS: list[str] = [
    "bot_events",
]

for extension in EXTENSIONS:
    bot.load_extension(extension)

if __name__ == "__main__":
    bot.run(TOKEN)

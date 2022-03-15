from os import environ as env

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN: str = env["TOKEN"]
STR_TEST_GUILDS: str = env["TEST_GUILDS"]
TEST_GUILDS: list[int] = [int(guild_id) for guild_id in STR_TEST_GUILDS.split(",")]
ALL_INTENTS: disnake.Intents = disnake.Intents.all()

bot: commands.Bot = commands.Bot(intents=ALL_INTENTS, test_guilds=TEST_GUILDS)

EXTENSIONS: list[str] = [
    "bot_events",
    "general_bot_commands",
    "dice_roll_game.game_commands",
]

for extension in EXTENSIONS:
    bot.load_extension(extension)

if __name__ == "__main__":
    bot.run(TOKEN)

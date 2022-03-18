"""
A module for fetching AppInfo of a bot.
"""

import disnake
from disnake.ext import commands


async def get_app_info(bot: commands.Bot) -> disnake.AppInfo:
    try:
        info = await bot.application_info()
    except disnake.HTTPException as e:
        raise e

    return info

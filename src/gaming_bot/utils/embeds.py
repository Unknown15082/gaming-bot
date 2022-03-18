"""
A module for providing packages with the default embed.
"""

from datetime import datetime

import disnake
from disnake.ext import commands
from utils import get_app_info


async def base_embed(bot: commands.Bot) -> disnake.Embed:
    app_info = await get_app_info.get_app_info(bot)

    default_embed: disnake.Embed = disnake.Embed(timestamp=datetime.utcnow())
    default_embed.set_author(name="Gaming Bot", icon_url=app_info.cover_image.url)

    return default_embed

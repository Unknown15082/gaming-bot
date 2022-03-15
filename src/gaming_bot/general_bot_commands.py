from os import environ as env

import disnake
from disnake.ext import commands


class GeneralBotCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.slash_command()
    async def help(self, inter: disnake.ApplicationCommandInteraction) -> None:
        await inter.response.send_message("There is currently no help message.")

    @commands.slash_command()
    async def get_bot_invite_link(
        self, inter: disnake.ApplicationCommandInteraction
    ) -> None:
        permission: disnake.Permissions = disnake.Permissions()
        # Set the required permissions for the bot (default to administrator)
        disnake.Permissions.update(permission, administrator=True)
        scopes: list[str] = ["bot", "applications.commands"]

        oauth_url: str = disnake.utils.oauth_url(
            env["CLIENT_ID"], permissions=permission, scopes=scopes
        )

        await inter.response.send_message(
            f"You can invite me into your servers using this link:\n{oauth_url}"
        )


def setup(bot: commands.Bot) -> None:
    bot.add_cog(GeneralBotCommands(bot))

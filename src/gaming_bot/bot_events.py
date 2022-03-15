from disnake.ext import commands


class BotEvents(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Bot is now logged in.")


def setup(bot: commands.Bot) -> None:
    bot.add_cog(BotEvents(bot))

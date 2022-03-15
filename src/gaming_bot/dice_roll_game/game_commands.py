import disnake
from disnake.ext import commands


class DiceRollCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.slash_command(name="dice")
    async def group(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @group.sub_command()
    async def setup(self, inter: disnake.ApplicationCommandInteraction):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(DiceRollCog(bot))

import disnake
from dice_roll_game import current_game, game_implementation
from disnake.ext import commands


class DiceRollCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.slash_command(name="dice")
    async def game(self, inter: disnake.ApplicationCommandInteraction) -> None:
        # Set the game's ID as the player's ID
        user_id = inter.author.id

        # TODO: Ask for the target score, currently default to 100

        new_game = game_implementation.DiceRollGame(100)

        try:
            current_game.add_game(user_id, new_game)
        except Exception:
            await inter.response.send_message("You are currently playing a game.")
            return

        # TODO: Represent a game using an embed

        await inter.response.send_message(f"A game was created with ID = {user_id}")


def setup(bot: commands.Bot):
    bot.add_cog(DiceRollCog(bot))

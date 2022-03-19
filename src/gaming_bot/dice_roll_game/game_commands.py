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

        if current_game.check_if_exists(user_id):
            await inter.response.send_message("You are already playing this game!")
            return

        # TODO: Ask for level of AI

        new_game = game_implementation.DiceRollGame(100)
        current_game.update_game(user_id, new_game)

        # TODO: Represent a game using an embed

        await inter.response.send_message(f"A game was created with ID = {user_id}")


def setup(bot: commands.Bot):
    bot.add_cog(DiceRollCog(bot))

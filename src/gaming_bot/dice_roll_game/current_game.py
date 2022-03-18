from dice_roll_game import game_implementation as game

from gaming_bot.utils import exceptions

current_game_list: dict[int, game.DiceRollGame] = {}


def check_if_exists(id: int) -> bool:
    """
    Check if a game with the given ID currently exists.
    """
    if id in current_game_list.keys():
        return True
    return False


def update_game(id: int, new_game: game.DiceRollGame) -> None:
    """
    Update the game with the corresponding ID in the list of currently running games.
    If it doesn't exists, create a new game instead.
    """
    current_game_list[id] = new_game


def fetch_game(id: int) -> game.DiceRollGame:
    """
    Return a current game with the corresponding ID.
    Raises GameNotFoundError if no game with the given ID is found.
    """
    if not check_if_exists(id):
        raise exceptions.GameNotFoundError("Dice Roll", id)
    else:
        return current_game_list[id]


def remove_game(id: int) -> None:
    """
    Remove the game with the corresponding ID from the list of currently running game.
    Raises GameNotFoundError if no game with the given ID is found.
    """
    if not check_if_exists(id):
        raise exceptions.GameNotFoundError("Dice Roll", id)
    else:
        return current_game_list.pop(id)

from dice_roll_game import game_implementation as game

current_game_list: dict[int, game.DiceRollGame] = {}


def add_game(id: int, new_game: game.DiceRollGame) -> None:
    """
    Add a game to the list of currently running games.
    """
    if id in current_game_list.keys():
        raise Exception("Game with given ID already exists!")
    else:
        current_game_list[id] = new_game


def fetch_game(id: int) -> game.DiceRollGame:
    if id not in current_game_list.keys():
        raise Exception("Game with given ID not found!")
    else:
        return current_game_list[id]


def remove_game(id: int) -> None:
    if id not in current_game_list.keys():
        raise Exception("Game with given ID not found!")
    else:
        return current_game_list.pop(id)

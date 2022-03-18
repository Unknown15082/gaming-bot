"""
Files for every custom exceptions.
"""


class GameNotFoundError(Exception):
    """
    Exception to raise when the required game is not found.
    """

    def __init__(self, game_type: str, game_id: int) -> None:
        self.game_id = game_id
        self.game_type = game_type

    def __str__(self) -> str:
        return f"Game ({self.game_type}) with ID = {self.game_id} not found!"

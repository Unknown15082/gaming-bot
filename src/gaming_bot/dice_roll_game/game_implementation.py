import random


class DiceRollGame(object):
    def __init__(self, target: int) -> None:
        self.target: int = target  # The target number to achieve
        self.player_num: int = 2  # Currently default to 2 players
        self.scores: list[int] = []
        self.reset()  # Initialize the scores

        self.current_player: int = 0  # The current player, 0-indexed
        self.accumulate: int = 0  # The total points of this current turn

    def reset(self) -> None:
        """
        Return the scores of each player to 0.
        """
        self.scores = [0] * self.player_num

    def next_turn(self) -> None:
        """
        Switch to the next player.
        """
        self.current_player += 1
        if self.current_player >= self.player_num:
            self.current_player -= self.player_num

        self.accumulate = 0  # Set the total score for the round to 0

    def roll(self) -> int:
        """
        Simulate and return a dice roll from 1 -> 6.
        """
        value: int = random.randint(1, 6)
        self.resolve_roll(value)  # Resolve this roll
        return value

    def resolve_roll(self, value: int) -> None:
        """
        Handles the result of the dice roll.
        """
        if value == 1:  # Rolls a 1 => Set accumulate to 0, end turn immediately
            self.accumulate = 0
            self.next_turn()
        else:  # Add the values to accumulate
            self.accumulate += value

    def save(self) -> None:
        """
        Handles when the player save their results.
        """
        self.scores[self.current_player] += self.accumulate
        self.next_turn()

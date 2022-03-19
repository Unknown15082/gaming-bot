import disnake


class DiceRollSetup(disnake.ui.View):
    def __init__(self) -> None:
        super().__init__()

        self.level: int | None = None

        for level in range(3):  # Hard-coded values
            self.add_item(DiceRollSetupButton(level))


class DiceRollSetupButton(disnake.ui.Button):
    def __init__(self, level: int) -> None:
        # The label is set to level + 1, since level is 0-based
        super().__init__(
            style=disnake.ButtonStyle.blurple,
            custom_id=f"dice_roll_setup_button::level_{level}",
            label=f"Level {level + 1}",
            row=level,
        )
        self.level = level

    async def callback(self, inter: disnake.MessageInteraction) -> None:
        assert self.view is not None
        view: DiceRollSetup = self.view
        view.level = self.level

        view.clear_items()
        await inter.response.edit_message(
            content=f"The AI level is chosen to be {self.level + 1}...", view=view
        )

import logging
import random
from typing import List

from dnd_character_sheet.utils.exceptions import InvalidInputException

logger = logging.getLogger(__name__)


class DiceRoller:
    def __init__(self) -> None:
        random.seed()

    def roll_n_sided_die(self, num_dice_sides: int):
        if num_dice_sides <= 0:
            raise InvalidInputException(str(num_dice_sides), "number greater than 0")
        logger.debug(f"Rolling {num_dice_sides}-sided die")
        dice_roll = random.randrange(1, num_dice_sides, 1)
        logger.debug(f"Rolled a {dice_roll}!")
        return dice_roll

    def roll_x_num_of_n_sided_die(
        self, num_dice_sides: int, num_dice_to_roll: int
    ) -> List[int]:
        if num_dice_to_roll <= 0:
            raise InvalidInputException(str(num_dice_to_roll), "number greater than 0")
        logger.debug(f"Rolling {num_dice_sides}-sided die {num_dice_to_roll} times")
        all_dice_rolls = []
        for roll in range(num_dice_to_roll):
            logger.debug(
                f"On roll {roll} out of {num_dice_to_roll}, {num_dice_to_roll - roll} to go!"
            )
            dice_roll = self.roll_n_sided_die(num_dice_sides)
            all_dice_rolls.append(dice_roll)
        return all_dice_rolls

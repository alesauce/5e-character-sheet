import logging
import random
from typing import Optional

from dnd_character_sheet.utils.exceptions import InvalidInputException

logger = logging.getLogger(__name__)


class DiceRoller:
    def __init__(self) -> None:
        pass

    def roll_n_sided_die(self, num_dice_sides: int):
        random.seed()
        if num_dice_sides <= 0:
            raise InvalidInputException(str(num_dice_sides), "number greater than 0")
        logger.debug(f"Rolling {num_dice_sides}-sided die")
        dice_roll = random.randrange(1, num_dice_sides, 1)
        logger.debug(f"Rolled a {dice_roll}!")
        return dice_roll

    def roll_x_num_of_n_sided_die(
        self, num_dice_sides: int, num_dice_to_roll: int, sort_rolls: Optional[bool] = False
    ) -> list[int]:
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
        if sort_rolls:
            all_dice_rolls.sort()
        return all_dice_rolls

    def sum_dice_rolls(self, rolls_to_sum: list[int]) -> int:
        total_nums_to_add = len(rolls_to_sum)
        logger.debug(f"Summing up {total_nums_to_add} numbers")
        if total_nums_to_add == 0:
            logger.debug("Reached base case")
            return 0
        elif total_nums_to_add == 1:
            logger.debug("Reached base case")
            return rolls_to_sum[0]
        else:
            return rolls_to_sum[-1] + self.sum_dice_rolls(rolls_to_sum[:-1])

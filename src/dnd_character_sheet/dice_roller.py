import logging
import random
from typing import List

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

    """
    Idea to try to implement quicksort with a random pivot point:
        1. decide on the pivot point, either with a PRNG, or by picking the halway point
        1. (potential helper method) create a new list of every element but the pivot point
        1. run the less/greater than methods on those lists (potential helper method)
        1. recurse with the less than/greater than lists after
    """
    def sort_dice_rolls(self, rolls_to_sort: List[int]) -> List[int]:
        total_nums_to_sort = len(rolls_to_sort)
        logger.info(f"Sorting {total_nums_to_sort} dice rolls with value(s): {rolls_to_sort}")
        if len(rolls_to_sort) < 2:
            logger.debug(f"Reached base case with value(s): {rolls_to_sort}")
            return rolls_to_sort
        else:
            pivot = rolls_to_sort[0]
            less = [num for num in rolls_to_sort[1:] if num <= pivot]
            greater = [num for num in rolls_to_sort[1:] if num > pivot]
            return (self.sort_dice_rolls(less) + [pivot] + self.sort_dice_rolls(greater))

    def sum_dice_rolls(self, rolls_to_sum: List[int]) -> int:
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

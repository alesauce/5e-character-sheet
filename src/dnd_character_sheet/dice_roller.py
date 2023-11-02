import logging
import random

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
        return all_dice_rolls

    def sort_dice_rolls(self, rolls_to_sort: list[int]) -> list[int]:
        total_nums_to_sort = len(rolls_to_sort)
        logger.info(f"Sorting {total_nums_to_sort} dice rolls with value(s): {rolls_to_sort}")
        if len(rolls_to_sort) < 2:
            logger.debug(f"Reached base case with value(s): {rolls_to_sort}")
            return rolls_to_sort
        else:
            random.seed()
            pivot_index = random.randrange(0, len(rolls_to_sort))
            pivot = rolls_to_sort[pivot_index]
            partitioned_list = self._partition_list_from_pivot_point(pivot_index, rolls_to_sort)
            less = [num for num in partitioned_list if num <= pivot]
            greater = [num for num in partitioned_list if num > pivot]
            return (self.sort_dice_rolls(less) + [pivot] + self.sort_dice_rolls(greater))

    def _partition_list_from_pivot_point(self, pivot_index: int, list_to_partition: list[int]) -> list[int]:
        logger.info(f"Partitioning list from index {pivot_index} with value: {list_to_partition[pivot_index]}")
        if (pivot_index == (len(list_to_partition) - 1)):
            logger.debug("No items after pivot index.")
            list_items_after = []
        else:
            list_items_after = list_to_partition[(pivot_index + 1):]
        if (pivot_index == 0):
            logger.debug("No items before pivot index.")
            list_items_before = []
        else:
            list_items_before = list_to_partition[:pivot_index]
        partitioned_list = list_items_before + list_items_after
        logger.debug(f"Created new partitioned list: {partitioned_list=}")
        return partitioned_list

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

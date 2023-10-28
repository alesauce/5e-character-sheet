from random import randrange
import logging
from typing import List


logger = logging.getLogger(__name__)


def roll_n_sided_die(num_dice_sides: int):
    if num_dice_sides <= 0:
        logger.error("Can't be lower than 0, ya dummy!")
    logger.debug(f"Rolling {num_dice_sides}-sided die")
    dice_roll = randrange(1, num_dice_sides, 1)
    logger.debug(f"Rolled a {dice_roll}!")
    return dice_roll


def roll_n_sided_die_x_times(num_dice_sides: int, num_rolls: int) -> List[int]:
    if num_rolls <= 0:
        logger.error("Gotta roll it at least one time, ya dummy!")
    logger.debug(f"Rolling {num_dice_sides}-sided die {num_rolls} times")
    all_dice_rolls = []
    for roll in range(1, num_rolls, 1):
        logger.debug(f"On roll {roll} out of {num_rolls}, {num_rolls - roll} to go!")
        all_dice_rolls.append(roll_n_sided_die(num_dice_sides))
    return all_dice_rolls


def roll_dice_for_ability_scores() -> List[int]:
    NUM_DICE_SIDES = 6
    NUM_DICE_TO_ROLL = 4
    NUM_TIMES_TO_ROLL = 6
    logger.info("Rolling to determine ability scores.")
    ability_scores_final = []
    completed_rolls = 1
    while completed_rolls <= NUM_TIMES_TO_ROLL:
        all_dice_rolls = roll_n_sided_die_x_times(NUM_DICE_SIDES, NUM_DICE_TO_ROLL)
        sorted_rolls = quicksort(all_dice_rolls)
        highest_three = sorted_rolls[-3:]
        ability_score = sum_list(highest_three)
        ability_scores_final.append(ability_score)
    return ability_scores_final


def quicksort(nums_to_sort: List[int]) -> List[int]:
    total_nums_to_sort = len(nums_to_sort)
    logger.info(f"Sorting {total_nums_to_sort} numbers")
    if len(nums_to_sort) < 2:
        logger.debug("Reached base case")
        return nums_to_sort
    else:
        halfway_point = total_nums_to_sort // 2
        pivot = nums_to_sort[halfway_point]
        less = [num for num in nums_to_sort[: halfway_point - 1] if num <= pivot]
        greater = [num for num in nums_to_sort[halfway_point + 1 :] if num <= pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def sum_list(nums_to_add: List[int]) -> int:
    total_nums_to_add = len(nums_to_add)
    logger.debug(f"Summing up {total_nums_to_add} numbers")
    if total_nums_to_add == 0:
        logger.debug("Reached base case")
        return 0
    elif total_nums_to_add == 1:
        logger.debug("Reached base case")
        return nums_to_add[0]
    else:
        return nums_to_add[-1] + sum_list(nums_to_add[:-1])

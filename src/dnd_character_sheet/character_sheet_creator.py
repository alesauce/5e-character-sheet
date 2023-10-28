import logging
from typing import List
from dice_roller import DiceRoller


logging.basicConfig(
    filename="5e_character_sheet_app.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s: [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


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


def roll_dice_for_ability_scores() -> List[int]:
    NUM_DICE_SIDES = 6
    NUM_DICE_TO_ROLL = 4
    NUM_TIMES_TO_ROLL = 6
    logger.info("Rolling to determine ability scores.")
    ability_scores_final = []
    completed_rolls = 1
    while completed_rolls <= NUM_TIMES_TO_ROLL:
        all_dice_rolls = DiceRoller().roll_x_num_of_n_sided_die(
            NUM_DICE_SIDES, NUM_DICE_TO_ROLL
        )
        sorted_rolls = quicksort(all_dice_rolls)
        highest_three = sorted_rolls[-3:]
        ability_score = sum_list(highest_three)
        ability_scores_final.append(ability_score)
    return ability_scores_final

def create_character_sheet_from_scratch():
    """
    Following the basic flow from my diagram:
        1. Choose race
        1. Choose subrace
        1. Note down traits from each
        1. Choose class
        1. Calculate hit points
        1. Roll for/Choose ability scores
        1. Calculate modifiers
        1. Choose equipment (probably more after this, but it's all in the same vein so I'll map it out later)
    """
    pass

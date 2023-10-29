import logging
from typing import List

from dnd_character_sheet.dice_roller import DiceRoller

logging.basicConfig(
    filename="5e_character_sheet_app.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s: [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
dice_roller = DiceRoller()


def roll_dice_for_ability_scores() -> List[int]:
    NUM_DICE_SIDES = 6
    NUM_DICE_TO_ROLL = 4
    NUM_TIMES_TO_ROLL = 6
    logger.info("Rolling to determine ability scores.")
    ability_scores_final = []
    attempted_rolls = 1
    while attempted_rolls <= NUM_TIMES_TO_ROLL:
        logger.debug(f"Attempting roll {attempted_rolls} out of {NUM_TIMES_TO_ROLL}")
        all_dice_rolls = dice_roller.roll_x_num_of_n_sided_die(
            NUM_DICE_SIDES, NUM_DICE_TO_ROLL
        )
        sorted_rolls = dice_roller.sort_dice_rolls(all_dice_rolls)
        highest_three = sorted_rolls[-3:]
        ability_score = dice_roller.sum_dice_rolls(highest_three)
        ability_scores_final.append(ability_score)
        attempted_rolls += 1
    return ability_scores_final


def get_all_srd_races():
    pass


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

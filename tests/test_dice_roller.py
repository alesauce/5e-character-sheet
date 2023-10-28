from dnd_character_sheet.dice_roller import DiceRoller
from dnd_character_sheet.utils.exceptions import InvalidInputException
import pytest


dice_roller = DiceRoller()


def test_roll_n_sided_die_bad_input():
    with pytest.raises(InvalidInputException):
        dice_roller.roll_n_sided_die(-3)


def test_roll_sided_die():
    roll_d20 = dice_roller.roll_n_sided_die(20)
    assert roll_d20 is not None
    assert roll_d20 <= 20
    assert roll_d20 >= 1

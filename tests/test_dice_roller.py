import pytest
from dnd_character_sheet.dice_roller import DiceRoller
from dnd_character_sheet.utils.exceptions import InvalidInputException

dice_roller = DiceRoller()


def test_roll_n_sided_die_negative_input():
    with pytest.raises(InvalidInputException):
        dice_roller.roll_n_sided_die(-3)


def test_roll_n_sided_die():
    roll_d20 = dice_roller.roll_n_sided_die(20)
    assert roll_d20 is not None
    assert roll_d20 <= 20
    assert roll_d20 >= 1


def test_roll_x_num_of_n_sided_die_negative_input():
    with pytest.raises(InvalidInputException):
        dice_roller.roll_x_num_of_n_sided_die(20, -20)


def test_roll_x_num_of_n_sided_die():
    roll_4_d20 = dice_roller.roll_x_num_of_n_sided_die(20, 4)
    assert roll_4_d20 is not None
    assert len(roll_4_d20) == 4

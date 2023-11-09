import pytest
from dnd_character_sheet.dice_roller import DiceRoller
from dnd_character_sheet.utils.exceptions import InvalidInputException
import logging

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


def test_sum_dice_rolls(random_number_list):
    total = dice_roller.sum_dice_rolls(random_number_list)
    assert total is not None
    assert total == 3635953


def test_sum_dice_rolls_no_numbers():
    total = dice_roller.sum_dice_rolls([])
    assert total is not None
    assert total == 0


def test_sort_dice_rolls(caplog, random_number_list):
    caplog.set_level(logging.DEBUG)
    sorted_list = dice_roller.sort_dice_rolls(random_number_list)
    assert sorted_list is not None
    assert sorted_list == [118746, 222767, 385105, 534536, 754958, 766371, 853470]

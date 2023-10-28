import logging


logging.basicConfig(
    filename="5e_character_sheet_app.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s: [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


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

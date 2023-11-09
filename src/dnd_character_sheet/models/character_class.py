from pydantic import BaseModel


class CharacterClass(BaseModel):
    name: str
    hit_die: int
    proficiency_choices: str
    subclasses: str

from typing import List, Optional

from pydantic import BaseModel, Field


class DnDBase(BaseModel):
    name: str = Field(frozen=True)
    description: str = Field(frozen=True)


class Trait(DnDBase):
    # TODO: figure this one out
    pass


class Race(DnDBase):
    traits: List[Trait]


class CharacterClass(DnDBase):
    level: int
    pass


class Character(DnDBase):
    race: Race = Field(frozen=True)
    character_class: CharacterClass
    subclass: Optional[CharacterClass]
    level: int
    age: int

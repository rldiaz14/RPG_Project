from __future__ import annotations
from dataclasses import dataclass
from typing import Type

from .base_character import BaseCharacter
from .warrior import Warrior
from .mage import Mage
from .rogue import Rogue

@dataclass(frozen=True)
class CharacterFactory:
    key: str
    cls: Type[BaseCharacter]
    default: dict

    def create_character(self, name: str | None = None, **overrides) -> BaseCharacter:
        kwargs = {**self.default, "name": name or self.default["name"], **overrides}
        return self.cls(**kwargs)


WarriorFactory = CharacterFactory(
    key="warrior",
    cls=Warrior,
    default=dict(name = "Warrior", max_hp=140, attack=14, defense=8, speed=5)
)

MageFactory = CharacterFactory(
    key="mage",
    cls=Mage,
    default=dict(name = "Mage", max_hp=90, attack=8, defense=3, speed=6, mana=60, spell_power=12)
)

RogueFactory = CharacterFactory(
    key="rogue",
    cls=Rogue,
    default=dict(name = "Rogue", max_hp=100, attack=11, defense=4, speed=9)
)



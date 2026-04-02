from dataclasses import dataclass, field
from typing import Dict, Any

from .base_character import BaseCharacter
from .career_stat import MageCareerStat

@dataclass
class Mage(BaseCharacter):
    mana: int = 50
    spell_power: int = 8
    career_stat: MageCareerStat = field(default_factory=MageCareerStat)


    def compute_raw_damage(self, target: BaseCharacter) -> int:
        # If mana available, cast spell (bigger hit)
        if self.mana >= 10:
            self.mana -= 10
            return self.attack + self.spell_power
        return self.attack # basic attack if no mana

    def snapshot(self) -> dict:
        return {**super().snapshot(), "mana": self.mana, "spell_power": self.spell_power}
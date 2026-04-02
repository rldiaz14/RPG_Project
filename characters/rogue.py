from dataclasses import dataclass, field
from typing import Dict, Any

from .base_character import BaseCharacter

from .career_stat import RogueCareerStat

@dataclass
class Rogue(BaseCharacter):
    career_stat: RogueCareerStat = field(default_factory=RogueCareerStat)

    # Rogues: higher crit/dodge by default, and "backstab" vs slower targets
    def __post_init__(self):
        super().__post_init__()
        self.crit_chance = max(self.crit_chance, 0.10)
        self.dodge_chance = max(self.dodge_chance, 0.12)

    def compute_raw_damage(self, target: BaseCharacter) -> int:
        dmg = self.attack
        if self.speed > target.speed:
            dmg += 4 # backstab bonus
        return dmg

    def snapshot(self) -> dict:
        return {**super().snapshot()}
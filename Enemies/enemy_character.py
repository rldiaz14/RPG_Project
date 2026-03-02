from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Any

from characters.base_character import BaseCharacter

BEHAVIORS = {"aggressive", "defensive", "balanced", "caster"}

@dataclass
class EnemyCharacter(BaseCharacter):
    behavior: str = "aggressive"
    spell_resistance: float = 0.0
    element_weakness: dict = field(default_factory=dict) # {"fire": 1.5}
    element_resistance: dict = field(default_factory=dict) # {"ice": 0.5}
    xp_reward: int = 10
    spell_keys: list = field(default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        if self.behavior not in BEHAVIORS:
            raise ValueError(f"Unknown behavior: '{self.behavior}' . Option: {BEHAVIORS}")

    def snapshot(self) -> dict:
        return {**super().snapshot(),
                "behavior": self.behavior,
                "spell_resistance": self.spell_resistance,
                "element_weakness": self.element_weakness,
                "element_resistance": self.element_resistance,
                "xp_reward": self.xp_reward}
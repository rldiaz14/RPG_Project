from dataclasses import dataclass
from typing import Dict, Any

from .base_character import BaseCharacter

@dataclass
class Warrior(BaseCharacter):
    rage: int = 0 # simple resource

    def compute_raw_damage(self, target: BaseCharacter) -> int:
        """Warrior hits harder as rage builds"""
        bonus = self.rage // 10
        return self.effective_stats().get("attack", self.attack) + bonus

    def on_after_attack(self, target: BaseCharacter, outcome: dict) -> None:
        # gain rage when you hit (or even when dodged, your choice)
        self.rage = min(100, self.rage + 15)


    def compute_damage_taken(self, raw_damage: int) -> int:
        # Warrior have better mitigation (flat reduction)
        defense = self.effective_stats().get("defense", self.defense)
        return max(0, raw_damage - (defense + 2))

    def snapshot(self) -> Dict[str, Any]:
        return {**super().snapshot(), "rage": self.rage}
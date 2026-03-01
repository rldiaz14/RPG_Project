from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Any

from combat.magic_damage import apply_element_modifier, apply_spell_damage
from combat.rng import roll
from combat.damage import apply_defense


@dataclass
class BaseCharacter:
    name: str

    # Core stats
    level: int = 1
    max_hp: int = 100
    attack: int = 10
    defense: int = 5
    speed: int = 5

    # Probabilities stats
    crit_chance: float = 0.10
    crit_multiplier: float = 1.5
    dodge_chance: float = 0.05

    # Runtime
    hp: int = field(init=False)

    def __post_init__(self) -> None:
        self.hp = self.max_hp

    # ------- Public helper -------
    def is_alive(self) -> bool:
        return self.hp > 0

    def snapshot(self) -> Dict[str, Any]:
        """Small stat dump for debugging/logging"""
        return {
            "class": self.__class__.__name__,
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "crit_chance": self.crit_chance,
            "crit_multiplier": self.crit_multiplier,
            "dodge_chance": self.dodge_chance,
        }

    # ----------- Combat "hooks" (subclasses override these) -----------
    def compute_raw_damage(self, target: BaseCharacter) -> int:
        """Base damage before crit/target mitigation"""
        return self.attack

    def on_before_attack(self, target: BaseCharacter) -> None:
        """Hook: buffs, stance, change, mana checks, etc. """
        return None

    def on_after_attack(self, target: BaseCharacter, outcome: Dict[str, Any]) -> None:
        """Hook: lifesteal, rage gain, poison apply, etc"""
        return None

    def compute_damage_taken(self, raw_damage: int) -> int:
        """Mitigation formula (override for shield/armor types)."""
        return apply_defense(raw_damage, self.defense)


    # ---------- Core action ---------------
    def take_damage(self, raw_damage: int) -> Dict[str, Any]:
        # dodge check
        if roll(self.dodge_chance):
            return {"dodge": True, "damage_taken": 0, "hp": self.hp}

        dmg =self.compute_damage_taken(raw_damage)
        self.hp = max(0, self.hp - dmg)
        return {"dodge": False, "damage_taken": dmg, "hp": self.hp}

    def heal(self, amount: int) -> int:
        if amount <= 0:
            return 0
        before = self.hp
        self.hp =min(self.max_hp, self.hp + amount)
        return self.hp - before

    def attack_target(self, target: BaseCharacter) -> Dict[str, Any]:
        self.on_before_attack(target)

        raw =self.compute_raw_damage(target)

        # crit check
        crit = roll(self.crit_chance)
        if crit:
            raw = int(raw * self.crit_multiplier)

        result = target.take_damage(raw)

        outcome = {
            "attacker": self.name,
            "attacker_class": self.__class__.__name__,
            "target": target.name,
            "target_class": target.__class__.__name__,
            "crit": crit,
            **result,
        }
        self.on_after_attack(target, outcome)
        return outcome

    def effective_stats(self, equipment=None):
        """

        Returns a stats snapshot after applying equipment (if provided).
        Does not mutate the character.
        """
        base = self.snapshot()
        if equipment is None:
            return base
        return equipment.apply_all(base)


    def take_spell_damage(self, raw_damage: int, element: str = None) -> Dict[str, Any]:
        # dodge check
        if roll(self.dodge_chance):
            return {"dodge": True, "damage_taken": 0, "hp": self.hp}

        dmg = apply_spell_damage(raw_damage, self)

        if element:
            dmg = apply_element_modifier(dmg, element, self)

        self.hp = max(0, self.hp - dmg)
        return {"dodge": False, "damage_taken": dmg, "hp": self.hp}
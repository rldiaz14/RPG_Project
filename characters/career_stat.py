from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class WarriorCareerStat:
    # Offensive tracking
    rage_triggers: int = 0      # times that rages was used in damage
    heavy_hits: int = 0         # hits above damage threshold
    total_damage_dealt: int = 0       # cumulative damage dealt


    # Defensive tracking
    damage_absorbed: int = 0    # total damage mitigated
    blocks: int = 0             # hits reduced to 0
    total_damage_taken: int = 0 # cumulative damage taken

    # Battle tracking
    battles_fought: int = 0
    battles_won: int = 0
    enemies_defeated: int = 0
    turns_survived: int = 0


    def snapshot(self) -> Dict[str, Any]:
        return {
            "rage_triggers": self.rage_triggers,
            "heavy_hits": self.heavy_hits,
            "total_damage_dealt": self.total_damage_dealt,
            "damage_absorbed": self.damage_absorbed,
            "blocks": self.blocks,
            "total_damage_taken": self.total_damage_taken,
            "battles_fought": self.battles_fought,
            "battles_won": self.battles_won,
            "enemies_defeated": self.enemies_defeated,
            "turns_survived": self.turns_survived,
        }

@dataclass
class MageCareerStat:
    # Spell tracking
    spell_cast: int = 0
    spell_hits: int = 0
    spell_missed: int = 0
    total_spell_damage: int = 0

    # Element tracking
    element_used: Dict[str, int] = field(default_factory=dict)
    consecutive_hits: int = 0
    max_consecutive_hits: int = 0

    # Resource tracking
    total_mana_spent: int = 0
    times_out_of_mana: int = 0

    # Battle Tracking
    battles_fought: int = 0
    battles_won: int = 0
    enemies_defeated: int = 0
    turns_survived: int = 0

    def snapshot(self) -> Dict[str, Any]:
        return {
            "spell_cast": self.spell_cast,
            "spell_hits": self.spell_hits,
            "spell_missed": self.spell_missed,
            "total_spell_damage": self.total_spell_damage,
            "element_used": self.element_used,
            "consecutive_hits": self.consecutive_hits,
            "max_consecutive_hits": self.max_consecutive_hits,
            "total_mana_spent": self.total_mana_spent,
            "times_out_of_mana": self.times_out_of_mana,
            "battles_fought": self.battles_fought,
            "battles_won": self.battles_won,
            "enemies_defeated": self.enemies_defeated,
            "turns_survived": self.turns_survived,
        }

@dataclass
class RogueCareerStat:
    # Offensive tracking
    backstabs: int = 0          # speed advantage hits
    crits: int = 0              # critical hits landed
    kill_shots: int = 0         # finishing blows
    total_damage_dealt: int = 0

    # Defensive tracking
    dodges: int =0
    total_damage_taken: int = 0

    # Battle Tracking
    battles_fought: int = 0
    battles_won: int = 0
    enemies_defeated: int = 0
    turns_survived: int = 0

    def snapshot(self) -> Dict[str, Any]:
        return {
            "backstabs": self.backstabs,
            "crits": self.crits,
            "kill_shots": self.kill_shots,
            "total_damage_dealt": self.total_damage_dealt,
            "dodges": self.dodges,
            "total_damage_taken": self.total_damage_taken,
            "battles_fought": self.battles_fought,
            "battles_won": self.battles_won,
            "enemies_defeated": self.enemies_defeated,
            "turns_survived": self.turns_survived,

        }


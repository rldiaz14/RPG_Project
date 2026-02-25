from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class CombatTracker:
    attacks_by: Dict[str, int] = field(default_factory=dict)
    crits_by: Dict[str, int] = field(default_factory=dict)
    damage_done: Dict[str, int] = field(default_factory=dict)

    attacks_received: Dict[str, int] = field(default_factory=dict)
    dodges_by: Dict[str, int] = field(default_factory=dict)


    wins: Dict[str, int] = field(default_factory=dict)
    total_turns: int = 0
    duels: int = 0

    def _ensure(self, name: str) -> None:
        for d in (self.attacks_by, self.crits_by, self.damage_done,
                  self.attacks_received, self.dodges_by, self.wins):
            d.setdefault(name, 0)

    def record_attack(self, attacker_name: str, defender_name: str, outcome: Dict[str,Any]) -> None:
        self._ensure(attacker_name)
        self._ensure(defender_name)

        self.attacks_by[attacker_name] += 1
        self.crits_by[attacker_name] += int(outcome.get('crit', False))
        self.damage_done[attacker_name] += int(outcome.get('damage_taken', 0))

        self.attacks_received[defender_name] += 1
        self.dodges_by[defender_name] += int(outcome.get('dodge', False))

    def record_duel(self, winner_name: str, turns: int) -> None:
        self._ensure(winner_name)
        self.wins[winner_name] += 1
        self.total_turns += turns
        self.duels += 1
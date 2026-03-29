from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class BattleResult:
    outcome: str   # "win", "lose", "flee", "draw"
    turns: int
    xp_gained: int
    log: list[dict] = field(default_factory=list)
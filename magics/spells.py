from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

from elements import Element

@dataclass(frozen=True)
class Spell:
    key: str
    name: str
    element: Element
    cost_mana: int
    power: int       # added to caster spell_power
    accuracy: float  #0.0 - 1.0


SPELLS: Dict[str, Spell] = {
    "fireball": Spell(
        key="fireball",
        name="Fireball",
        element=Element.FIRE,
        cost_mana=10,
        power=12,
        accuracy=0.90,
    )
}

def get_spell(key: str) -> Spell:
    k = key.lower().strip().replace(" ", "_").replace("-","_")
    if k not in SPELLS:
        raise ValueError(f"Unknown spell '{key}'. Options: {list(SPELLS.keys())}")
    return SPELLS[k]
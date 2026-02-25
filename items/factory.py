from __future__ import annotations
from typing import Dict, Any


from .weapon import Weapon
from .clothes import Clothes
from .armament  import Armament
from .types import WeaponType, ClothesType, Stat


ITEMS: Dict[str, Dict[str, Any]] = {
    # ---- Weapon -----
    "iron_sword": {
        "cls": Weapon,
        "args": {"name": "Iron Sword", "weapon_type": WeaponType.SWORD},
        "mods": {Stat.ATTACK: 3},
        "element": None,
    },
    "fire_staff": {
        "cls": Weapon,
        "args": {"name": "Fire Staff", "weapon_type": WeaponType.STAFF},
        "mods": {Stat.ATTACK: 1, Stat.SPELL_POWER: 4},
        "element": "fire",

    },
    "poison_dagger": {
      "cls": Weapon,
      "args": {"name": "Poison Dagger", "weapon_type": WeaponType.DAGGER},
      "mods": {Stat.ATTACK: 2, Stat.CRIT_CHANCE: 0.05},
      "element": "poison",
    },
    # ----- Clothes ----
    "steel_armor":{
    "cls": Clothes,
    "args": {"name": "Steel Armor" ,"clothes_type": ClothesType.ARMOR},
    "mods": {Stat.DEFENSE: 4, Stat.SPEED: -1},
    "element": None,
    },
    "ice_robes":{
    "cls": Clothes,
    "args": {"name": "Ice Robes", "clothes_type": ClothesType.ROBES},
    "mods": {Stat.DEFENSE: 2, Stat.SPELL_POWER: 2},
    "element": "ice",
    },

    # -------- Armament -------
    "dark_charm":{
    "cls": Armament,
    "args": {"name": "Dark Charm"},
    "mods": {Stat.CRIT_CHANCE: 0.03, Stat.DODGE_CHANCE: 0.02},
    "element": "dark_magic",
    },
}

def _norm(s: str) -> str:
    return s.lower().strip().replace(" ", "_").replace("-","_")

def create_item(item_id: str):
    key = _norm(item_id)
    if key not in ITEMS:
        raise ValueError(f"Unknown item id: {item_id}. Options are: {list(ITEMS.keys())}")

    spec = ITEMS[key]
    cls = spec["cls"]
    args = dict(spec.get("args", {}))
    mods = dict(spec.get("mods", {}))
    element = spec.get("element", None)

    # All  item classes accept (name, type..., modifiers, element)
    return cls(modifiers=mods, element=element, **args)

def available_items():
    return list(ITEMS.keys())
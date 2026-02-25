from __future__ import annotations
from dataclasses import dataclass
from typing import Optional,Dict



from .base import Item
from .types import ItemCategory, WeaponType, Stat

@dataclass(frozen=True)
class Weapon(Item):
    weapon_type: WeaponType = WeaponType.SWORD

    def __init__(self,name: str, weapon_type : WeaponType,
                 modifiers: Optional[Dict[Stat, float]] = None,
                 element: Optional[str] = None):
        super().__init__(name=name, category=ItemCategory.WEAPON, modifiers=modifiers or {}, element=element)
        object.__setattr__(self, "weapon_type", weapon_type)
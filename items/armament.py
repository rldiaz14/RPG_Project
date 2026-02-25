from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict


from .base import Item
from .types import ItemCategory, Stat


@dataclass(frozen=True)
class Armament(Item):
    """
    Generic extra gear (shield, ring, amulet, charm)
    Later you can add Armament enum if you want.
    """
    def __init__(self, name: str, modifiers: Optional[Dict[Stat, float]] = None, element: Optional[str] = None):
        super().__init__(name=name, category=ItemCategory.ARMAMENT, modifiers=modifiers or {}, element=element)
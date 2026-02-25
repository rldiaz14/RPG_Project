from __future__ import annotations
from dataclasses import dataclass
from typing import Dict,Optional

from .base import Item
from .types import ItemCategory, ClothesType, Stat

@dataclass(frozen=True)
class Clothes(Item):
    clothes_type: ClothesType = ClothesType.ARMOR

    def __init__(self, name: str, clothes_type: ClothesType,
                 modifiers: Optional[Dict[Stat, float]] = None,
                 element: Optional[str] = None):

        super().__init__(name=name, category=ItemCategory.CLOTHES, modifiers=modifiers or {}, element=element)
        object.__setattr__(self, "clothes_type", clothes_type)
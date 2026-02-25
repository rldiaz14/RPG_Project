from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional


from .base import Item
from .weapon import Weapon
from .clothes import Clothes
from .armament import Armament

@dataclass
class Equipment:
    weapon: Optional[Weapon]=None
    clothes: Optional[Clothes]=None
    armament: Optional[Armament]=None


    def apply_all(self, base_stats: Dict[str, Any]) -> Dict[str, Any]:
        """

        Pure Function: return a modified version of base_stats after applying all equipped items.
        """
        out = dict(base_stats)
        for item in (self.weapon, self.clothes, self.armament):
            if item is not None:
                out = item.apply(out)

        return out

    def summary(self) -> Dict[str, str]:
        return {
            "weapon": self.weapon.name if self.weapon else "None",
            "clothes": self.clothes.name if self.clothes else "None",
            "armament": self.armament.name if self.armament else "None",
        }
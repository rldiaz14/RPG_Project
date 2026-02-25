from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .types import ItemCategory, Stat

@dataclass(frozen=True)
class Item:
    name: str
    category: ItemCategory
    modifiers: Dict[str, float] = field(default_factory=dict)
    element: Optional[str] = None

    def apply(self, stats: Dict[str, Any]) -> Dict[str, Any]:
        """

         Takes a character snapshot dict-like and returns a modifiers copy.
         (Does NOT mutate the character; it's a pure stat view)
        """
        out = dict(stats)
        for k, v in self.modifiers.items():
            key = k.value
            if key in out and isinstance(out[key], (int, float)):
                out[key] = out[key] + v
            else:
                out[key] = v
        return out

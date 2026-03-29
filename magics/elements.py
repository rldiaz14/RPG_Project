from __future__ import annotations
from enum import Enum

class Element(str, Enum):
    FIRE = "fire"
    ICE = "ice"
    POISON = "poison"
    DARK = "dark"

def normalize_element(s: str) -> Element:
    key = s.lower().strip().replace(" ", "_").replace("-","_")
    return Element(key)
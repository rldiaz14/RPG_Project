from __future__ import annotations
from enum import Enum


class ItemCategory(str, Enum):
    WEAPON = "weapon"
    CLOTHES = "clothes"
    ARMAMENT = "armament"

class WeaponType(str, Enum):
    SWORD = "sword"
    DAGGER = "dagger"
    STAFF = "staff"
    CLAW = "claw"
    LANCE = "lance"

class ClothesType(str, Enum):
    ARMOR = "armor"
    ROBES = "robes"

class Stat(str, Enum):
    MAX_HP = "max_hp"
    ATTACK = "attack"
    DEFENSE = "defense"
    SPEED = "speed"
    CRIT_CHANCE = "crit_chance"
    DODGE_CHANCE = "dodge_chance"
    SPELL_POWER = "spell_power"

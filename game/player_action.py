from __future__ import annotations
import random

from magics.resolver import cast_spell
from magics.spells import get_spell


def player_attack(attacker, target) -> dict:
    return attacker.attack_target(target)


def player_cast(attacker, target, spell_key: str) -> dict:
    try:
        spell = get_spell(spell_key)
    except ValueError:
        return {
            "type": "spell",
            "success": False,
            "reason": f"unknown_spell:{spell_key}",
            "caster": attacker.name,
            "target": target.name,
        }
    return cast_spell(attacker, target, spell)


def player_flee(character, enemy) -> dict:
    base_chance = 0.25
    speed_bonus = (character.speed - enemy.speed) * 0.05
    flee_chance = max(0.10, min(0.90, base_chance + speed_bonus))
    success = random.random() < flee_chance
    return {
        "type": "flee",
        "attacker": character.name,
        "success": success,
        "flee_chance": round(flee_chance, 2),
    }
def default_action(player, enemy) -> dict:
    return player_attack(player, enemy)

def flee_action(player, enemy) -> dict:
    return player_flee(player, enemy)

def cast_action(spell_key: str):
    def _cast(player, enemy) -> dict:
        return player_cast(player, enemy, spell_key)
    return _cast

def player_use_item(character, item) -> dict:
    # TODO: implement when inventory system is built
    pass
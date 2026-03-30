from __future__ import annotations
import random

from magics.resolver import cast_spell
from magics.spells import get_spell

def player_attack(attacker, target) -> dict:
    return attacker.attack_target(target)

def player_cast(attacker, target, spell_key: str) -> dict:
    """
    Player casts a spell by key name.
    Return outcome dict from cast spell
    :param attacker:
    :param target:
    :param spell_key:
    :return:
    """
    try:
        spell = get_spell(spell_key)
    except ValueError:
        return {
            "type": "spell",
            "success": False,
            "reason": f"unknown_spell: {spell_key}",
            "caster": attacker.name,
            "target": target.name,
        }
    return cast_spell(attacker, target ,spell)
def player_flee(character, enemy) -> dict:
    """
    Flee chance based on player speed vs enemy speed.
    Higher player speed = better chance to flee.
    :param character:
    :param enemy: 
    :return:
    """
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

def player_use_item(character, item) -> dict:
    # TODO: implement item usage
    pass

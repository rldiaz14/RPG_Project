import random
from magics.resolver import cast_spell
from magics.spells import get_spell


def enemy_turn(attacker, target, spell_keys: list[str] = None) -> dict:
    """

    Decides and executes enemy actions based on behavior.
    Returns outcome dict.
    """
    behavior = getattr(attacker, "behavior", "aggressive")

    if behavior == "aggressive":
        return _aggressive(attacker, target)
    elif behavior == "defensive":
        return _defensive(attacker, target)
    elif behavior == "balanced":
        return _balanced(attacker, target, spell_keys)
    elif behavior == "caster":
        return _caster(attacker, target, spell_keys)

    return attacker.attack_target(target) # fallback

def _aggressive(attacker, target) -> dict:
    return attacker.attack_target(target)
def _defensive(attacker, target) -> dict:
    hp_percent = attacker.hp / attacker.max_hp

    if hp_percent < 0.5 and attacker.hp < attacker.max_hp:
        # try to heal
        healed = attacker.heal(15)
        return {
            "type": "heal",
            "attacker": attacker.name,
            "healed": healed,
            "hp": attacker.hp,
        }
    return attacker.attack_target(target)

def _balanced(attacker, target, spell_keys: list[str] = None) -> dict:


    # 50/50 between spell and attack if mana available
    if spell_keys and getattr(attacker, "mana", 0) > 0:
        if random.random() < 0.5:
            return _try_cast(attacker, target, spell_keys)
    return attacker.attack_target(target)

def _caster(attacker, target, spell_keys: list[str] = None) -> dict:
    # prefer spell, fallback to attack if no mana
    if spell_keys and getattr(attacker, "mana", 0) > 0:
        return _try_cast(attacker, target, spell_keys)
    return attacker.attack_target(target)

def _try_cast(attacker, target, spell_keys: list[str] = None) -> dict:
    key = random.choice(spell_keys)
    try:
        spell = get_spell(key)
        return cast_spell(attacker, target, spell)
    except ValueError:
        return attacker.attack_target(target)
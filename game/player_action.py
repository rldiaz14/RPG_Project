from __future__ import annotations

def player_attack(attacker, target) -> dict:
    return attacker.attack_target(target)

def player_cast(attacker, target, spell) -> dict:
    # TODO: implement spell location
    pass

def player_use_item(character, item) -> dict:
    # TODO: implement item usage
    pass

def player_flee(character, enemy) -> dict:
    # TODO: implement flee chance
    pass


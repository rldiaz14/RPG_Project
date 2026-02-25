from __future__  import annotations
from typing import Dict,Any


from combat.rng import roll
from .spells import Spell

def cast_spell(caster, target, spell: Spell) -> Dict[str, Any]:
    """
    :param caster has : name, mana (int), spell_power (int)
    :param target has : take_damage(raw_damage) -> dict with "damage_taken", "hp", "dodge"(or "dodged")
    """

    # 1) Mana check
    if getattr(caster, "mana", 0) < spell.cost_mana:
        return {
            "type": "spell",
            "spell": spell.key,
            "spell_name": spell.name,
            "element": spell.element.value,
            "caster": caster.name,
            "target": target.name,
            "success": False,
            "reason": "not_enough_mana",
        }
    caster.mana -= spell.cost_mana

    # 2) Hit toll
    hit = roll(spell.accuracy)
    if not hit:
        return {
            "type": "spell",
            "spell": spell.key,
            "spell_name": spell.name,
            "element": spell.element.value,
            "caster": caster.name,
            "target": target.name,
            "success": False,
            "reason": "miss",
        }

    # 3) Damage calc (simple for now)
    spell_power = getattr(caster, "spell_power", 0)
    raw_damage = spell_power + spell.power

    # 4) Apply damage using existing pipeline
    result = target.take_damage(raw_damage) # expect dodge logic inside take_damage

    return {
        "type": "spell",
        "spell": spell.key,
        "spell_name": spell.name,
        "element": spell.element.value,
        "caster": caster.name,
        "target": target.name,
        "success": True,
        "raw_damage": raw_damage,
        **result, # includes "damage_taken", "hp", and dodge field
    }
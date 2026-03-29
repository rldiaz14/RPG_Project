
def apply_spell_damage(raw: int, target) -> int:
    """
    Spell Mitigation - uses spell-resistance if target has it,
    falls back to half physical defense.
    """
    resistance = getattr(target, "spell_resistance", None)
    if resistance: # only use spell_resistance if it's > 0
        return max(0, raw - resistance)
    return max(0, raw - (target.defense // 2)) # fallback to half defense


def apply_element_modifier(raw: int, element: str, target) -> int:
    """"
    Applies weakness/resistance multipliers based on target's element profile
    """
    weaknesses = getattr(target, "element_weakness", {})
    resistance = getattr(target, "element_resistance", {})

    if element in weaknesses:
        return int(raw * weaknesses[element])
    if element in resistance:
        return int(raw * resistance[element])
    return raw
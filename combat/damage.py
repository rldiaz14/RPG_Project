def apply_defense(raw_damage: int, defense: int) -> int:
    """Simple mitigation formula"""
    return max(0, raw_damage - defense)
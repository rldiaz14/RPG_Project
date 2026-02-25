import random

def roll(chance: float) -> bool:
    """Returns True with probability = chance (0.0 to 1.0)."""
    return random.random() < chance


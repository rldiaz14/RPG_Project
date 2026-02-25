import random

from characters import Mage,Rogue

from tools.tracker import CombatTracker
from tools.report import  print_report




# ---------- Setting ----------
SEED = 123
MAX_TURNS = 50
# ------------------------------

def duel(a, b, tracker: CombatTracker, max_turns= MAX_TURNS, stats=None):
    """

    Runs one duel. If stats dict is provided, it accumulates combat metrics
    Return: {"Winner: <name|draw>, "turns":int}
    """

    turns = 0


    while a.is_alive() and b.is_alive() and turns < max_turns:
        turns += 1

        # who goes first by speed
        first, second = (a, b) if a.speed >= b.speed else (b, a)

        # first attacks
        out1 = first.attack_target(second)
        tracker.record_attack(first.name, second.name, out1)

        # second attacks (only if still alive)
        if second.is_alive():
            out2 = second.attack_target(first)
            tracker.record_attack(second.name, first.name, out2)


    if a.is_alive() and not b.is_alive():
        winner = a.name
    elif b.is_alive() and not a.is_alive():
        winner = b.name
    else:
        winner = "draw"

    tracker.record_duel(winner, turns)

    return {"winner": winner, "turns": turns}

def run_trials(n=1000):
    if SEED is not None:
        random.seed(SEED)

    tracker = CombatTracker()

    for _ in range(n):
        # fresh character each duel
        m = Mage(name="Mage", max_hp=90, attack=8, defense=3, speed=6, mana=60, spell_power=12)
        r = Rogue(name="Rogue", max_hp=100, attack=11, defense=4, speed=9)

        # example match-up: Mage vs Rogue (choose character)
        duel(m, r, tracker)

    print_report(tracker, fighters=["Mage", "Rogue", "draw"])


if __name__ == "__main__":
    run_trials(1000)

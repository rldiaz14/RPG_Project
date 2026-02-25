from typing import List
from .tracker import CombatTracker

def print_report(tracker: CombatTracker, fighters: List[str]) -> None:
    print("\n=== Summary ===")
    print("Duels: ", tracker.duels)
    if tracker.duels > 0:
        print("Avg turns:", tracker.total_turns / tracker.duels)


    print("\n=== Wins ===")
    for f in fighters:
        w = tracker.wins.get(f,0)
        print(f"{f}: {w} ({( w / tracker.duels) if tracker.duels else 0:.3f})")

    print("\n=== Attacker stats crit + damage ===")
    for f in fighters:
        a = tracker.attacks_by.get(f,0)
        if a == 0:
            print(f"{f}: no attacks recorded")
            continue
        crit_rate = tracker.crits_by.get(f,0) / a
        avg_dmg = tracker.damage_done.get(f,0) / a
        print(f"{f}: attacks={a}, crit_rate={crit_rate:.3f}, avg_dmg/attack={avg_dmg:.3f}")

    print("\n=== Defense stats (dodge) ===")
    for f in fighters:
        recv = tracker.attacks_received.get(f,0)
        if recv == 0:
            print(f"{f}: no attacks received")
            continue
        dodge_rate = tracker.dodges_by.get(f,0) / recv
        print(f"{f} received={recv}, dodge_rate={dodge_rate:.3f}")
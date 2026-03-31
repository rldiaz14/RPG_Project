from tools.test_utils import (
    make_warrior, make_enemy,
    assert_eq, assert_in, run_test
)
from game.battle import battle


def test_player_wins():
    w = make_warrior(level=10)
    g = make_enemy("goblin")
    result = battle(w, g)
    assert_eq("outcome", result.outcome, "win")
    print(f"  Turns: {result.turns} | XP: {result.xp_gained}")

def test_enemy_wins():
    w = make_warrior(level=1, max_hp=20, attack=2, defense=1)
    t = make_enemy("troll")
    result = battle(w, t)
    assert_eq("outcome", result.outcome, "loss")
    print(f"  Turns: {result.turns}")

def test_turn_order_enemy_first():
    w = make_warrior(level=1)
    g = make_enemy("goblin")
    result = battle(w, g)
    first = result.log[0].get("attacker", "?")
    assert_eq("enemy goes first", first, g.name)
    print(f"  First actor: {first}")

def test_turn_order_player_first():
    w = make_warrior(level=10)
    g = make_enemy("goblin")
    result = battle(w, g)
    first = result.log[0].get("attacker", "?")
    assert_eq("player goes first", first, w.name)
    print(f"  First actor: {first}")

def test_caster_enemy():
    w = make_warrior(level=10)
    dm = make_enemy("dark_mage")
    mana_before = dm.mana
    result = battle(w, dm)
    print(f"  Outcome: {result.outcome} | Turns: {result.turns}")
    print(f"  Dark Mage mana: {mana_before} → {dm.mana}")
    for entry in result.log:
        print(f"    {entry.get('type', 'attack')} | "
              f"{entry.get('attacker', entry.get('caster', '?'))}")

def test_battle_log():
    w = make_warrior(level=10)
    g = make_enemy("goblin")
    result = battle(w, g)
    assert_in("attacker in first log entry", "attacker", result.log[0])
    print(f"  Total log entries: {len(result.log)}")
    for i, entry in enumerate(result.log):
        print(f"    [{i+1}] {entry.get('attacker', entry.get('caster', '?'))} "
              f"-> {entry.get('target', '?')}")


if __name__ == "__main__":
    run_test(
        test_player_wins,
        test_enemy_wins,
        test_turn_order_enemy_first,
        test_turn_order_player_first,
        test_caster_enemy,
        test_battle_log,
    )
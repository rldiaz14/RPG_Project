from tools.test_utils import (
    make_warrior, make_mage, make_enemy,
    assert_eq, assert_in, assert_false, assert_true, assert_gte, run_test
)
from game.player_action import player_attack, player_cast, player_flee


def test_player_attack():
    w = make_warrior()
    g = make_enemy("goblin")
    result = player_attack(w, g)
    assert_in("damage_taken in result", "damage_taken", result)
    print(f"  Result: {result}")

def test_player_cast_success():
    m = make_mage()
    g = make_enemy("goblin")
    mana_before = m.mana
    result = player_cast(m, g, "fireball")
    assert_eq("spell type", result["type"], "spell")
    print(f"  Mana: {mana_before} → {m.mana}")
    print(f"  Result: {result}")

def test_player_cast_no_mana():
    m = make_mage(mana=0)
    g = make_enemy("goblin")
    result = player_cast(m, g, "fireball")
    assert_false("cast failed", result["success"])
    assert_eq("reason", result["reason"], "not_enough_mana")

def test_player_cast_unknown_spell():
    m = make_mage()
    g = make_enemy("goblin")
    result = player_cast(m, g, "thunder")
    assert_false("unknown spell failed", result["success"])

def test_player_flee_fast():
    w = make_warrior(speed=15)
    g = make_enemy("goblin")
    results = [player_flee(w, g) for _ in range(10)]
    successes = sum(1 for r in results if r["success"])
    flee_chance = results[0]["flee_chance"]
    assert_gte("fast player flee chance", flee_chance, 0.5)
    print(f"  Flee chance: {flee_chance} | Successes: {successes}/10")

def test_player_flee_slow():
    w = make_warrior(speed=2)
    t = make_enemy("troll")
    results = [player_flee(w, t) for _ in range(10)]
    successes = sum(1 for r in results if r["success"])
    flee_chance = results[0]["flee_chance"]
    print(f"  Flee chance: {flee_chance} | Successes: {successes}/10")


if __name__ == "__main__":
    run_test(
        test_player_attack,
        test_player_cast_success,
        test_player_cast_no_mana,
        test_player_cast_unknown_spell,
        test_player_flee_fast,
        test_player_flee_slow,
    )
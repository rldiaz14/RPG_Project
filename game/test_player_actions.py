import random
from characters.factory import WarriorFactory, MageFactory
from Enemies.enemy_factory import spawn_enemy
from game.player_action import player_attack, player_cast, player_flee


random.seed(42)  # Set seed for reproducibility

def test_player_attack():
    print("\n==== Test: Player Attack ====")
    w = WarriorFactory.create(name="Guts")
    g = spawn_enemy("goblin")

    result = player_attack(w, g)
    print(f"Result: {result}")
    assert "damage_taken" in result  # Goblin starts with 20 HP at level 3
    print("PASSED")

def test_player_cast_success():
    print("\n==== Test: Player Cast Success ====")
    m = MageFactory.create(name="Vivi")
    g = spawn_enemy("goblin")

    print(f"Vivi mana before: {m.mana}")
    result = player_cast(m, g, "fireball")
    print(f"Vivi mana after: {m.mana}")
    assert result["type"] == "spell"
    print("PASSED")

def test_player_cast_no_mana():
    print("\n==== Test: Player Cast No Mana ====")
    m = MageFactory.create(name="Vivi", mana=0)
    g = spawn_enemy("goblin")

    result = player_cast(m, g, "fireball")
    print(f"Result: {result}")
    assert result["success"] == False
    assert result["reason"] == "not_enough_mana"
    print("PASSED")

def test_player_cast_unknown_spell():
    print("\n==== Test: Player Cast Unknown Spell ====")
    m = MageFactory.create(name="Vivi")
    g = spawn_enemy("goblin")

    result = player_cast(m, g, "thunder")
    print(f"Result: {result}")
    assert result["success"] == False
    print("PASSED")

def test_player_flee_fast():
    print("\n==== Test: Player Flee (fast player) ====")
    r = WarriorFactory.create(name="Guts", speed=15)
    g = spawn_enemy("goblin") # speed 7

    result = [player_flee(r, g) for _ in range(10)]
    successes = sum(1 for r in result if r["success"])
    print(f"Flee chance: {result[0]['flee_chance']} ")
    print(f"Successes in 10 attempts: {successes}")
    print("PASSED")

def test_player_flee_slow():
    print("\n==== Test: Player Flee (slow player) ====")
    w = WarriorFactory.create(name="Guts", speed=2)
    t = spawn_enemy("troll") # speed 3

    result = [player_flee(w, t) for _ in range(10)]
    success = sum(1 for r in result if r ["success"])
    print(f"Flee chance: {result[0]['flee_chance']} ")
    print(f"Successes in 10 attempts: {success}")
    print("PASSED")


if __name__ == "__main__":
    test_player_attack()
    test_player_cast_success()
    test_player_cast_no_mana()
    test_player_cast_unknown_spell()
    test_player_flee_fast()
    test_player_flee_slow()
import random
from characters.factory import WarriorFactory
from Enemies.enemy_factory import spawn_enemy
from game.battle import battle

random.seed(42)

def test_turn_order_at_level(player_level, enemy_level, enemy_key="goblin"):
    w = WarriorFactory.create(name="Guts", level=player_level)
    e = spawn_enemy(enemy_key, level=enemy_level)

    player_score = player_level
    enemy_score = enemy_level + 3

    result = battle(w, e)
    first_actor = result.log[0].get("attacker", result.log[0].get("caster", "?"))

    print(f"Player lvl:{player_level} vs Enemy lvl:{enemy_level} "
          f"| scores: player={player_score} enemy={enemy_score} "
          f"| first: {first_actor}")

if __name__ == "__main__":
    print("\n==== Test: Turn order at different levels ====")
    test_turn_order_at_level(1, 1)   # enemy score 4 vs 1  → enemy first
    test_turn_order_at_level(3, 1)   # enemy score 4 vs 3  → enemy first
    test_turn_order_at_level(4, 1)   # enemy score 4 vs 4  → speed tiebreaker
    test_turn_order_at_level(5, 1)   # enemy score 4 vs 5  → player first
    test_turn_order_at_level(7, 3)   # enemy score 6 vs 7  → player first
    test_turn_order_at_level(5, 3)   # enemy score 6 vs 5  → enemy first
    test_turn_order_at_level(10, 5)  # enemy score 8 vs 10 → player first
    test_turn_order_at_level(10, 10) # enemy score 13 vs 10 → enemy first
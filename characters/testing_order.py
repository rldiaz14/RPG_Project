# game/testing_order.py
from tools.test_utils import make_warrior, make_enemy, assert_eq, run_test
from game.battle import battle


def _check_turn_order(player_level: int, enemy_level: int, expected_first: str, enemy_key: str = "goblin"):
    w = make_warrior(level=player_level)
    e = make_enemy(enemy_key, level=enemy_level)

    player_score = player_level
    enemy_score = enemy_level + 3

    result = battle(w, e)
    first_actor = result.log[0].get("attacker", result.log[0].get("caster", "?"))

    print(f"  Player lvl:{player_level} vs Enemy lvl:{enemy_level} "
          f"| scores: player={player_score} enemy={enemy_score} "
          f"| first: {first_actor}")

    assert_eq(f"turn order lvl {player_level} vs {enemy_level}", first_actor, expected_first)


def test_enemy_goes_first_low_level():
    _check_turn_order(1, 1, "Goblin")   # enemy score 4 vs 1 → enemy first
    _check_turn_order(3, 1, "Goblin")   # enemy score 4 vs 3 → enemy first


def test_speed_tiebreaker():
    _check_turn_order(4, 1, "Goblin")   # tie 4 vs 4 → goblin speed 7 > warrior 5


def test_player_goes_first_high_level():
    _check_turn_order(5, 1, "Guts")    # player 5 > enemy 4 → player first
    _check_turn_order(7, 3, "Guts")    # player 7 > enemy 6 → player first
    _check_turn_order(10, 5, "Guts")   # player 10 > enemy 8 → player first


def test_enemy_goes_first_high_enemy_level():
    _check_turn_order(5, 3, "Goblin")   # enemy 6 > player 5 → enemy first
    _check_turn_order(10, 10, "Goblin") # enemy 13 > player 10 → enemy first


if __name__ == "__main__":
    run_test(
        test_enemy_goes_first_low_level,
        test_speed_tiebreaker,
        test_player_goes_first_high_level,
        test_enemy_goes_first_high_enemy_level,
    )
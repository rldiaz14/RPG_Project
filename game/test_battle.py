import random
from characters.factory import WarriorFactory, MageFactory, RogueFactory
from Enemies.enemy_factory import spawn_enemy
from game.battle import battle

random.seed(42)  # Set seed for reproducibility

def test_player_wins():
    print("\n==== Test: Player Wins (strong player vs goblin) ====")
    w = WarriorFactory.create(name="Guts", level=10)
    g = spawn_enemy("goblin")

    result = battle(w, g)
    print(f"Outcome: {result.outcome}")
    print(f"Turns: {result.turns}")
    print(f"XP gained: {result.xp_gained}")
    assert result.outcome == "win"
    print("PASSED")


def test_enemy_wins():
    print("\n==== Test: Enemy Wins (weak player vs Troll) ====")
    w = WarriorFactory.create(name="Guts", level=1, max_hp=20, attack=2, defense=1)
    t = spawn_enemy("troll")

    result = battle(w, t)
    print(f"Outcome: {result.outcome}")
    print(f"Turns: {result.turns}")
    print(f"XP gained: {result.xp_gained}")
    assert result.outcome == "loss"
    print("PASSED")

def test_turn_order_enemy_first():
    print("\n==== Test: Enemy goes first (low level player) ====")
    w = WarriorFactory.create(name="Guts", level=1)
    g = spawn_enemy("goblin")

    print(f"Player level: {w.level} | Enemy Level: {g.level}")
    print(f"Enemy advantage: +3 -> enemy score {g.level + 3} vs player score {w.level}")

    result = battle(w, g)
    print(f"First action log: {result.log[0].get('attacker', 'unknown')}")
    assert result.log[0].get('attacker') == g.name
    print("PASSED")

def test_turn_order_player_first():
    print("\n==== Test: Player goes first (low level player) ====")
    w = WarriorFactory.create(name="Guts", level=10)
    g = spawn_enemy("goblin")

    print(f"Player level: {w.level} | Enemy Level: {g.level}")
    print(f"Enemy advantage: +3 -> enemy score {g.level + 3} vs player score {w.level}")

    result = battle(w, g)
    print(f"First action log: {result.log[0].get('attacker', 'unknown')}")
    assert result.log[0].get('attacker') == w.name
    print("PASSED")

def test_caster_enemy():
    print("\n==== Test: Caster enemy uses spells ====")
    w = WarriorFactory.create(name="Guts", level=10)
    dm = spawn_enemy("dark_mage")

    print(f"Before - Guts hp:{w.hp} | Dark Mage mana:{dm.mana}")
    result = battle(w, dm)
    print(f"Outcome: {result.outcome}")
    print(f"Turns: {result.turns}")
    print(f"Dark Mage mana after: {dm.mana}")
    # add this to see what actions were taken
    for entry in result.log:
        print(f"  {entry.get('type', 'attack')} "
              f"| {entry.get('attacker', entry.get('caster', '?'))}")

def test_log():
    print("\n==== Test:  Battle log ====")
    w = WarriorFactory.create(name="Guts", level=10)
    g = spawn_enemy("goblin")

    result = battle(w, g)
    print(f"Total log entries: {len(result.log)}")
    for i, entry in enumerate(result.log):
        print(f" [{i+1}] {entry.get('attacker', entry.get('caster' , '?'))}"
              f" -> {entry.get('target', '?')}")


if __name__ == "__main__":
    test_player_wins()
    test_enemy_wins()
    test_turn_order_player_first()
    test_turn_order_enemy_first()
    test_caster_enemy()
    test_log()

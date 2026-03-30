from characters.factory import WarriorFactory
from items.factory import create_item
from items.equipment import Equipment


def test_equipment_affects_combat():
    print("\n==== Test: Equipment affects combat stats ====")
    w = WarriorFactory.create(name="Guts", level=1)

    print(f"Base stats: {w.attack}  defense: {w.defense}")
    print(f"Effective stats (no gear): {w.effective_stats()}")

    w.equipment = Equipment(
        weapon=create_item("iron_sword"),
        clothes=create_item("steel_armor"),
        armament=create_item("dark_charm"),
    )

    eff = w.effective_stats()
    print(f"Effective stats (with gear): attack={eff['attack']} defense={eff['defense']}")
    assert eff["attack"] == w.attack + 3
    assert eff["defense"] == w.defense + 4
    print("PASSED")

def test_equipment_affects_damage():
    print("\n==== Test: Equipment affects actual damage dealt ====")
    from characters.factory import WarriorFactory
    from Enemies.enemy_factory import spawn_enemy
    import random
    random.seed(42)

    w_no_gear = WarriorFactory.create(name="Guts")
    w_with_gear = WarriorFactory.create(name="Guts2")
    w_with_gear.equipment = Equipment(weapon=create_item("iron_sword"))

    g1 = spawn_enemy("goblin")
    g2 = spawn_enemy("goblin")

    out1 = w_no_gear.attack_target(g1)
    out2 = w_with_gear.attack_target(g2)

    print(f"No gear damage: {out1['damage_taken']} ")
    print(f"With sword damage: {out2['damage_taken']} ")
    assert out2['damage_taken'] >= out1['damage_taken']
    print("PASSED")

if __name__ == "__main__":

    test_equipment_affects_combat()
    test_equipment_affects_damage()

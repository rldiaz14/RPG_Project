from tools.test_utils import (
    make_warrior,make_enemy,
    make_warrior_gear,
    assert_eq, assert_gte, run_test
)
from items.factory import create_item
from items.equipment import Equipment


def test_equipment_stats():
    w = make_warrior()

    # no gear
    base = w.effective_stats()
    assert_eq("base attack", base["attack"], w.attack)
    assert_eq("base defense", base["defense"], w.defense)

    # equip gear
    w.equipment = make_warrior_gear()
    eff = w.effective_stats()

    assert_eq("attack with sword", eff["attack"], w.attack + 3)
    assert_eq("defense with armor", eff["defense"], w.defense + 4)
    print(f"    Base: attack={w.attack} defense={w.defense}")
    print(f"    Boosted: attack={eff['attack']} defense={eff['defense']}")


def test_equipment_affect_damage():
    w_no_gear = make_warrior(name="Guts")
    w_with_gear = make_warrior(name="Guts2")
    w_with_gear.equipment = Equipment(weapon=create_item("iron_sword"))

    g1 = make_enemy("goblin")
    g2 = make_enemy("goblin")

    out1 = w_no_gear.attack_target(g1)
    out2 = w_with_gear.attack_target(g2)

    print(f" No gear damage: {out1['damage_taken']}")
    print(f" With gear damage: {out2['damage_taken']}")
    assert_gte("sword deal more or equal damage", out2["damage_taken"], out1["damage_taken"])

def test_no_equipment_return_base_stats():
    w = make_warrior()
    eff = w.effective_stats()
    assert_eq("hp unchanged", eff["hp"], w.hp)
    assert_gte("speed unchanged", eff["speed"], w.speed)


if __name__ == "__main__":
    run_test(
        test_equipment_stats,
        test_equipment_affect_damage,
        test_no_equipment_return_base_stats,
    )
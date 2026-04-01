from tools.test_utils import (
    make_warrior, make_mage, make_rogue, make_enemy,
    assert_eq, assert_true, assert_in, run_test
)
from Enemies.enemy_factory import ENEMIES
from magics.spells import get_spell
from magics.resolver import cast_spell


def test_spawn_basic():
    for key in ENEMIES:
        e = make_enemy(key)
        snap = e.snapshot()
        assert_eq(f"{key} hp initialized", e.hp, e.max_hp)
        print(f"  {snap}")

def test_spawn_override():
    g = make_enemy("goblin", name="Big Goblin", attack=15, xp_reward=20)
    assert_eq("name override", g.name, "Big Goblin")
    assert_eq("attack override", g.attack, 15)
    assert_eq("xp override", g.xp_reward, 20)

def test_invalid_enemy():
    try:
        make_enemy("dragon")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"  Correctly raised: {e}")

def test_invalid_behavior():
    try:
        make_enemy("goblin", behavior="coward")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"  Correctly raised: {e}")

def test_hp_initialized():
    e = make_enemy("troll")
    assert_eq("troll hp == max_hp", e.hp, e.max_hp)

def test_physical_combat():
    w = make_warrior()
    g = make_enemy("goblin")
    out1 = w.attack_target(g)
    assert_in("damage_taken in result", "damage_taken", out1)
    print(f"  Warrior attacks Goblin: {out1}")
    if g.is_alive():
        out2 = g.attack_target(w)
        assert_in("damage_taken in result", "damage_taken", out2)
        print(f"  Goblin attacks Warrior: {out2}")

def test_rogue_vs_slime():
    r = make_rogue()
    s = make_enemy("slime")
    assert_true("rogue faster than slime", r.speed > s.speed)
    out = r.attack_target(s)
    assert_in("damage_taken in result", "damage_taken", out)
    print(f"  Rogue speed:{r.speed} vs Slime speed:{s.speed}")
    print(f"  Result: {out}")

def test_spell_vs_enemy():
    m = make_mage()
    t = make_enemy("troll")
    result = cast_spell(m, t, get_spell("fireball"))
    assert_eq("spell type", result["type"], "spell")
    assert_in("success in result", "success", result)
    print(f"  Cast result: {result}")

def test_spell_vs_weakness():
    m = make_mage()
    g = make_enemy("goblin", element_weakness={"fire": 1.5})
    result = cast_spell(m, g, get_spell("fireball"))
    assert_eq("spell type", result["type"], "spell")
    print(f"  Weakness result: {result}")

def test_spell_vs_resistance():
    m = make_mage()
    t = make_enemy("troll", element_resistance={"fire": 0.5})
    result = cast_spell(m, t, get_spell("fireball"))
    assert_eq("spell type", result["type"], "spell")
    print(f"  Resistance result: {result}")


if __name__ == "__main__":
    run_test(
        test_hp_initialized,
        test_spawn_basic,
        test_spawn_override,
        test_invalid_enemy,
        test_invalid_behavior,
        test_physical_combat,
        test_rogue_vs_slime,
        test_spell_vs_enemy,
        test_spell_vs_weakness,
        test_spell_vs_resistance,
    )
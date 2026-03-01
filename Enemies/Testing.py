from Enemies.enemy_factory import spawn_enemy, ENEMIES
import random


from characters.factory import WarriorFactory, MageFactory, RogueFactory
from magics.spells import get_spell
from magics.resolver import cast_spell
from magics.elements import Element

random.seed(42)

def test_spawn_basic():
    print("\n==== Test: Spawn all Enemies ====")
    for key in ENEMIES:
        e = spawn_enemy(key)
        print(e.snapshot())

def test_spawn_override():
    print("\n==== Test: Spawn with Override ====")
    g = spawn_enemy("goblin", name="Big Goblin", attack=15, xp_reward=20)
    print(g.snapshot())

def test_invalid_enemy():
    print("\n==== Test: Invalid enemy key ====")
    try:
        spawn_enemy("dragon")
    except ValueError as e:
        print(f"PASSED: {e}")

def test_invalid_behavior():
    print("\n==== Test: Invalid behavior ====")
    try:
        spawn_enemy("goblin", behavior="coward")
    except ValueError as e:
        print(f"PASSED: {e}")

def test_hp_initialized():
    print("\n==== Test: HP initialized correctly ====")
    e = spawn_enemy("troll")
    assert e.hp == e.max_hp
    print(f"PASSED: Troll hp={e.hp} max_hp={e.max_hp}")





def test_physical_combat():
    print("\n==== Test: Physical Combat (Warrior vs Goblin) ====")
    w = WarriorFactory.create(name="Guts")
    g = spawn_enemy("goblin")
    print(f"Before - Guts hp:{w.hp} | Goblin hp:{g.hp}")

    out1 = w.attack_target(g)
    print(f"Guts attack Goblin: {out1}")

    if g.is_alive():
        out2 = g.attack_target(w)
        print(f"Goblin attack Guts: {out2}")

    print(f"After - Guts hp:{w.hp} | Goblin hp:{g.hp}")


def test_rogue_vs_slime():
    print("\n=== Test: Rogue vs Slime (speed backstab check) ===")
    r = RogueFactory.create(name="Rogue")
    s = spawn_enemy("slime")

    print(f"Kira speed: {r.speed} | Slime speed: {s.speed}")
    print(f"Before - Kira hp:{r.hp} | Slime hp:{s.hp} ")

    out = r.attack_target(s)
    print(f"Rogue attack Slime: {out}")
    print(f"After - kira hp:{r.hp} | Slime hp:{s.hp} ")


def test_spell_vs_enemy():
    print("\n=== Test: Spell Combat (Mage vs Troll) ===")
    m = MageFactory.create(name="Vivi")
    t = spawn_enemy("troll")

    print(f"Before - Vivi hp:{m.hp} | Troll hp:{t.hp}")

    out1 = m.attack_target(t)
    print(f"Guts attack Goblin: {out1}")

    spell = get_spell("fireball")
    result = cast_spell(m, t, spell)
    print(f"Cast result: {result}")

    print(f"After - Vivi hp:{m.hp} | Troll hp:{t.hp}")

def test_spell_vs_weakness():
    print("\n=== Test: Element Weakness (Fireball vs fire-weak enemy) ===")
    m = MageFactory.create(name="Vivi")
    g = spawn_enemy("goblin", element_weakness={"fire": 1.5})

    print(f"Goblin weakness: {g.element_weakness}")
    print(f"Before - Goblin h:{g.hp}")

    result = cast_spell(m, g, get_spell("fireball"))
    print(f"Cast result: {result}")
    print(f"After - Goblin h:{g.hp}")

def test_spell_vs_resistance():
    print("\n=== Test: Element Resistance (Fireball vs fire-resistant enemy) ===")
    m = MageFactory.create(name="Vivi")
    t = spawn_enemy("troll", element_resistance={"fire": 0.5})

    print(f"Troll resistance: {t.element_resistance}")
    print(f"Before - Troll h:{t.hp}")

    result = cast_spell(m, t, get_spell("fireball"))
    print(f"Cast result: {result}")
    print(f"After - Troll h:{t.hp}")

if __name__ == "__main__":
    test_hp_initialized()
    test_spawn_override()
    test_spawn_basic()
    test_invalid_enemy()
    test_invalid_behavior()

    test_physical_combat()
    test_spell_vs_enemy()
    test_spell_vs_weakness()
    test_spell_vs_resistance()
    test_rogue_vs_slime()


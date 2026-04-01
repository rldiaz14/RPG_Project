# characters/Testing.py
from tools.test_utils import (
    make_warrior, make_mage, make_rogue,
    assert_eq, assert_true, assert_in, run_test
)


def test_snapshots():
    w = make_warrior(attack=20)
    m = make_mage()
    r = make_rogue()

    ws = w.snapshot()
    ms = m.snapshot()
    rs = r.snapshot()

    assert_eq("warrior class", ws["class"], "Warrior")
    assert_eq("mage class", ms["class"], "Mage")
    assert_eq("rogue class", rs["class"], "Rogue")
    assert_in("mana in mage snapshot", "mana", ms)
    assert_in("rage in warrior snapshot", "rage", ws)
    print(f"  Warrior: {ws}")
    print(f"  Mage: {ms}")
    print(f"  Rogue: {rs}")


def test_combat_between_characters():
    w = make_warrior(attack=20)
    m = make_mage()
    r = make_rogue()

    out1 = w.attack_target(m)
    assert_in("damage_taken in warrior result", "damage_taken", out1)
    print(f"  Warrior attacks Mage: {out1}")

    out2 = m.attack_target(r)
    assert_in("damage_taken in mage result", "damage_taken", out2)
    print(f"  Mage attacks Rogue: {out2}")

    out3 = r.attack_target(w)
    assert_in("damage_taken in rogue result", "damage_taken", out3)
    print(f"  Rogue attacks Warrior: {out3}")


def test_hp_changes_after_combat():
    w = make_warrior(attack=20)
    m = make_mage()

    hp_before = m.hp
    w.attack_target(m)
    print(f"  Mage hp before: {hp_before} after: {m.hp}")
    assert_true("mage took damage or dodged", m.hp <= hp_before)


if __name__ == "__main__":
    run_test(
        test_snapshots,
        test_combat_between_characters,
        test_hp_changes_after_combat,
    )
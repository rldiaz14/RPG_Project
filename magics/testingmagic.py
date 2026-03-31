from tools.test_utils import (
    make_mage, make_rogue, make_enemy,
    assert_eq, assert_true, assert_false, run_test
)
from magics.spells import get_spell, Spell
from magics.resolver import cast_spell
from magics.elements import Element


def test_spell_hit():
    m = make_mage()
    r = make_rogue()
    spell = get_spell("fireball")
    mana_before = m.mana
    result = cast_spell(m, r, spell)
    assert_eq("spell type", result["type"], "spell")
    assert_true("mana deducted", m.mana < mana_before)
    print(f"  Mana: {mana_before} → {m.mana}")
    print(f"  Result: {result}")

def test_spell_no_mana():
    m = make_mage(mana=5)
    r = make_rogue()
    result = cast_spell(m, r, get_spell("fireball"))
    assert_false("cast failed", result["success"])
    assert_eq("reason", result["reason"], "not_enough_mana")

def test_spell_miss():
    m = make_mage()
    r = make_rogue()
    weak_spell = Spell(
        key="weak", name="Weak Shot",
        element=Element.FIRE,
        cost_mana=5, power=5, accuracy=0.01
    )
    hp_before = r.hp
    result = cast_spell(m, r, weak_spell)
    assert_false("spell missed", result["success"])
    assert_eq("hp unchanged", r.hp, hp_before)
    print(f"  Result: {result}")


if __name__ == "__main__":
    run_test(
        test_spell_hit,
        test_spell_no_mana,
        test_spell_miss,
    )
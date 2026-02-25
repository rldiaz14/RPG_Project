from characters.factory import MageFactory, RogueFactory
from magics.spells import get_spell, Spell
from magics.resolver import cast_spell

def test_spell_hit():
    print("\n=== Test: Normal cast ====")
    m = MageFactory.create(name="Vivi")
    r = RogueFactory.create(name="Kira")

    spell = get_spell("fireball")
    print(f"Spell: {spell.name} | cost: {spell.cost_mana} | power: {spell.power} | accuracy: {spell.accuracy}")
    print(f"Vivi mana before: {m.mana}")


    result = cast_spell(m, r,spell)
    print(f"Result: {result}")
    print(f"Vivi mana after: {m.mana}")
    print(f"Kira hp after: {r.hp}")


def test_spell_no_mana():
    print("\n=== Test: Not enough mana ====")
    m = MageFactory.create(name="Vivi", mana=5) # not enough for fireball (cost 10)
    r = RogueFactory.create(name="Kira")

    result = cast_spell(m, r, get_spell("fireball"))
    print(f"Result: {result}")
    assert result["success"] == False
    assert result["reason"] == "not_enough_mana"
    print("PASSED")

def test_spell_miss():
    print("\n=== Test: Force miss ===")
    import random
    random.seed(99)
    m = MageFactory.create(name="Vivi")
    r = RogueFactory.create(name="Kira")


    #use a low accuracy spell to guarantee miss
    from magics.spells import SPELLS
    from magics.elements import Element

    weak_spell = Spell(key="weak", name="Weak Shot", element=Element.FIRE,
                        cost_mana=5, power=5, accuracy=0.01)

    result = cast_spell(m, r, weak_spell)
    print(f"Result: {result}")
    print(f"Kira hp (should be unchanged): {r.hp}")

if __name__ == "__main__":
    test_spell_hit()
    test_spell_no_mana()
    test_spell_miss()
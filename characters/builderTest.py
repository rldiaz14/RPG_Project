# characters/test_builder.py
from tools.test_utils import assert_eq, assert_in, assert_true, run_test
from characters.builder import CharacterBuilder



def test_from_preset_warrior():
    w = CharacterBuilder.from_preset("warrior", "guts")
    assert_eq("name", w.name, "Guts")
    assert_eq("class", w.__class__.__name__, "Warrior")
    assert_eq("max_hp", w.max_hp, 140)
    assert_eq("attack", w.attack, 14)
    print(f"  Snapshot: {w.snapshot()}")


def test_from_preset_mage():
    m = CharacterBuilder.from_preset("mage", "vivi")
    assert_eq("name", m.name, "Vivi")
    assert_eq("class", m.__class__.__name__, "Mage")
    assert_eq("mana", m.mana, 60)
    assert_eq("spell_power", m.spell_power, 12)
    print(f"  Snapshot: {m.snapshot()}")


def test_from_preset_rogue():
    r = CharacterBuilder.from_preset("rogue", "kira")
    assert_eq("name", r.name, "Kira")
    assert_eq("class", r.__class__.__name__, "Rogue")
    assert_eq("speed", r.speed, 9)
    print(f"  Snapshot: {r.snapshot()}")


def test_from_defaults():
    w = CharacterBuilder.from_default("warrior", "Custom", attack=20)
    assert_eq("name", w.name, "Custom")
    assert_eq("attack override", w.attack, 20)
    assert_eq("default max_hp", w.max_hp, 140)
    print(f"  Snapshot: {w.snapshot()}")


def test_equipment_loaded():
    w = CharacterBuilder.from_preset("warrior", "guts")
    eff = w.effective_stats()
    assert_eq("attack with sword", eff["attack"], w.attack + 3)
    assert_eq("defense with armor", eff["defense"], w.defense + 4)
    print(f"  Equipment: {w.equipment.summary()}")


def test_from_dict():
    data = {
        "name": "Test Warrior",
        "class_type": "warrior",
        "max_hp": 100,
        "attack": 10,
        "defense": 5,
        "speed": 5,
    }
    w = CharacterBuilder.from_dict(data)
    assert_eq("name", w.name, "Test Warrior")
    assert_eq("class", w.__class__.__name__, "Warrior")


def test_invalid_preset():
    try:
        CharacterBuilder.from_preset("warrior", "unknown")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError as e:
        print(f"  Correctly raised: {e}")


if __name__ == "__main__":
    run_test(
        test_from_preset_warrior,
        test_from_preset_mage,
        test_from_preset_rogue,
        test_from_defaults,
        test_equipment_loaded,
        test_from_dict,
        test_invalid_preset,
    )
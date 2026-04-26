from __future__ import annotations
import random
from typing import Callable

from characters.builder import CharacterBuilder
from Enemies.enemy_factory import spawn_enemy
from items.factory import create_item
from items.equipment import Equipment




# ---------- Character builders -------------
def make_warrior(name: str = "Guts", level: int = 1, **overrides):
    return CharacterBuilder.from_default("warrior", name, level=level, **overrides)

def make_mage(name: str = "Vivi", level: int = 1, **overrides):
    return CharacterBuilder.from_default("mage", name, level=level, **overrides)

def make_rogue(name: str = "Kira", level: int = 1, **overrides):
    return CharacterBuilder.from_default("rogue", name, level=level, **overrides)


# -------------- Enemy Builders  -------------------
def make_enemy(key: str = "goblin", **overrides):
    return spawn_enemy(key, **overrides)

# -------------- Equipment Builders  -------------------
def make_warrior_gear() -> Equipment:
    return Equipment(
        weapon=create_item("iron_sword"),
        clothes=create_item("steel_armor"),
        armament=create_item("dark_charm"),
    )

def make_mage_gear() -> Equipment:
    return Equipment(
        weapon=create_item("fire_staff"),
        clothes=create_item("ice_robes"),
    )

def make_rogue_gear() -> Equipment:
    return Equipment(
        weapon=create_item("poison_dagger"),
    )


# ---------------- Assertion helper -----------------------
def assert_eq(label: str, actual, expected) -> None:
    assert actual == expected, f"Failed {label} - Expected: {expected} got {actual}"
    print(f"    PASSED {label} : {actual}")


def assert_gt(label: str, actual, expected) -> None:
    assert actual > expected, f"Failed {label} - Expected > {expected} got {actual}"
    print(f"    PASSED {label} : {actual} > {expected}")


def assert_gte(label: str, actual, expected) -> None:
    assert actual >= expected, f"Failed {label} - Expected >= {expected} got {actual}"
    print(f"    PASSED {label} : {actual} >= {expected}")

def assert_lt(label: str, actual, expected) -> None:
    assert actual < expected, f"Failed {label} - Expected < {expected} got {actual}"
    print(f"    PASSED {label} : {actual} < {expected}")

def assert_in(label: str, key, container) -> None:
    assert key in container, f"Failed {label} - '{key}' not in {container}"
    print(f"    PASSED {label} : {key} found")

def assert_true(label: str, value) -> None:
    assert value, f"Failed {label} - expected True got {value}"
    print(f"    PASSED {label} : {value}")

def assert_false(label: str, value) -> None:
    assert not value, f"Failed {label} - expected False got {value}"
    print(f"    PASSED {label} : {value}")

def assert_none(label: str, value) -> None:
    assert value is None, f"Failed {label} - expected None got {value}"
    print(f"    PASSED {label} : {value}")


# --------- Test runner ---------

def run_test(*test_funcs: Callable, seed: int = 42) -> None:
    """
    Runs a list of test functions with a fixed seed
    Report pass/fail for each.
    :param test_funcs:
    :param seed:
    :return:
    """

    random.seed(seed)
    passed = 0
    fails = 0
    print("\n" + "="*50)

    for fn in test_funcs:
        print(f"\n ==== {fn.__name__} ==== ")
        try:
            fn()
            passed += 1
        except AssertionError as e:
            print(f" FAILED: {e}")
            fails += 1
        except Exception as e:
            print(f" Error: {type(e).__name__}: {e}")
            fails += 1

    print("\n" + "="*50)
    print(f"Results: {passed} passed, {fails} failed out of {passed+fails} tests")
    print("="*50)

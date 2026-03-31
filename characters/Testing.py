from characters.factory import WarriorFactory, MageFactory, RogueFactory



def main():
    """
      w = Warrior(name="Guts", max_hp=140, attack=14, defense=8, speed=5)
    m = Mage(name="Vivi", max_hp=90, attack=8, defense=3, speed=6, mana=60, spell_power=12)
    r = Rogue(name="Kira", max_hp=100, attack=11, defense=4, speed=9)
    :return:
    """
    w = WarriorFactory.create(name="Guts", attack=20)
    m = MageFactory.create(name="Vivi")
    r = RogueFactory.create(name="Kira")

    print(w.snapshot())
    print(m.snapshot())
    print(r.snapshot())

    print("\nWarrior attack Mage:")
    print(w.attack_target(m))
    print("Mage attack Rogue:")
    print(m.attack_target(r))
    print("Rogue attack Warrior:")
    print(r.attack_target(w))

    print("\nAfter:")
    print(w.snapshot())
    print(m.snapshot())
    print(r.snapshot())


if __name__ == "__main__":
    main()
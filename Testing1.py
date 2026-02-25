from characters.factory import WarriorFactory, MageFactory
from items.factory import create_item
from items.equipment import Equipment


def main():
    # create characters
    w = WarriorFactory.create_character(name="Guts")
    m = MageFactory.create_character(name="Vivi")

    #Build loadouts
    w_gear = Equipment(
        weapon=create_item("iron_sword"),
        clothes=create_item("steel_armor"),
        armament=create_item("dark_charm")
    )

    m_gear = Equipment(
        weapon=create_item("fire_staff"),
        clothes=create_item("ice_robes"),
    )


    print("Warrior load out:", w_gear.summary())
    print("Mage load out:", m_gear.summary())

    print("\nWarrior boosted stats:")
    print(w_gear.apply_all(w.snapshot()))

    print("\nMage boosted stats:")
    print(m_gear.apply_all(m.snapshot()))

if __name__ == "__main__":
    main()
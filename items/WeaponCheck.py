from items.factory import create_item, available_items


print(available_items())

sword = create_item("iron_sword")
staff = create_item("Fire Staff")
charm = create_item("dark_charm")

print(sword)
print(staff)
print(charm)

# test apply() on a character snapshot
stats = {"attack": 14, "defense": 8, "speed": 5}
print(sword.apply(stats))
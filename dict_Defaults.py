from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken:{chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans:{beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

Z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {Z_quantity}")
print()
print("`pantry` now conatins...")

for key, value in sorted(pantry.items()):
    print(key, value)
scents = ["lavender", "rose", "jasmine", "sandalwood", "vanilla"]
print("List:", scents)

scents_tuple = tuple(scents)
print("Tuple:", scents_tuple)

scent_prices = {
    "lavender": 5,
    "rose": 7,
    "jasmine": 6,
    "sandalwood": 8,
    "vanilla": 4
}
print("Dictionary:", scent_prices)

scent_set = set(scent_prices.keys())
seasonal_scents = {"pine", "cinnamon", "jasmine"}
print("Set:", scent_set)
print("Union:", scent_set | seasonal_scents)

print("\nMutability:")
print("List = mutable (can change)")
print("Tuple = immutable (cannot change)")
print("Dictionary = mutable (can change)")
print("Set = mutable (can change)")


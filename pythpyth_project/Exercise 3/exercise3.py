my_list = ["chocolate", "mint choc chip", "cookie dough", "pistachio", "honeycomb"]
print("Shopping list:", my_list)

my_list.append("caramel swirl")
print("After append (added 'caramel swirl'):", my_list)

my_list.pop(2)
print("After pop (removed flavour):", my_list)

flavour = "brownie"
print("\nOriginal string:", flavour)
print("Original id:", id(flavour))

flavour = flavour.replace("brownie", "brownie swirl")
print("\nAfter replace:", flavour)
print("New id:", id(flavour))

def add_flavour(flavour, basket=[]):
    basket.append(flavour)
    return basket

print("\nUsing mutable default argument:")
print(add_flavour("chocolate"))
print(add_flavour("mint"))
print(add_flavour("cookie dough"))

def add_flavour_safe(flavour, basket=None):
    if basket is None:
        basket = []
    basket.append(flavour)
    return basket

print("\nUsing safe default argument (None):")
print(add_flavour_safe("chocolate"))
print(add_flavour_safe("mint"))
print(add_flavour_safe("cookie dough"))
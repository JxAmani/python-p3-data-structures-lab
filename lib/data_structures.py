spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

# 1. Return a list of names
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. Return foods with heat_level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. Print all foods in the correct format
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# 4. Return the first food that matches a cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

# 5. Print only foods with heat_level > 5
def print_spiciest_foods(spicy_foods):
    for food in get_spiciest_foods(spicy_foods):
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

# 6. Calculate average heat level (integer)
def get_average_heat_level(spicy_foods):
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

# 7. Add a new spicy food to the list
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    print("Names:", get_names(spicy_foods))
    print("Spiciest foods:", get_spiciest_foods(spicy_foods))
    print("\nAll spicy foods:")
    print_spicy_foods(spicy_foods)
    print("\nFood by cuisine (American):", get_spicy_food_by_cuisine(spicy_foods, "American"))
    print("\nOnly spiciest foods:")
    print_spiciest_foods(spicy_foods)
    print("\nAverage heat level:", get_average_heat_level(spicy_foods))
    create_spicy_food(spicy_foods, {"name": "Griot", "cuisine": "Haitian", "heat_level": 10})
    print("\nAfter adding Griot:")
    print_spicy_foods(spicy_foods)

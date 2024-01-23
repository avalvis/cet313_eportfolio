import random
from itertools import combinations

# Sample shopping cart history data
shopping_history = [
    ["cookies", "noodles", "juice", "chocolate", "tea"],
    ["cookies", "juice", "chocolate"],
    ["cookies", "juice"],
    ["juice", "chocolate", "tea"],
    ["noodles", "chocolate"],
    ["chocolate", "tea"],
    ["noodles", "juice", "chocolate", "tea"],
    ["juice"],
    ["cookies", "noodles", "juice", "chocolate"],
    ["juice", "chocolate"]
]

# Task 1: Count occurrences of each item and their coexistence
item_occurrences = {item: sum(item in cart for cart in shopping_history) for item in set(item for cart in shopping_history for item in cart)}
pair_counts = {pair: sum(all(item in cart for item in pair) for cart in shopping_history) for pair in combinations(item_occurrences.keys(), 2)}

# Display item and pair counts
print("Item Occurrences:")
print(item_occurrences)

print("\nPair Coexistence Counts:")
print(pair_counts)

# Task 2: Generate random shopping history
available_items = list(item_occurrences.keys())
random_shopping_history = [random.sample(available_items, random.randint(1, 5)) for _ in range(10)]

print("\nRandomly Generated Shopping History:")
print(random_shopping_history)

# Task 3: Automate the item list
automated_item_list = list(item_occurrences.keys())

print("\nAutomated Item List:")
print(automated_item_list)

# Function to get count of a specific item
def get_item_count(item_name):
    return item_occurrences.get(item_name, 0)
cookies_count = get_item_count("cookies")
juice_count = get_item_count("juice")

print(f"\nNumber of 'cookies': {cookies_count}")
print(f"Number of 'juice': {juice_count}")
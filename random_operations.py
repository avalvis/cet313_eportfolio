# Python Basics: Random Dice Rolls and Data Structures

# Importing libraries
import matplotlib.pyplot as plt
import random

# Function to simulate die rolls and modify outcomes
def roll_die(times):
    count = 0
    results = [None] * times  # Initialize list with placeholder values
    
    while count < times:
        roll_result = random.randint(1, 6)  # Roll the die
        count += 1
        if roll_result % 2 != 0:  # Check for odd numbers
            results.append(6)
        else:
            results.append(roll_result)
        results = results[-times:]  # Keep only the recent 'times' results
    return results

# Rolling the die 1500 times
die_rolls = roll_die(1500)

# Creating a histogram of the results
fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(die_rolls, bins=[0, 1, 2, 3, 4, 5, 6])
plt.show()

# Demonstrating for-loops with a list
sample_list = [12, 22, 32, 42]
for number in sample_list:
    print("Hello number", number)

# Tuples and printing with variables
vector_space = [(2, 3), (4, 5), (6, 7), (8, 9)]
print("The number is", vector_space[3][1], "from the last tuple in vector_space")

# Using dictionaries
space_dictionary = {}
space_dictionary[0] = {"Space1": vector_space}
space_dictionary[1] = {"Space2": vector_space * 2}

print(space_dictionary)
print(space_dictionary[0])
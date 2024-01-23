from sympy import symbols

# Defining family members as symbolic variables
alice, brian, clara, daniel, ella, fred, georgia, harry, isabel, jack, linda, max = symbols('alice brian clara daniel ella fred georgia harry isabel jack linda max')

# Establishing parent-child relationships in a dictionary
family_tree = {
    alice: [brian, clara],
    brian: [daniel, ella],
    clara: [fred, georgia],
    daniel: [isabel, jack],
    ella: [linda, max],
    fred: [],
    georgia: [],
    isabel: [],
    jack:  [],
    linda:  [],
    max:  [],
}

# User input to find relatives in the family tree
query_person = input("Enter a family member's name to find their relatives: ").lower()

# Mapping the family tree to lowercase for easier comparison
family_tree_lower = {key.name.lower(): [child.name.lower() for child in value] for key, value in family_tree.items()}

# Checking if the person is in the family tree and displaying relatives
if query_person in family_tree_lower:
    relatives = family_tree_lower[query_person]
    print(f"Relatives of {query_person.capitalize()}:", relatives)
else:
    print(f"No information found for '{query_person}' in the family tree.")
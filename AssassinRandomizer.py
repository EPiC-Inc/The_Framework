import random

# Variables
names = None
targets = []

# Get players' names
try:
    names = raw_input("Enter a list of names, seperated by spaces:\n").split(" ")
except:
    names = input("Enter a list of names, seperated by spaces:\n").split(" ")

print("These players are playing Assassin:")
for name in names:
    print(name)

# Shuffle the names
print("\nRandomizing...")
random.shuffle(names)
print("Assigning targets...")

# Time to assign targets to the assasins
for target in names:
    # Check if this is the last name in the list
    # If it is, wrap around
    if names.index(target) == (len(names) - 1):
        i = 0
    # If not, proceed
    else:
        # Choose the next person in the names list to be targeted
        i = (names.index(target)) + 1
    targets.append(names[i])

print("\n\n")
print("Assasins:\tTargets:")

for i in range(0, len(names)):
    # Determine proper column spacing
    sep = ("-" * (16 - len(names[i])))
    # Print a list of all names and their targets
    print(names[i]+sep+targets[i])

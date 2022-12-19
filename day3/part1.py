# SpawnTerror 2022
# Python 3.11.1
# AOC Day 3

# Import string function and assign values 1-53 to a-Z
import string
letterValues = dict(zip(string.ascii_letters, range(1,53)))

# Create lists and variables
listPairs = []
sharedItems = []
sum = 0

with open('day3/input.txt', 'r') as f:
    for line in f:
        # Split each line in half and add both to list as separate item
        firstpart, secondpart = line[0: len(line)//2], line[len(line)//2: len(line)].rstrip()
        listPairs += firstpart, secondpart

# Iterate through pairs and find duplicates, add them to shared list
for k, v in zip(listPairs[0::2], listPairs[1::2]):
    sharedItems.extend([letter for letter in set(k) if letter in v])

# Iterate through shared letters and increase sum by the letter value
for i in sharedItems:
    sum += letterValues[i]

print(f'Sum of properties is ', sum)
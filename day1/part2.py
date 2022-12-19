# SpawnTerror 2022
# Python 3.11.1
# AOC Day 1

# Parse input data into a list, strip line breaks
with open('day1/input.txt', 'r') as f:
    entries = []
    for line in f:
        entries.append(line.rstrip())

# Count elves by checking for line break
elves = entries.count('') + 1
print(f'Elves = ', elves)

# Create a list with total calories for each elf
totals = []
count = 0

# Iterate through all entries, addidng them up until a line break
for i in entries:
    if i != '':
        count = count + int(i)
    else:
        totals.append(count)
        count = 0

# Sort the totals and calculate sum of the last 3 items
sort = sorted(totals)
print(f'Top 3 Elves are carrying ', sum(sort[-3:]))
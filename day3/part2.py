# SpawnTerror 2022
# Python 3.11.1
# AOC Day 3

# Import string function and assign values 1-53 to a-Z
import string
letterValues = dict(zip(string.ascii_letters, range(1,53)))

# Create lists and variables
lines = []
shared = []
sum = 0

with open('day3/input.txt', 'r') as f:
    
    for line in f:
        lines.append(line.rstrip())

# Pop 3 lines at a time from the list and add to Shared list
while len(lines) > 0:   
    line_1 = set(lines.pop())
    line_2 = set(lines.pop())
    line_3 = set(lines.pop())
    shared += ((line_1.intersection(line_2)).intersection(line_3))

# Iterate through shared letters and increase sum by the letter value
for i in shared:
    sum += letterValues[i]

print(f'Sum of the priorities of item types is', sum)
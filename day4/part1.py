# SpawnTerror 2022
# Python 3.11.1
# AOC Day 4

data = []
sum = 0

# Open input file and strip new line character
with open('day4/input.txt', 'r') as f:
    for line in f:
        data.append(line.rstrip())

# Pop a single line, split into individual numbers
while len(data) >0:
    line = data.pop()
    line = line.split(',')

    part1 = line[0].split('-')
    part2 = line[1].split('-')

    # Generate two sets from the numbers
    elfOne = set(range(int(part1[0]), int(part1[1])+1))    
    elfTwo = set(range(int(part2[0]), int(part2[1])+1))

    # Check if any of the sets contains in each other fully
    if elfOne.intersection(elfTwo) == elfTwo or elfTwo.intersection(elfOne) == elfOne:
        sum += 1

print('Assignment pairs that fully contain each other = ', sum)
# SpawnTerror 2022
# Python 3.11.1
# AOC Day 10 Part 1

rewritedCode = [0,0]
cycleNumber = []
counter = 1

sumSignals = 0
lookUpLocations = [20,60,100,140,180,220]

with open('day10/input.txt', 'r') as f:
    for line in f.read().split('\n'):

        match line[0:4]:
            case 'noop':
                rewritedCode.append(0)
            case 'addx':
                rewritedCode.append(0)
                rewritedCode.append(int(line[5:]))
   
for l in rewritedCode:
    counter += l
    cycleNumber.append(counter)

for location in lookUpLocations:
    print(f'Cycle = ', location,'Register =', cycleNumber[location])
    sumSignals += location * cycleNumber[location]
print(f'Total signal strengths = ', sumSignals)


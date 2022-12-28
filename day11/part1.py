# SpawnTerror 2022
# Python 3.11.1
# AOC Day 11 Part 1
import re
mDict = {}
with open('day11/test.txt', 'r') as f:
    for line in f.read().split('\n'):
        if 'Monkey' in line:  
            monkeyNunber = line[7]
            mDict[monkeyNunber] = {}
        if 'Starting' in line:
            monkeyItems = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            mDict[monkeyNunber]['Items'] = monkeyItems
        if 'Operation' in line:
            stressMonkey = line.partition('old ')[2]
            print(stressMonkey)
            mDict[monkeyNunber]['Stress'] = stressMonkey
        if 'Test' in line:
            divideMonkey = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            mDict[monkeyNunber]['Divide'] = divideMonkey 
        if 'true' in line:
            throwMonkey = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            mDict[monkeyNunber]['True'] = throwMonkey
        if 'false' in line:
            throwMonkey = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            mDict[monkeyNunber]['False'] = throwMonkey

for x in mDict:
    print(f'Monkey {x} = ', mDict[x])
    
print(int(x) for x in mDict['2']['Divide'][0])



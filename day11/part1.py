# SpawnTerror 2022
# Python 3.11.1
# AOC Day 11 Part 1
import re


def processMonkeys():
    mDict = {}
    with open('day11/input.txt', 'r') as f:
        for line in f.read().split('\n'):
            if 'Monkey' in line:  
                monkeyNunber = int(line[7])
                mDict[monkeyNunber] = {}
            elif 'Starting' in line:
                monkeyItems = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
                mDict[monkeyNunber]['Items'] = monkeyItems
            elif 'Operation' in line:
                stressMonkey = line.partition('old ')[2]
                mDict[monkeyNunber]['Stress'] = stressMonkey
            elif 'Test' in line:
                divideMonkey = re.findall(r'-?\d+\.?\d*', line)
                mDict[monkeyNunber]['Divide'] = int(divideMonkey[0]) 
            elif 'true' in line:
                throwMonkey = re.findall(r'-?\d+\.?\d*', line)
                mDict[monkeyNunber]['True'] = int(throwMonkey[0])
            elif 'false' in line:
                throwMonkey = re.findall(r'-?\d+\.?\d*', line)
                mDict[monkeyNunber]['False'] = int(throwMonkey[0])
    return mDict

def calculateStress(itemValue, monkey):
    stressValue = monkeyDict[monkey]['Stress']
    match stressValue[0]:
        case '*':
            print('Multiplication')
            if stressValue[2:] == 'old':
                itemValue = itemValue * itemValue
            else:
                itemValue = itemValue * int(stressValue[2:])
        case '+':
            itemValue = itemValue + int(stressValue[2:])
    return itemValue

# Parse input file
monkeyDict = processMonkeys()

# List all the data
for x in monkeyDict:
    print(f'Monkey {x} = ', monkeyDict[x])

# Test calculations
print(f'New value = ', calculateStress(79, 1))

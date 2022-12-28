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

''' Example output
Monkey 0 =  {'Items': [93, 98], 'Stress': '* 17', 'Divide': 19, 'True': 5, 'False': 3}
Monkey 1 =  {'Items': [95, 72, 98, 82, 86], 'Stress': '+ 5', 'Divide': 13, 'True': 7, 'False': 6}
Monkey 2 =  {'Items': [85, 62, 82, 86, 70, 65, 83, 76], 'Stress': '+ 8', 'Divide': 5, 'True': 3, 'False': 0}        
Monkey 3 =  {'Items': [86, 70, 71, 56], 'Stress': '+ 1', 'Divide': 7, 'True': 4, 'False': 5}
Monkey 4 =  {'Items': [77, 71, 86, 52, 81, 67], 'Stress': '+ 4', 'Divide': 17, 'True': 1, 'False': 6}
Monkey 5 =  {'Items': [89, 87, 60, 78, 54, 77, 98], 'Stress': '* 7', 'Divide': 2, 'True': 1, 'False': 4}
Monkey 6 =  {'Items': [69, 65, 63], 'Stress': '+ 6', 'Divide': 3, 'True': 7, 'False': 2}
Monkey 7 =  {'Items': [89], 'Stress': '* old', 'Divide': 11, 'True': 0, 'False': 2}
'''
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

def printMonkeys():
    for x in monkeyDict:
        print(f'Monkey {x} = ', monkeyDict[x])

def calculateWorryLevel(monkey, item):
    getFormula = monkeyDict[monkey]['Stress']
    operationSign, number = getFormula[0], getFormula[2:]
    
    if number == "old": number = item
    match operationSign:
        case '*':
            item = item * int(number)
        case '+':
            item = item + int(number)
    return item

def checkIfDivisible(monkey, item):
    checkDivisionNumber = int(monkeyDict[monkey]['Divide'])
    #print(f'Divide by {checkDivisionNumber}')
    return (True if item % checkDivisionNumber == 0 else False)

def throwItem(monkey, item, newItemToThrow, divisible):
    trueMonkey = int(monkeyDict[monkey]['True'])
    falseMonkey = int(monkeyDict[monkey]['False'])
    monkeyDict[monkey]['Items'].remove(item)
    if divisible:
        monkeyDict[trueMonkey]['Items'].append(newItemToThrow)
        #print(f'Throw {newItemToThrow} to {trueMonkey}')
        #print(f'Appending', monkeyDict[trueMonkey]['Items'])
        #print(f'---> This monkey now has <----')
        #print(monkeyDict[trueMonkey])
        x = trueMonkey
        #print(x)
    else:
        monkeyDict[falseMonkey]['Items'].append(newItemToThrow)
        #print(f'Throw {newItemToThrow} to {falseMonkey}')
        x = falseMonkey
        #print(x)
    return x

def round(rounds):
    for _ in range(rounds):
    
        for monkey in monkeyDict:
            
            
            noOfItems = len(monkeyDict[monkey]['Items'])
            itemsToCheck = [int(item) for item in monkeyDict[monkey]['Items']]

            if noOfItems >0:

                for item in itemsToCheck:
                    
                    countItems[monkey] += 1

                    newWorryLevel = calculateWorryLevel(monkey, item)
                    newWorryLevelBy3 = int(newWorryLevel / 3)
                    
                    #print(f'--> Checking M{monkey} item {item}.')
                    #print(f'New worry level is {newWorryLevel}, %3 is {newWorryLevelBy3}.')
                    divisible = checkIfDivisible(monkey, newWorryLevelBy3)
                    #print(f'Divisable status =  ', divisible)
                    x = throwItem(monkey, item, newWorryLevelBy3, divisible)
                    #print(f'---> This monkey no {x} now has <----')
                    #print(monkeyDict[x])
            else:
                pass
                # inactivate monkey {monkey}
    return countItems

def getResults(inspectedPerMonkey):
    topOne, topTwo = inspectedPerMonkey[-2:]
    return topOne * topTwo

monkeyDict = processMonkeys()
countItems = [0 for monkey in monkeyDict]
totalItemsInspected = [0 for monkey in monkeyDict]

totalInspected = round(20)
totalInspected.sort()
monkeyBusiness = getResults(totalInspected)

print(monkeyBusiness)






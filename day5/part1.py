# SpawnTerror 2022
# Python 3.11.1
# AOC Day 5 Part 1

with open('day5/test.txt', 'r') as f:
    inputData = f.read().splitlines()

for lineNumber, stringData in enumerate(inputData):
    if stringData == '':
        separateLine = lineNumber
    
cratesData = inputData[:separateLine]
movesData = inputData[separateLine+1:]
columnsNumber = int(max(cratesData[-1]))
movementlist = []

cratesList = [[letter] for letter in cratesData[-2][1:4*columnsNumber:4]]

for string in cratesData[-3::-1]:
    for position, letter in enumerate(string[1:4*columnsNumber:4]):
        if letter.isalpha():
            cratesList[position].append(letter)

for movementInstruction in movesData:
    splitIntruction = movementInstruction.split(' ')
    movementlist.append([int(splitIntruction[1]),int(splitIntruction[3]),int(splitIntruction[5])])

print(cratesList)
print(movementlist)
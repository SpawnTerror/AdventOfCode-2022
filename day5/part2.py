# SpawnTerror 2022
# Python 3.11.1
# AOC Day 5 Part 2

# Open the file, read and split by lines
with open('day5/input.txt', 'r') as f:
    inputData = f.read().splitlines()

# Enumerate lines and each string
# Empty line means end of crates
for lineNumber, stringData in enumerate(inputData):
    if stringData == '':
        separateLine = lineNumber

# Divide crates and movement instructions
cratesData = inputData[:separateLine]
movementData = inputData[separateLine+1:]

# Count all the columns by finding the biggest integer in the last line
columnsNumber = int(max(cratesData[-1]))

# Define a list and answer string
movementlist = []
answer = ""

# Create a list, based on the last line in cratesData
cratesList = [[letter] for letter in cratesData[-2][1:4*columnsNumber:4]]

# Then enumerate position and letter, append to the above list
for string in cratesData[-3::-1]:
    for position, letter in enumerate(string[1:4*columnsNumber:4]):
        if letter.isalpha():
            cratesList[position].append(letter)

# Create movement list by taking position 1, 3 and 5 from each line
for movementInstruction in movementData:
    splitIntruction = movementInstruction.split(' ')
    movementlist.append([int(splitIntruction[1]),int(splitIntruction[3]),int(splitIntruction[5])])

# Move crates all at once, use pop and append
for movement in movementlist:
    for position in range(movement[0],0,-1):
        bufferCrate = cratesList[movement[1]-1].pop(-position)
        # Move all the crates at once (-position)
        # print(f'Buffer crate = ', bufferCrate)
        cratesList[movement[2]-1].append(bufferCrate)

# Get all the last letters in the list [-1]
for number in range(0, columnsNumber):
    answer = answer + cratesList[number][-1]
print(f'Crates on top, counting from the left column: ', answer)
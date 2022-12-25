# SpawnTerror 2022
# Python 3.11.1
# AOC Day 6 Part 1

# Working with 4 letter in a row
setSize = 4

# Grab each letter and put into a list
def getData(fileName: str) -> list:
    with open(fileName, 'r') as f:
        initialData = [x for x in f.readline()]
    return initialData

# Part 1
def processData(data: list):

    # Create dictionary to count occurences
    # Marker is already on 4 as first set is 4 long
    dictionaryFours = {}
    markerPosition = 4

    # Itterate through every letter 
    # (-3) to end on a full set of 4
    # Put 4 letters into a line
    for x in range(0, len(data)-3):
        dictionaryFours = {}
        line = data[x: x + setSize]

        # Count occurences of each letter
        # in the current dictionary of 4
        for letter in line:
            if letter in dictionaryFours:
                dictionaryFours[letter] += 1
            else:
                dictionaryFours[letter] =1

        # Check if all counts are equal to 1
        # If true, return the set and marker position
        if all(value == 1 for value in dictionaryFours.values()):
            return dictionaryFours, markerPosition
        else:
            markerPosition += 1

data = getData('day6/input.txt')
uniqueSet, markerPosition = processData(data)

print(f'Unique set found: ', uniqueSet, 'with a markerPosition at position: ', markerPosition)


    

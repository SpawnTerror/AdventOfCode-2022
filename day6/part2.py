# SpawnTerror 2022
# Python 3.11.1
# AOC Day 6 Part 2

# Working with 14 letters in a row

setSize = 14

# Grab each letter and put into a list

def getData(fileName: str) -> list:
    with open(fileName, 'r') as f:
        initialData = [x for x in f.readline()]
    return initialData

# Part 2

def processData(data: list):

    # Create dictionary to count occurences
    # Marker is already on 14 as first set is 14 long

    dictionarySet = {}
    markerPosition = 14

    # Itterate through every letter 
    # (-3) to end on a full set of 14
    # Put 14 letters into a line

    for x in range(0, len(data)-3):
        dictionarySet = {}
        line = data[x: x + setSize]

        # Count occurences of each letter
        # in the current dictionary of 14

        for letter in line:
            if letter in dictionarySet:
                dictionarySet[letter] += 1
            else:
                dictionarySet[letter] =1

        # As letters are added as keys
        # and duplicates are merged
        # Stop when we count to 14
        # which means all letters are unique
        
        if len(dictionarySet) == 14:
            return dictionarySet, markerPosition
        else:
            markerPosition += 1
        
data = getData('day6/input.txt')
uniqueSet, markerPosition = processData(data)

print(f'Unique set found: ', uniqueSet, 'with a marker at position: ', markerPosition)
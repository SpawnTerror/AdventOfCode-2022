# SpawnTerror 2022
# Python 3.11.1
# AOC Day 8 Part 2

# Create an array treeMatrix
with open('day8/input.txt', 'r') as f:
    treeMatrix = []    
    for line in f.read().split('\n'):      
        treeMatrix += [[l for l in line]]

# Count rows and columns, create list for all the scores
rowNumber = len(treeMatrix[0])
colNumber = len(treeMatrix)
allScores = []

# Iterate through every tree in the treeMatrix
# Not including edges as x*0 = 0
for positionX in range(1, colNumber-1):
    for positionY in range(1, rowNumber-1):
        
        treeHeight = treeMatrix[positionX][positionY]

        # Generate lists for looking in 4 directions
        # Reverse left and top lists
        
        # Right, slice
        checkRight = treeMatrix[positionX][positionY+1:]
        
        # Left, slice
        checkLeft = treeMatrix[positionX][:positionY]
        checkLeft.reverse()

        # Bottom, iterate through treeMatrix's lists
        checkBottom = []
        for c in range(positionX+1, colNumber):
            checkBottom.append(treeMatrix[c][positionY])
        
        # Top, iterate through treeMatrix's lists
        checkTop = []
        for c in range(0, positionX):
            checkTop.append(treeMatrix[c][positionY])
        checkTop.reverse()
       
        # Count trees in all directions
        # Include equal or higher tree then break
        countRight, countLeft, countTop, countBottom = 0, 0, 0, 0

        # Check right
        for tree in checkRight:
            if tree < treeHeight:
                countRight += 1
            elif tree >= treeHeight:
                countRight += 1
                break
        
        # Check left
        for tree in checkLeft:
            if tree < treeHeight:
                countLeft += 1
            elif tree >= treeHeight:
                countLeft += 1
                break
        
        # Check top
        for tree in checkTop:
            if tree < treeHeight:
                countTop += 1
            elif tree >= treeHeight:
                countTop += 1
                break
        
        # Check bottom
        for tree in checkBottom:
            if tree < treeHeight:
                countBottom += 1
            elif tree >= treeHeight:
                countBottom += 1
                break
       
        # Multiply the scores and add to allScores lis
        treeScore = countBottom * countTop * countLeft * countRight
        allScores.append(treeScore)

# Print the best score using max function
print(f'Highest scenic score is {max(allScores)}')
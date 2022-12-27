# SpawnTerror 2022
# Python 3.11.1
# AOC Day 8 Part 1

# Create an array treeMatrix
with open('day8/input.txt', 'r') as f:
    treeMatrix = []    
    for line in f.read().split('\n'):      
        treeMatrix += [[l for l in line]]

# Count rows and columns
# Count trees on the edges
rowNumber = len(treeMatrix[0])
colNumber = len(treeMatrix)
countEdges = (2*rowNumber + 2*colNumber) - 4

# Variable for visible trees in total
visibleTreesEdges = 0 + countEdges
visibleTreesInside = 0

# Iterate through every tree in the treeMatrix
# Not including the edges
for positionX in range(1, colNumber-1):
    for positionY in range(1, rowNumber-1):
        
        treeHeight = treeMatrix[positionX][positionY]

        # Generate lists for looking in 4 directions
        
        # Right, slice
        checkRight = treeMatrix[positionX][positionY+1:]

        # Left, slice
        checkLeft = treeMatrix[positionX][:positionY]

        # Bottom, iterate through treeMatrix's lists
        checkBottom = []
        for c in range(positionX+1, colNumber):
            checkBottom.append(treeMatrix[c][positionY])

        # Top. iterate through treeMatrix's lists
        checkTop = []
        for c in range(0, positionX):
            checkTop.append(treeMatrix[c][positionY])
        
        # Create a dictionary with all directions' booleans
        # Check if each tree is visible from any direction
        # By comparing their heights
        visibilitytreeMatrix = {'Right': False, 'Left': False, "Top": False, "Bottom": False}
        
        # If tree from the list is higher than my tree
        if any(tree >= treeHeight for tree in checkRight):
            # Do nothing
            pass
        # If it is smaller
        else:
            # My tree is visible
            visibilitytreeMatrix['Right'] = True

        if any(tree >= treeHeight for tree in checkLeft):
            pass
        else:
            visibilitytreeMatrix['Left'] = True

        if any(tree >= treeHeight for tree in checkTop):
            pass
        else:
            visibilitytreeMatrix['Top'] = True

        if any(tree >= treeHeight for tree in checkBottom):
            pass
        else:
            visibilitytreeMatrix['Bottom'] = True

        # If the tree is visible from any direction
        # add it to the list of visible trees
        if any(value == True for value in visibilitytreeMatrix.values()):
            visibleTreesInside += 1
        
# Print results
print(f'Visible trees are {visibleTreesEdges} on the edges and {visibleTreesInside} inside.')
print(f'Total visible {visibleTreesEdges+visibleTreesInside}.')

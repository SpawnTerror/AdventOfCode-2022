# SpawnTerror 2022
# Python 3.11.1
# AOC Day 9 Part 1

# Numpy to check the +- sign of the difference
# Between the coordinates of tail and head
import numpy as np

with open('day9/test.txt', 'r') as f:
    instructions = [line for line in f.read().split('\n')]

def processMovement(instructions):
    
    # Start at 0,0 coordinates for both
    headXY = (0, 0)
    tailXY = (0, 0)
    
    # Initiate a SET for tail positions
    # Add 0,0 as starting position
    tailPositions = set()
    tailPositions.add(tailXY)
    
    # Split instructions into direction and number of steps
    for line in  instructions:
        command, count = line.split(' ')
        
        # Do the command for so many steps
        for c in range(int(count)):

            # Match the command and increase axes X and Y
            match command[0]:
                case 'R': headXY = (headXY[0] + 1, headXY[1])
                case 'L': headXY = (headXY[0] - 1, headXY[1])
                case 'D': headXY = (headXY[0], headXY[1] - 1)
                case 'U': headXY = (headXY[0], headXY[1] + 1)

            # Get the difference between head and tail
            diffX = headXY[0] - tailXY[0]
            diffY = headXY[1] - tailXY[1]
          
            # Numpy's SIGN function checks for sign
            # Returns -1 | 0 | 1 for integers
            # Check if HEAD moved away more than 1 cell away
            if abs(diffX) > 1 or abs(diffY) > 1:
                
                # Add -1 or 0 or 1
                tailXY = (tailXY[0] + np.sign(diffX), tailXY[1] + np.sign(diffY))
                
                # Add to set of positions visited by the tail
                tailPositions.add(tailXY)
        
    return tailPositions

# Print results using len to count the items
results = processMovement(instructions)
print(f'Tail visited below locations',len(results),'times: \n', results)
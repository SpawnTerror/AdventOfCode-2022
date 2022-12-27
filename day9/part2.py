# SpawnTerror 2022
# Python 3.11.1
# AOC Day 9 Part 2

# Numpy to check the +- sign of the difference
# Between the coordinates of tail and head
import numpy as np

with open('day9/test.txt', 'r') as f:
    instructions = [line for line in f.read().split('\n')]

def processMovement(instructions):
    
    # Create a list with 10 knots starting at 0,0
    knots = []
    for _ in range(10):
        knots.append((0,0))

    # Initiate a set for tail positions
    # Set doesn't contain duplicates
    # Add 0,0 as starting position
    knotPositions = set()
    knotPositions.add(knots[-1])
    
    # Split instructions into direction and number of steps
    for line in  instructions:
        command, count = line.split(' ')
        
        # Do the command for so many steps
        for _ in range(int(count)):

            # Match the command and increase axes X and Y
            match command:
                case 'R': knots[0] = (knots[0][0] + 1, knots[0][1])
                case 'L': knots[0] = (knots[0][0] - 1, knots[0][1])
                case 'D': knots[0] = (knots[0][0], knots[0][1] - 1)
                case 'U': knots[0] = (knots[0][0], knots[0][1] + 1)

            # Get the difference between head and tail
            for c in range(9):
                diffX = knots[c][0] - knots[c+1][0]
                diffY = knots[c][1] - knots[c+1][0]
          
                # Numpy's SIGN function checks for sign
                # Returns -1 | 0 | 1 for integers
                # Check if HEAD moved away more than 1 cell away
                if abs(diffX) > 1 or abs(diffY) > 1:
                    
                    # Add -1 or 0 or 1
                    knots[c+1] = (knots[c+1][0] + np.sign(diffX), knots[c+1][1] + np.sign(diffY))
                    
                    # Add to set of positions visited by the tail
                knotPositions.add(knots[c-1])
        print(knotPositions)
    return knotPositions

# Print results using LEN to count the items
results = processMovement(instructions)
print(f'Tail visited locations',len(results),'times.')
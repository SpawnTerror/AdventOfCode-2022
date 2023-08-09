# SpawnTerror 2022
# Python 3.11.1
# AOC Day 12 Part 1
print('------------------------------------')
'''
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi



[['Sabqponm'], 
 ['abcryxxl'], 
 ['accszExk'], 
 ['acctuvwj'], 
 ['abdefghi']]
'''
with open("day12/test.txt") as f:
    grid = [list(row.strip()) for row in f.readlines()]
    totalLines = len(grid)
    lineLength = len(grid[0])

def getStartCoordinates(grid):

    totalLines = len(grid)
    startPositionX = 0
    startPositionY = 0

    for lineNumber in range(0, totalLines):
        for point in grid[lineNumber]:
            if point == "S":
                startX, startY = startPositionX, startPositionY
            if point == "E":
                goalX, goalY = startPositionX, startPositionY
            startPositionY += 1
        startPositionX += 1
        startPositionY = 0

    return startX, startY, goalX, goalY


def debug():
    print(f'Start coords = ', startX, '-', startY)
    print(f'Goal coords = ', goalX, goalY)
    print(f'Total lines = ', totalLines)
    print(f'Line length = ', lineLength)
    print(f'Starting value = ',grid[startX][startY])
    print(f'Ending value = ',grid[goalX][goalY])

def replaceWithNumbers(grid):
    for n in range(0, totalLines):
        for c in range(0, lineLength):
            match grid[n][c]:
                case 'S':
                    grid[n][c] = 0
                case 'E':
                    grid[n][c] = 27
                case other:
                    grid[n][c] = ord(grid[n][c]) - 96
    return grid

startX, startY, goalX, goalY = getStartCoordinates(grid)
grid = replaceWithNumbers(grid)
#print(debug())
for line in range(0,totalLines):
    print(grid[line])

value = 0
current = [grid[startX][startY]]

while True:
    if value == 0:
        break
    # check right
    if startX  lineLength:
        if current - grid[startX][startY+1] == -1:
            startX +=1
            value = grid[startX][startY+1]
        
        
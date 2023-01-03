# SpawnTerror 2022
# Python 3.11.1
# AOC Day 12 Part 1

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

print(grid)
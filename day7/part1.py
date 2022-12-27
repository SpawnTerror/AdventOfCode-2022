# SpawnTerror 2022
# Python 3.11.1
# AOC Day 7 Part 1

# Code review

inputs = []
sizes = {}
for i in open("day7/test.txt", "r").read().split("\n"):
    i = i.replace("$ ", "")    
    if i[0:2] != "ls" and i[0:3] != "dir":
        inputs.append(i)

stack = []
for i in range(len(inputs)):
    line = inputs[i]    
    if line[0:2] == "cd" and ".." in line:
        stack.pop()    
    elif line[0:2] == "cd":
        stack.append(i)        
        sizes[i] = 0    
    else:        
        size = int(line.split(" ")[0])        
        for s in stack:            
            sizes[s] += size

part1_answer = sum([sizes[i] for i in sizes if sizes[i] <= 100000])
print("Part 1 answer: ", part1_answer)

unused = 70000000 - sizes[0]
unused_needed = 30000000 - unused
potential_deletes = [sizes[i] for i in sizes if sizes[i] >= unused_needed]
part2_answer = min(potential_deletes)
print("Part 2 answer: ", part2_answer)

# For context, sizes is a dict that maps line indexes to values (both 
# ints).
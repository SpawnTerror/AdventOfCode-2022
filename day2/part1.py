# SpawnTerror 2022
# Python 3.11.1
# AOC Day 2

# 1 for Rock, 2 for Paper, and 3 for Scissors
pointsOption = {'X': 1, "Y": 2, "Z": 3}

# 0 if you lost, 3 if the round was a draw, and 6 if you won
pointsResult = {"lost": 0, "draw": 3, "win": 6}

# Possible outcomes for (A,X) is Rock (B,Y) is Paper (C,Z) is Scissors
Win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
Draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
Lost = {'A': 'Z', 'B': 'X', 'C': 'Y'}

totalPoints = 0

with open('day2/input.txt', 'r') as f:
    for line in f:
        k, v = line[0], line[2]
       
        # add points depending on the option selected
        totalPoints += pointsOption[v]

        # ccompare input data and add points depending on the outcome
        if (k, v) in Win.items():
            totalPoints += pointsResult['win']
        elif (k, v) in Draw.items():
            totalPoints += pointsResult['draw']
        elif (k, v) in Lost.items():
            totalPoints += pointsResult['lost']

    print(totalPoints)




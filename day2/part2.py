# SpawnTerror 2022
# Python 3.11.1
# AOC Day 2

# A = Rock, B = Paper, C = Scissors
# X = Lost, Y = Draw, Z = Win
totalPoints =0

# Must pick Rock if draw to Rock, lost to Paper, win to Scissors is required
chooseRock = {'A': 'Y', 'B': 'X', 'C': 'Z'}
choosePaper = {'B': 'Y', 'C': 'X', 'A': 'Z'}
chooseScissors = {'C': 'Y', 'A': 'X', 'B': 'Z'}
pointsOOutcome = {'X': 0, "Y": 3, "Z": 6}
pointsOption = {'rock': 1, 'paper': 2, 'scissors': 3}

with open('day2/input.txt', 'r') as f:
    for line in f:
        k, v = line[0], line[2]
        # A, Y
        # add points depending if win, draw or lost
        totalPoints += pointsOOutcome[v]

        # add points depending on what was required to play and the outcome required
        if (k, v) in chooseRock.items():
            totalPoints += pointsOption['rock']
        elif (k, v) in choosePaper.items():
            totalPoints += pointsOption['paper']
        elif (k, v) in chooseScissors.items():
            totalPoints += pointsOption['scissors']
            
    print(totalPoints)
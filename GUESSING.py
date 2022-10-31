import itertools
from random import randrange
players = [None] * int(input("How many players: "))
print("")
for i in range(0, len(players)):
    players[i] = input("Player {}'s name: ".format(i + 1))
teams = [[], []]
for i in range(0, len(players)):
    teams[i % len(teams)].append(players.pop(randrange(0, len(players))))
for i in range(0, len(teams)):
    print("\nTeam {} is {}".format(i + 1, teams[i]), end="")
print("\nThere are 5 rounds. The winning team will be the one with the lowest score!")

scores = [0, 0]
for round in range(0, 5):
    print("\nRound {}".format(round + 1))
    for team in range(0, len(teams)):
        print("\nTeam {}".format(team + 1))
        for player in range(0, len(teams[team])):
            rand = randrange(1, 100 + 1)
            guess = int(input("{}, guess the number (between 1 and 100): ".format(teams[team][player])))
            quality = abs(rand - guess)
            scores[team] += quality
            print("The number was {}. You were {} away. Your team's current score is {}.".format(rand, quality, scores[team]))

print("\nRESULTS\nTeam 1 has {} points.\nTeam 2 has {} points.".format(scores[0], scores[1]))

# This line is a comment
# It does nothing
# I'm just adding these to troll you
# Oh look I still only used 39 lines huh

if scores[0] < scores[1]:
    print("The winner is Team 1!")
elif scores[1] < scores[0]:
    print("The winner is Team 2!")
else:
    print("It's a tie!")
input("\nPress enter to exit")
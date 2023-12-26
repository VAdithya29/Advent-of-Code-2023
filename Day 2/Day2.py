puzzleInput = open('Day 2/testinput.txt')
totalRed = 12
totalGreen = 13
totalBlue = 14
gamePossible = True
acceptedGameSums = 0
gamePowerSums = 0

#Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue, 18 green; 6 blue, 19 red, 10 green; 12 red, 19 green, 11 blue
for game in puzzleInput:
    minRed = 0
    minBlue = 0
    minGreen = 0
    # 1
    gameId = int(game.split(" ")[1].split(":")[0])
    rounds = game.split(":")[1]
    # 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    for round in rounds:
        gamePossible = True
        round = rounds.split(";")
        # round is: 6 red, 1 blue, 3 green
        for colours in round:
            if gamePossible:
                colours = colours.replace(", ",",")
                colouredBalls = colours.split(",")
                #20 green
                # the number of balls is known in this block only.
                for balls in colouredBalls:
                    balls = balls.strip()
                    colour = balls[-1]
                    if colour == "d":
                        if int(balls.split(" ")[0]) > int(minRed):
                            minRed = balls.split(" ")[0]
                        if int(balls.split(" ")[0]) > int(totalRed):
                            gamePossible = False
                    elif colour == "e":
                        if int(balls.split(" ")[0]) > int(minBlue):
                            minBlue =int(balls.split(" ")[0])
                        if int(balls.split(" ")[0]) > int(totalBlue):
                            gamePossible = False
                    elif colour == "n":
                        if gameId == 3:
                            print(balls.split(" ")[0])
                        if int(balls.split(" ")[0]) > int(minGreen):
                            minGreen =int(balls.split(" ")[0])
                        if int(balls.split(" ")[0]) > int(totalGreen):
                            gamePossible = False
            if not gamePossible:
                break
    if gamePossible:
        acceptedGameSums+=gameId
    print(int(minRed))
    print(int(minBlue))
    print(int(minGreen))
    print(int(minRed)*int(minBlue)*int(minGreen))
    gamePowerSums = gamePowerSums + int(minRed)*int(minBlue)*int(minGreen)
print(acceptedGameSums)
print(gamePowerSums)
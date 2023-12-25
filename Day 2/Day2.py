puzzleInput = open('Day 2/input.txt')
totalRed = 12
totalGreen = 13
totalBlue = 14
gamePossible = True
acceptedGameSums = 0

#Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue, 18 green; 6 blue, 19 red, 10 green; 12 red, 19 green, 11 blue
for game in puzzleInput:
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
                for balls in colouredBalls:
                    balls = balls.strip()
                    colour = balls[-1]
                    if colour == "d" and int(balls.split(" ")[0]) > int(totalRed):
                        gamePossible = False
                        break
                    elif colour == "e" and int(balls.split(" ")[0]) > int(totalBlue):
                        gamePossible = False
                        break
                    elif colour == "n" and int(balls.split(" ")[0]) > int(totalGreen):
                        gamePossible = False
                        break
            if not gamePossible:
                break
    if gamePossible:
        # print("Possible", gameId)
        acceptedGameSums+=gameId
print(acceptedGameSums)
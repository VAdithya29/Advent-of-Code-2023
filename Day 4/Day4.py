scards = open("Day 4/input.txt",'r').read().split("\n")
cardPoints = 0
totalPoints = 0
#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#Card   2:  3 88 36 12  2  9 15 55 21 89 | 23 39 98 36  2 24  9  3 78 95 55 37 12 61 38 88 85 89 13 15 96 45 21 25 30

for card in scards:
    matches = 0
    numMatches = 0
    card = card.replace("  "," ")
    winningNumbers = card.split("|")[0].split(":")[1].strip().split(" ") # 41 48 83 86 17
    elfNumbers = card.split("|")[1].strip().split(" ") # 83 86  6 31 17  9 48 53
    for number in winningNumbers:
        if number in elfNumbers:
            if matches > 0:
                cardPoints*=2
                numMatches+=1
            else:
                cardPoints = 1
                matches = 1
                numMatches+=1
    print(numMatches)
    totalPoints+=cardPoints
    cardPoints = 0
print(totalPoints)
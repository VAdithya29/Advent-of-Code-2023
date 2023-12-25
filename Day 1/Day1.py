puzzleInput = data = open('Day 1/input.txt', 'r').read().split('\n')
sum = 0
numbers = ["one","two","three","four","five","six","seven","eight","nine"]
for line in puzzleInput:
    firstDigit = 0
    lastDigit = 0
    flag = 0
    for c in line:
        if c.isdigit() and flag == 0:
            firstDigit = c
            flag = 1
        elif c.isdigit() and flag == 1:
            lastDigit = c
    if firstDigit and lastDigit:
        sum = sum + (10*int(firstDigit)+int(lastDigit))
    elif firstDigit and not(lastDigit):
        sum = sum + (10*int(firstDigit)+int(firstDigit))

input = "sgnfscdnd52twozg"
print(sum)

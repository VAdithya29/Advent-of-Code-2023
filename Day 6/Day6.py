inp = open("Day 6/input.txt",'r').read().split("\n")
time = inp[0].split(":")[1].strip().split()
distance = inp[1].split(":")[1].strip().split()
# Time:      7  15   30
# Distance:  9  40  200
moe = 1
for index,raceTime in enumerate(time):
    raceFinish = 0
    for i in range(0,int(raceTime)):
        distTravelled = (int(raceTime)-i)*i
        if distTravelled>int(distance[index]):
            raceFinish+=1
    moe*=raceFinish
print(moe)
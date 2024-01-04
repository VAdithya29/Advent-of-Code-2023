inp = open("Day 5/input.txt",'r').read().split("\n")
maps = 
seeds = inp[0].split(":")[1].split(" ")
# seeds: 79 14 55 13
# seed -> soil -> fert -> water -> light -> temp -> hum -> location
for seed in seeds:


def convert(source, destination,l):
    drs = destination.split(" ")[0]
    srs = destination.split(" ")[1]
    srl = destination.split(" ")[2]
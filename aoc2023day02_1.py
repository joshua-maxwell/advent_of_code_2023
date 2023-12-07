# https://adventofcode.com/2023/day/2
# Determine which games would have been possible if the bag had been loaded with 
# only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

aoc_day2_input_1 = open('aoc2023day02input1.txt', 'r')

map = {}
map['red'] = 12
map['green'] = 13
map['blue'] = 14

totalGood = 0
lineNumber = 0
while True:
    lineNumber += 1
    line = aoc_day2_input_1.readline()
    if not line:
        break
    line = line.replace(",","")
    line = line.replace(";","")
    x = line.split()

    wasItGood = True
    i = 2
    while i < len(x):
        count = int(x[i][0:len(x[i])])
        color = x[i+1][0:len(x[i+1])]
        if (count > map.get(color)):
            wasItGood = False
            break
        i += 2
    if(wasItGood):
        totalGood+=lineNumber
print(totalGood)
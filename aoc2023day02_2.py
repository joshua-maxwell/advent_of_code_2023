# https://adventofcode.com/2023/day/2
# fewest number of cubes of each color
# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# What is the sum of the power of these sets?

aoc_day2_input_2 = open('aoc2023day02input2.txt', 'r')

powerSum = 0
while True:
    line = aoc_day2_input_2.readline()
    if not line:
        break
    line = line.replace(",","")
    line = line.replace(";","")
    x = line.split()
    rgb = [0, 0, 0]

    i = 2
    while i < len(x):
        count = int(x[i][0:len(x[i])])
        color = x[i+1][0:len(x[i+1])]
        if (color == "red"):
            rgb[0] = max(rgb[0],count)
        elif (color == "green"):
            rgb[1] = max(rgb[1],count)
        elif (color == "blue"):
            rgb[2] = max(rgb[2],count)
        i += 2
    powerSum += rgb[0] * rgb[1] * rgb[2]

print(powerSum)
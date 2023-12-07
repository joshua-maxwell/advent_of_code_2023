# https://adventofcode.com/2023/day/1
file1 = open('aoc2023day01input1.txt', 'r')
total = 0

while True:
    line = file1.readline()
    if not line:
        break
    
    for char in line:
        if char.isdigit():
            firstDigit = int(char)
            break

    for char in line[::-1]:
        if char.isdigit():
            lastDigit = int(char)
            break
    
    total =  total + (firstDigit * 10) + lastDigit

print(total) 
file1.close()

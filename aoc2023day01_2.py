# https://adventofcode.com/2023/day/1
dictionary = {}
dictionary['one'] = 1
dictionary['two'] = 2
dictionary['three'] = 3
dictionary['four'] = 4
dictionary['five'] = 5
dictionary['six'] = 6
dictionary['seven'] = 7
dictionary['eight'] = 8
dictionary['nine'] = 9
dictionary['zero'] = 0

file1 = open('aoc2023day01input2.txt', 'r')
total = 0

while True:
    line = file1.readline()
    if not line:
        break
    
    for char in line:
        if char.isdigit():
            firstDigit = char
            firstDigitIndex = line.find(firstDigit)
            break

    for char in line[::-1]:
        if char.isdigit():
            lastDigit = char
            lastDigitIndex = line.rfind(lastDigit)
            break
    
    firstNumberIndex = len(line)
    for key in dictionary.keys():
        position = line.find(key)
        if position != -1 and position < firstNumberIndex:            
            firstNumberIndex = position
            firstNumber = dictionary[key]
    
    lastNumberIndex = 0
    for key in dictionary.keys():
        position = line.rfind(key)
        if position != -1 and position > lastNumberIndex:            
            lastNumberIndex = position
            lastNumber = dictionary[key]

    if firstNumberIndex < firstDigitIndex:
        tensDigit = firstNumber
    else:
        tensDigit = firstDigit

    if lastNumberIndex > lastDigitIndex:
        onesDigit = lastNumber
    else:
        onesDigit = lastDigit

    total =  total + (int(tensDigit) * 10) + int(onesDigit)

print(total) 
file1.close()
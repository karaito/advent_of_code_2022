def computeResult(a,b): #part1
    if b == 'X':
        if a == 'A':
            return 4
        elif a == 'B':
            return 1
        elif a == 'C':
            return 7
    if b == 'Y':
        if a == 'A':
            return 8
        elif a == 'B':
            return 5
        elif a == 'C':
            return 2
    if b == 'Z':
        if a == 'A':
            return 3
        elif a == 'B':
            return 9
        elif a == 'C':
            return 6
    return 0

def computeResult(a,b): #part2
    if b == 'X':
        if a == 'A':
            return 0 + 3
        elif a == 'B':
            return 0 + 1
        elif a == 'C':
            return 0 + 2
    if b == 'Y':
        if a == 'A':
            return 3 + 1
        elif a == 'B':
            return 3 + 2
        elif a == 'C':
            return 3 + 3
    if b == 'Z':
        if a == 'A':
            return 6 + 2
        elif a == 'B':
            return 6 + 3
        elif a == 'C':
            return 6 + 1
    return 0

with open('input.txt') as fp:
    line = fp.readline()
    result = 0
    while line:
        first_player = line[0]
        second_player = line[2]
        temp = computeResult(first_player, second_player)
        result += temp
        print(temp)
        line = fp.readline()
    print(result)
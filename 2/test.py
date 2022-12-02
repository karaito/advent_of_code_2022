opMoves = {
    "A":1,
    "B":2,
    "C":3,
    "X":1,
    "Y":2,
    "Z":3
}

def scoreTurn(turn):
    res = 0
    res += turn[1]
    res += ((turn[1]-turn[0]+1)%3) *3
    return res

with open("input.txt") as f:
    turns = []
    for line in f.readlines():
        line = line.replace("\n","")
        turns.append([opMoves[move] for move in line.split(" ")])

scores = [scoreTurn(turn) for turn in turns]
print(sum(scores))
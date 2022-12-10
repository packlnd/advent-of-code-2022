import sys

# A for Rock, B for Paper, and C for Scissors

MAP = {
    "A": {
        "X": 3 + 0,
        "Y": 1 + 3,
        "Z": 2 + 6,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 2 + 0,
        "Y": 3 + 3,
        "Z": 1 + 6,
    },
}

def sol(lines):
    score = 0
    for line in lines:
        a, b = line.strip().split(" ")
        score += MAP[a][b]
    return score

with open(sys.argv[1]) as f:
    lines = f.readlines()

print(sol(lines))

import sys
from collections import defaultdict


def get_crates(lines):
    crates = defaultdict(list)
    break_line = 0
    for i, line in enumerate(lines):
        if line.startswith(" 1") or line == "\n":
            break_line = i
            break
        j = 1
        for i in range(1, len(line)-1, 4):
            if line[i] != " ":
                crates[j].append(line[i])
            j += 1
    return crates, break_line


def get_moves(lines, start_line):
    for line in lines[start_line:]:
        _1, n, _2, f, _3, t = line.split(" ")
        yield int(n), int(f), int(t)


def get_message(crates, moves):
    for n, f, t in moves:
        # crates[t], crates[f] = crates[f][:n][::-1] + crates[t], crates[f][n:]
        crates[t], crates[f] = crates[f][:n] + crates[t], crates[f][n:]
    ans = ""
    for i in range(len(crates)):
        ans += crates[i+1][0]
    return ans


def sol(lines):
    crates, break_line = get_crates(lines)
    moves = get_moves(lines, break_line + 2)
    return get_message(crates, moves)


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x, f.readlines()))

print(sol(lines))

import sys


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))


def v(r, c):
    return int(lines[r][c])


def get_score_left(tree, r, c):
    for i in range(c-1, -1, -1):
        if v(r, i) >= tree:
            return c-i
    return c


def get_score_top(tree, r, c):
    for i in range(r-1, -1, -1):
        if v(i, c) >= tree:
            return r-i
    return r


def get_score_right(tree, r, c):
    for i in range(c+1, len(lines[0])):
        if v(r, i) >= tree:
            return i-c
    return len(lines[0]) - 1 - c


def get_score_down(tree, r, c):
    for i in range(r+1, len(lines)):
        if v(i, c) >= tree:
            return i-r
    return len(lines)- 1 - r


def sol():
    rows, cols = len(lines), len(lines[0])

    ans = -1
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            tree = v(row, col)
            l = get_score_left(tree, row, col)
            t = get_score_top(tree, row, col)
            r = get_score_right(tree, row, col)
            d = get_score_down(tree, row, col)
            ans = max(l*t*r*d, ans)
    return ans

print(sol())

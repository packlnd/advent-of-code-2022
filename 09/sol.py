import sys


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))


def process_head(direction, x, y):
    if direction == "R":
        return (x, y+1)
    elif direction == "U":
        return (x+1, y)
    elif direction == "L":
        return (x, y-1)
    elif direction =="D":
        return (x-1, y)


def process_tail(xh, yh, xt, yt):
    dx, dy = xh - xt, yh - yt

    if abs(dx) <= 1 and abs(dy) <= 1:
        return (xt, yt)

    nx, ny = 0, 0
    if xh > xt:
        nx += 1
    if xh < xt:
        nx -= 1
    if yh > yt:
        ny += 1
    if yh < yt:
        ny -= 1
    return (xt+nx, yt+ny)



def sol():
    rope = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    positions = set()
    positions.add(rope[-1])
    for line in lines:
        d, n = line[0], int(line[2:])
        for _ in range(n):
            rope[0] = process_head(d, *rope[0])
            for r in range(1, 10):
                rope[r] = process_tail(*rope[r-1], *rope[r])
            positions.add(rope[-1])
    return len(positions)


print(sol())

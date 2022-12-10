import sys


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))


class Screen:
    def __init__(self):
        screen = []
        for _ in range(6):
            screen.append([i for i in range(40)])
        self._screen = screen
        self._row = 0
        self._col = 0

    def draw(self, x, cycle):
        draw = "."
        if self._col in [x-1, x, x+1]:
            draw = "#"
        print(f"Cycle={cycle}, x={x}, ({self._row}, {self._col})={draw}")
        self._screen[self._row][self._col] = draw
        self._col += 1
        if self._col == 40:
            self._row = (self._row + 1) % 6
            self._col = 0

    def print(self):
        for row in self._screen:
            print("".join(row))


def sol():
    screen = Screen()
    cycle, x = 1, 1
    for line in lines:
        screen.draw(x, cycle)
        if line == "noop":
            cycle += 1
        else:
            add = int(line[5:])
            screen.draw(x, cycle+1)
            cycle += 2
            x += add
    screen.print()

print(sol())

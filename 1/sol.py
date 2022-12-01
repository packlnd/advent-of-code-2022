import sys


def sol(lines):
    res = []
    elf = 0
    for line in lines:
        if line == "":
            res.append(elf)
            elf = 0
            continue
        elf += int(line)
    res.append(elf)
    return res


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

print(max(sol(lines)))
print(sum(sorted(sol(lines))[-3:]))

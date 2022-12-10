import sys

def sol(lines):
    ans = 0
    for line in lines:
        a1, a2 = line.split(",")
        a1_1, a1_2 = map(int, a1.split("-"))
        a2_1, a2_2 = map(int, a2.split("-"))
        # ans += 1 if (a1_1 <= a2_1 and a1_2 >= a2_2) or (a2_1 <= a1_1 and a2_2 >= a1_2) else 0
        ans += 1 if (a1_2 >= a2_1 and a1_1 <= a2_1) or (a2_2 >= a1_1 and a2_1 <= a1_1) else 0
    return ans


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))

print(sol(lines))

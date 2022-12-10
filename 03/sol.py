import sys

def sol(lines):
    ans = 0
    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i], lines[i+1], lines[i+2]
        for c in l1:
            if c in l2 and c in l3:
                if c.isupper():
                    ans += ord(c)-ord("A")+26+1
                else:
                    ans += ord(c)-ord("a")+1
                break

    return ans


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))

print(sol(lines))

import sys
from math import prod


with open(sys.argv[1]) as f:
    lines = list(map(lambda x: x.rstrip(), f.readlines()))


def parse_op(s):
    def apply_op(o, x, y):
        if o == "*":
            return x*y
        if o == "+":
            return x+y
        if o == "-":
            return x-y
        if o == "/":
            return x/y
    a, o, b = s.split(" ")
    return lambda old: apply_op(o, old if a == "old" else int(a), old if b == "old" else int(b))


def parse_monkeys():
    monkeys = {}
    for i in range(0, len(lines), 7):
        monkey_i = int(lines[i][7:-1])
        items = list(map(int, lines[i+1][18:].split(", ")))
        operation = lines[i+2][19:]
        test = int(lines[i+3][21:])
        true = int(lines[i+4][29:])
        false = int(lines[i+5][30:])
        monkeys[monkey_i] = {"items": items, "op": parse_op(operation), "test": test, "True": true, "False": false, "inspected": 0}
    return monkeys


def sol():
    monkeys = parse_monkeys()
    div = prod([monkeys[m]["test"] for m in monkeys])
    for i in range(10000):
        if i % 100 == 0:
            print(i)
        for _, monkey in monkeys.items():
            for worry in monkey["items"]:
                new_worry = monkey["op"](worry)
                new_worry = new_worry %  div
                key = "True" if new_worry % monkey["test"] == 0 else "False"
                monkeys[monkey[key]]["items"].append(new_worry)
                monkey["inspected"] += 1
            monkey["items"] = []
    a, b = sorted([monkeys[m]["inspected"] for m in monkeys])[-2:]
    return a * b

print(sol())

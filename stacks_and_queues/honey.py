from collections import deque


def add(bee_n, nectar_n):
    return abs(bee_n + nectar_n)


def subtract(bee_n, nectar_n):
    return abs(bee_n - nectar_n)


def multiply(bee_n, nectar_n):
    return abs(bee_n * nectar_n)


def divide(bee_n, nectar_n):
    return abs(bee_n / nectar_n)


bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
honey_making_symbols = deque(input().split())
made_honey = 0
mapper = {'+': add, '-': subtract, '*': multiply, '/': divide}

while nectars and bees:
    nectar = nectars.pop()
    if nectar >= bees[0]:
        bee = bees.popleft()
        symbol = honey_making_symbols.popleft()
        if nectar == 0 and symbol == '/':
            continue
        made_honey += mapper[symbol](bee, nectar)
print(f'Total honey made: {made_honey}')
if bees:
    print(f'Bees left: {", ".join(str(b) for b in bees)}')
if nectars:
    print(f'Nectar left: {", ".join(str(n) for n in nectars)}')


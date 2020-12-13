import io
import math

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()

ids = []


def take_lower(u, l) -> int:
    diff = (u - l)
    if(diff == 1):
        return l

    return u - round(diff / 2)


def take_higher(u, l) -> int:
    diff = (u - l)
    if(diff == 1):
        return u

    return l + round(diff / 2)


for b in data:
    ru = 127
    rl = 0
    cu = 7
    cl = 0

    for c in b:

        if c == 'B':
            rl = take_higher(ru, rl)
        elif c == 'F':
            ru = take_lower(ru, rl)
        elif c == 'R':
            cl = take_higher(cu, cl)
        elif c == 'L':
            cu = take_lower(cu, cl)

    n = (ru * 8) + cu
    ids.append(n)

ids.sort()

prev = 0
for i in ids:
    if(prev + 2) == i:
        print(i - 1)
    prev = i

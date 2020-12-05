import io
import math

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()

big = 0

for b in data:
    rh = 127
    rl = 0
    ch = 7
    cl = 0

    for c in b:

        if c == 'B':
            diff = (rh - rl)
            if diff == 1:
                rh = rl
            else:
                rl = rl + round(diff / 2)
        elif c == 'F':
            diff = (rh - rl)
            if diff == 1:
                rh = rh - 1
            else:
                rh = rh - round(diff / 2)

        elif c == 'L':
            diff = (ch - cl)
            if diff == 1:
                ch = ch - 1
            else:
                ch = ch - round(diff / 2)
        elif c == 'R':
            diff = (ch - cl)
            if diff != 1:
                cl = cl + round(diff / 2)

    n = (rh * 8) + ch
    if n > big:
        big = n

print(big)

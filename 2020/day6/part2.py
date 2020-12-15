import io
import string
from os import replace

with open("input.txt", "r", encoding="utf-8") as g:
    groups = g.read().split('\n\n')

sum = 0
for g in groups:
    print('-')
    print(g)
    persons = g.split('\n')
    m = dict.fromkeys(string.ascii_lowercase, 0)
    for p in persons:
        print(p)
        for ans in p:
            m[ans] += 1

    for i in m.values():
        if i == len(persons):
            sum += 1

print(sum)

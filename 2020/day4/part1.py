import io
from os import replace

req = ["byr",
       "iyr",
       "eyr",
       "hgt",
       "hcl",
       "ecl",
       "pid",
       ]
# "cid"

reqLen = len(req)


with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().split('\n\n')

total = 0

for p in data:
    n = 0
    fields = p.replace('\n', ' ').split(' ')
    for f in fields:
        if f.split(':')[0] in req:
            n += 1

    if n >= reqLen:
        total += 1

print(total)

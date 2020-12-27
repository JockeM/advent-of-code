import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()

bagDict = dict()

for line in data:
    split = line.split(' ')
    key = ' '.join(split[0:2])
    bags = []

    if 'no other bags.' not in line:
        for b in range(4, len(split), 4):
            bags.append(' '.join(split[b + 1: b + 3]))

    bagDict[key] = bags

print(bagDict)

gold = 'shiny gold'


def contains_gold(bag) -> bool:
    if bag == gold:
        return True

    bags = bagDict[bag]
    for b in bags:
        if contains_gold(b):
            return True

    return False


n = 0
for i in bagDict.keys():
    if i == gold:
        continue

    if contains_gold(i):
        n += 1

print(n)

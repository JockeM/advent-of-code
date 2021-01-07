with open("input.txt", "r", encoding="utf-8") as g:
    data = [int(i) for i in g.read().splitlines()]

data.sort()

jolts = dict.fromkeys(range(1, 4), 0)

prev = 0
for o in data:
    diff = o - prev
    jolts[diff] = jolts[diff] + 1
    prev = o

jolts[3] = jolts[3] + 1


print(jolts[1] * jolts[3])

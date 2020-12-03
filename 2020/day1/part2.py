import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = list(map(int, g.readlines()))

target = 2020

for x in data:
    for y in data:
        for z in data:
            if (x + y + z) == target:
                print(x * y * z)
                exit(0)

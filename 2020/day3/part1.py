import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()


def fn(r, d):
    x = 0  # 3
    y = 0  # 1

    trees = 0

    width = len(data[0])
    height = len(data)
    while y < height:
        if(data[y][x] == '#'):
            trees += 1

        y += d
        x += r

        if(x >= width):
            x = x - width

    return trees


print(fn(1, 1) * fn(3, 1) * fn(5, 1) * fn(7, 1) * fn(1, 2))

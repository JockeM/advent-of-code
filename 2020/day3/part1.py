import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()

x = 0  # 3
y = 0  # 1
trees = 0
width = len(data[0])
height = len(data)
while y < height:
    if(data[y][x] == '#'):
        trees += 1
    y += 1
    x += 3
    if(x >= width):
        x = x - width

print(trees)

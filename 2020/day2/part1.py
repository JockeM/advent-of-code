import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.readlines()

valid = 0

for line in data:
    x = line.split(' ')
    req = x[0].split('-')
    min = int(req[0])
    max = int(req[1])
    letter = x[1][0]
    count = x[2].replace('\n', '').count(letter)
    if count >= min and count <= max:
        valid += 1

print(valid)

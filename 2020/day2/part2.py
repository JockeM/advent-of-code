import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.readlines()

valid = 0

for line in data:
    x = line.split(' ')
    req = x[0].split('-')
    min = int(req[0]) - 1
    max = int(req[1]) - 1
    letter = x[1][0]
    password = x[2].replace('\n', '')
    length = len(password)
    if max > length:
        continue
    if (password[min] == letter) ^ (password[max] == letter):
        valid += 1

print(valid)

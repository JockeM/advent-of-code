import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()

accumulator = 0

i = 0
tried = set()

while i != len(data):
    if i in tried:
        break

    tried.add(i)
    line = data[i]
    split = line.split(' ')
    instruction = split[0]
    argument = split[1]

    if instruction == 'acc':
        if argument[0] == '+':
            accumulator += int(argument[1:])
        else:
            accumulator -= int(argument[1:])

    if instruction == 'jmp':
        if argument[0] == '+':
            i += int(argument[1:])
        else:
            i -= int(argument[1:])
    else:
        i += 1

print(accumulator)

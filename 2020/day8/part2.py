import io

with open("input.txt", "r", encoding="utf-8") as g:
    data = g.read().splitlines()


def run(lines) -> bool:
    accumulator = 0

    i = 0
    tried = set()

    while i != len(lines):
        if i in tried:
            return False

        tried.add(i)
        line = lines[i]
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
    return True


for i in range(0, len(data)):
    line = data[i]
    newData = data[:]

    if 'acc' in line:
        continue
    if 'jmp' in line:
        newData[i] = line.replace('jmp', 'nop')
    else:
        if 'nop' in line:
            newData[i] = line.replace('nop', 'jmp')

    run(newData)

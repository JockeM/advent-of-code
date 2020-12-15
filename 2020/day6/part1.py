import io
from os import replace

with open("input.txt", "r", encoding="utf-8") as g:
    groups = g.read().split('\n\n')

sum = 0
for g in groups:
    persons = g.split('\n')
    answers = []

    for p in persons:
        for ans in p:
            if ans not in answers:
                answers.append(ans)

    sum += len(answers)

print(sum)

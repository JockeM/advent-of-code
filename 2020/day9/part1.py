def find_target(n, list):
    for i, num in enumerate(list[:-1]):
        completment = n - num
        if completment in list[i+1:]:
            return True
    return False


with open("input.txt", "r", encoding="utf-8") as g:
    data = [int(i) for i in g.read().splitlines()]

n = 25

for g in range(n, len(data)):
    prev = data[g-n:g]
    if not find_target(data[g], prev):
        print(data[g])

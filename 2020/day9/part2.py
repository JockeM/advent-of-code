with open("input.txt", "r", encoding="utf-8") as g:
    data = [int(i) for i in g.read().splitlines()]


def get_invalid():
    def find_target(n, list):
        for i, num in enumerate(list[:-1]):
            completment = n - num
            if completment in list[i+1:]:
                return True
        return False

    n = 25

    for g in range(n, len(data)):
        prev = data[g-n:g]
        if not find_target(data[g], prev):
            return data[g]


target = get_invalid()

for i in range(0, len(data)):
    sum = 0
    x = i
    while sum < target:
        sum += data[x]
        if sum == target:
            range = data[i:x]
            range.sort()
            print(range[0] + range[len(range) - 1])
            exit()
        x += 1

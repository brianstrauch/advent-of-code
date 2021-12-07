def simulate(d):
    new_d = {6: d.get(0, 0), 8: d.get(0, 0)}
    for i in range(8):
        new_d[i] = new_d.get(i, 0) + d.get(i + 1, 0)
    return new_d

def total(d):
    t = 0
    for f in d.values():
        t += f
    return t

def part_1(d):
    for _ in range(18):
        d = simulate(d)
    return total(d)

def part_2(d):
    for _ in range(256):
        d = simulate(d)
    return total(d)

with open('6.in') as file:
    line = file.readline().rstrip()

    d = {}
    for x in line.split(','):
        n = int(x)
        d[n] = d.get(n, 0) + 1

    print(part_1(d))
    print(part_2(d))

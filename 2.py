def part_1(arr):
    pos, depth = 0, 0

    for d, x in arr:
        if d == 'forward':
            pos += x
        elif d == 'down':
            depth += x
        elif d == 'up':
            depth -= x

    return pos * depth

def part_2(arr):
    pos, depth, aim = 0, 0, 0

    for d, x in arr:
        if d == 'down':
            aim += x
        elif d == 'up':
            aim -= x
        elif d == 'forward':
            pos += x
            depth += aim * x

    return pos * depth

with open('2.in') as file:
    arr = []

    for line in file.readlines():
        line = line.rstrip()
        d, x = line.split(' ')
        arr.append((d, int(x)))

    print(part_1(arr))
    print(part_2(arr))


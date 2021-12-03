def part_1(arr):
    g = ''
    e = ''

    for i in range(len(arr[0])):
        ones = 0
        for j in range(len(arr)):
            if arr[j][i] == '1':
                ones += 1

        if 2 * ones > len(arr):
            g += '1'
            e += '0'
        else:
            e += '1'
            g += '0'

    return int(g, 2) * int(e, 2)

def part_2(arr):
    o = set(arr)
    c = set(arr)

    for i in range(len(arr[0])):
        ones = set()

        for x in o:
            if x[i] == '1':
                ones.add(x)

        if 2 * len(ones) >= len(o):
            o = ones
        else:
            o = o.difference(ones)

        ones = set()

        for x in c:
            if x[i] == '1':
                ones.add(x)

        if len(ones) == 0 or len(ones) == len(c):
            continue

        if 2 * len(ones) >= len(c):
            c = c.difference(ones)
        else:
            c = ones

    return int(min(o), 2) * int(min(c), 2)

with open('3.in') as file:
    arr = []

    for line in file.readlines():
        line = line.rstrip()
        arr.append(line)
        
    print(part_1(arr))
    print(part_2(arr))


def part_1(segments):
    points = set()
    overlap = set()

    for (x1, y1), (x2, y2) in segments:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                point = (x1, y)
                if point in points:
                    overlap.add(point)
                points.add(point)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                point = (x, y1)
                if point in points:
                    overlap.add(point)
                points.add(point)

    return len(overlap)

def part_2(segments):
    points = set()
    overlap = set()

    for (x1, y1), (x2, y2) in segments:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                point = (x1, y)
                if point in points:
                    overlap.add(point)
                points.add(point)
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                point = (x, y1)
                if point in points:
                    overlap.add(point)
                points.add(point)
        else:
            dx = (x2 - x1) // abs(x2 - x1)
            dy = (y2 - y1) // abs(y2 - y1)
            for i in range(abs(x2 - x1) + 1):
                point = (x1 + dx * i, y1 + dy * i)
                if point in points:
                    overlap.add(point)
                points.add(point)

    return len(overlap)

with open('5.in') as file:
    segments = set()

    for line in file.readlines():
        a, b = line.split(' -> ')

        x1, y1 = [int(x) for x in a.split(',')]
        x2, y2 = [int(x) for x in b.split(',')]
        segments.add(((x1, y1), (x2, y2)))
        
    print(part_1(segments))
    print(part_2(segments))

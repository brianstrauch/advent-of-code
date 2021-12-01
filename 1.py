def count_inc(arr, w):
    count = 0

    for i in range(len(arr) - w):
        if arr[i + w] > arr[i]:
            count += 1

    return count

with open('1.in') as file:
    arr = [int(x.rstrip()) for x in file.readlines()]
    print(count_inc(arr, 1))
    print(count_inc(arr, 3))


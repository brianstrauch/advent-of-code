def find(board, n):
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                return i, j
    return -1, -1

def is_winner(marks):
    for i in range(5):
        h = True
        v = True
        for j in range(5):
            if not marks[i][j]:
                h = False
            if not marks[j][i]:
                v = False
        if h or v:
            return True
    return False

def score(board, marks):
    total = 0
    for i in range(5):
        for j in range(5):
            if not marks[i][j]:
                total += board[i][j]
    return total

def part_1(arr, boards):
    marks = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]

    for n in arr:
        for k in range(len(boards)):
            i, j = find(boards[k], n)
            if i >= 0 and j >= 0:
                marks[k][i][j] = True
                if is_winner(marks[k]):
                    return score(boards[k], marks[k]) * n
    
def part_2(arr, boards):
    marks = [[[False for _ in range(5)] for _ in range(5)] for _ in boards]
    winners = [False for _ in boards]
    win_count = 0

    for n in arr:
        for k in range(len(boards)):
            if winners[k]:
                continue

            i, j = find(boards[k], n)
            if i >= 0 and j >= 0:
                marks[k][i][j] = True
                if is_winner(marks[k]):
                    winners[k] = True
                    win_count += 1
                    if win_count == len(boards):
                        return score(boards[k], marks[k]) * n
    
with open('4.in') as file:
    lines = file.readlines()
    arr = [int(x) for x in lines[0].rstrip().split(',')]

    boards = []
    for i in range(2, len(lines), 6):
        board = []
        for j in range(i, i + 5):
            row = [int(x) for x in lines[j].rstrip().split()]
            board.append(row)
        boards.append(board)

    print(part_1(arr, boards))
    print(part_2(arr, boards))

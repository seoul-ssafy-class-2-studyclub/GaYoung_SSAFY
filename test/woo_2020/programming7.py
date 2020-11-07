def solution(n, horizontal):
    board = [[0] * n for _ in range(n)]
    total = 0
    if horizontal == True:
        x, y, time = 0, 1, 1
        total += time
    else:
        x, y, time = 1, 0, 1
        total += time

    while True:
        board[x][y] = total
        # print(board)

        if x == n - 1 and y == n - 1:
            break

        if x == 0 and y == n-1 and time == 2:
            x += 1
            time = 1
            total += time

        elif y == 0 and x == n-1 and time == 2:
            y += 1
            time = 1
            total += time

        elif (x == 0 or x == n - 1) and time == 2:
            y += 1
            time = 1
            total += time
            # print('a')
            # print(x, y, time)

        elif (x == 0 or x == n - 1) and time == 2:
            y += 1
            time = 1
            total += time
            # print('b')
            # print(x, y, time)

        elif x == 0 and (y == 0 or y == n - 1) and time == 2:
            x += 1
            time = 1
            total += time
            # print('c')
            # print(x, y, time)

        elif (y == 0 or y == n - 1) and time == 2:
            x += 1
            time = 1
            total += time
            # print('d')
            # print(x, y, time)

        elif 0 <= x + 1 < n and 0 <= y - 1 < n and board[x + 1][y - 1] == 0:
            x += 1
            y -= 1
            time = 2
            total += time
            # print('e')
            # print(x, y, time)

        elif 0 <= x - 1 < n and 0 <= y + 1 < n and board[x - 1][y + 1] == 0:
            x -= 1
            y += 1
            time = 2
            total += time
            # print('f')
            # print(x, y, time)

    print(board)
    return board

n = 99
horizontal = False
print(solution(n, horizontal))

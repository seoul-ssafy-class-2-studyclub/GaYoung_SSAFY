for t in range(10):
    board = []
    N = int(input())
    for i in range(100):
        board.append(list(map(int, input().split())))

    start = []
    for i in range(len(board)):
        if board[99][i] == 1:
            start += [i]
    # print(start)  # [0, 4, 6, 9]

    length = [0] * len(start)
    # print(length)  # [0, 0, 0, 0]

    for i in range(len(start)):
        for k in range(99, 0, -1):
            if start[i] != 0 and board[k][start[i] - 1] == 1:
                while start[i] > 0 and board[k][start[i] - 1] == 1:
                    start[i] -= 1
                    length[i] += 1

            elif start[i] != 99 and board[k][start[i] + 1] == 1:
                while start[i] < 99 and board[k][start[i] + 1] == 1:
                    start[i] += 1
                    length[i] += 1

    x = length.index(min(length))
    print('#{} {}'.format(N, start[x]))

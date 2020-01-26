for t in range(int(input())):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    a = N // 2
    board[a - 1][a - 1] = board[a][a] = 2
    board[a][a - 1] = board[a - 1][a] = 1
    # print(board)

    near = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    
    for m in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1

        if color == 1:
            another = 2
        elif color == 2:
            another = 1

        board[y][x] = color
        for a, b in near:
            xi = x + a
            yi = y + b
            if 0 <= xi < N and 0 <= yi < N:
                if board[yi][xi] == another:
                    cnt = 0
                    while board[yi][xi] == another:
                        xi = xi + a
                        yi = yi + b
                        cnt += 1
                        if xi < 0 or xi >= N or yi < 0 or yi >= N or board[yi][xi] == 0:
                            cnt = 0
                            break
                    xi = x + a
                    yi = y + b

                    while cnt != 0:
                        board[yi][xi] = color
                        xi = xi + a
                        yi = yi + b
                        cnt -= 1
        black = 0
        white = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    black += 1
                elif board[i][j] == 2:
                    white += 1

    print('#{} {} {}'.format(t+1, black, white))


